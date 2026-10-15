# Week 4 — Evaluating Classification Models

> **Main idea:** Training a model gives us predictions. Evaluation tells us whether those predictions are useful.
>
> This lecture uses customer churn prediction to explain accuracy, confusion matrices, precision, recall, ROC curves, AUC, cross-validation, and regularization.

---

## 1. The Classification Workflow

For customer churn:

- **0 = customer stays:** negative class.
- **1 = customer churns:** positive class.

“Positive” identifies the event we want to detect; it does not mean a desirable outcome.

The workflow is:

1. Prepare and clean the data.
2. Split it into training, validation, and test sets.
3. Fit the vectorizer on training features.
4. Train logistic regression using training features and labels.
5. Predict probabilities on validation data.
6. Evaluate performance and select settings.
7. Retrain on the full training pool.
8. Evaluate the final model on the held-out test set.

### Two objects work together

| Object | What it learns | Training operation | Operation on new data |
|---|---|---|---|
| `DictVectorizer` | Feature names and column order | `fit_transform()` | `transform()` |
| `LogisticRegression` | Weights and intercept | `fit(X_train, y_train)` | `predict_proba(X)` |

**Rule:** Keep every trained model paired with the vectorizer used to train it.

---

## 2. Training, Validation, and Test Data

| Dataset | Purpose |
|---|---|
| Training | Learn the encoding and model weights |
| Validation | Compare models, thresholds, and hyperparameters |
| Test | Evaluate the final model after choices are fixed |
| Full training pool | Training + validation data, used for cross-validation and final refitting |

In the notebook:

- The test set receives 20% of the original data.
- Validation receives 33% of the remaining 80%.
- This produces approximately 53.6% training, 26.4% validation, and 20% test.

### Avoid target leakage

The target, `churn`, must not be included among the input features.

Either remove it from the feature DataFrame or explicitly select feature columns that exclude it.

Preprocessing that learns from data, such as scaling or mean imputation, must be fitted using training data only.

---

## 3. Encoding Features with DictVectorizer

The following expression converts customer rows into dictionaries:

`df_train[features].to_dict(orient='records')`

For example, a customer becomes:

`{'contract': 'month-to-month', 'tenure': 5}`

`DictVectorizer` then converts these dictionaries into a numeric matrix:

- String values become one-hot encoded columns.
- Numeric values remain numeric.
- The fitted vectorizer remembers the column names and their order.

| Expression | Meaning |
|---|---|
| `categorical + numerical` | Join two lists of feature names |
| `df_train[features]` | Select feature columns |
| `.to_dict(orient='records')` | Create one dictionary per row |
| `dv.fit_transform(train_dicts)` | Learn the encoding and encode training rows |
| `dv.transform(val_dicts)` | Encode validation rows using the learned layout |

**Important:** A numeric 0/1 column remains numeric even if its name appears in a list called `categorical`.

---

## 4. How Logistic Regression Produces Probabilities

Logistic regression combines the input features into one score:

$$
z = b + w_1x_1 + w_2x_2 + \cdots + w_dx_d
$$

It then applies the sigmoid function:

$$
P(y=1 \mid x) = \frac{1}{1+e^{-z}}
$$

Here:

- $x_j$ is a feature value.
- $w_j$ is its learned weight.
- $b$ is the intercept.
- The result is an estimated probability of churn.

### Why are there only two output columns?

`model.predict_proba(X_val)` returns one probability for each class:

| Customer | Probability of staying | Probability of churn |
|---|---:|---:|
| A | 0.80 | 0.20 |
| B | 0.30 | 0.70 |

The two columns represent **two possible classes**, not two input features.

For a model with `model.classes_ = [0, 1]`:

`model.predict_proba(X_val)[:, 1]`

selects the churn probability.

### Understanding the shapes

For $m$ customers and $d$ encoded features:

| Object | Shape |
|---|---|
| `X_val` | `(m, d)` |
| `model.predict_proba(X_val)` | `(m, 2)` |
| `y_pred` | `(m,)` |
| `y_val` | `(m,)` |

In `[:, 1]`:

- `:` selects every row.
- `1` selects the second column because Python indexing starts at zero.

---

## 5. Probabilities Versus Class Decisions

A probability is not yet a class decision.

We use a threshold $t$ to convert a probability into a prediction:

$$
\hat{y} =
\begin{cases}
1 & \text{if } p \ge t \\
0 & \text{if } p < t
\end{cases}
$$

For example:

`y_decision = y_pred >= 0.5`

| Churn probability | Decision at 0.5 | Decision at 0.3 |
|---|---|---|
| 0.20 | Stay | Stay |
| 0.40 | Stay | Churn |
| 0.80 | Churn | Churn |

**Changing the threshold changes decisions without retraining the model.**

---

## 6. Accuracy

**Question:** Of all predictions, what fraction was correct?

$$
\text{Accuracy} =
\frac{\text{Number of correct predictions}}
{\text{Total number of predictions}}
$$

The notebook calculates:

`(y_decision == y_val).mean()`

This works because:

1. `y_decision == y_val` compares each prediction with its actual label.
2. The comparison produces `True` or `False`.
3. The mean treats `True` as 1 and `False` as 0.
4. The result is the fraction of correct predictions.

| Expression | Meaning |
|---|---|
| `(y_decision == y_val).sum()` | Number of correct predictions |
| `(y_decision == y_val).mean()` | Fraction of correct predictions |
| `accuracy_score(y_val, y_decision)` | Same accuracy calculation using scikit-learn |

### Why accuracy can be misleading

Suppose:

- 900 customers stay.
- 100 customers churn.

A model that predicts “stay” for everyone achieves:

$$
\text{Accuracy} = \frac{900}{1000} = 90\%
$$

But it catches **zero churners**.

> With imbalanced classes, high accuracy does not necessarily mean the model is useful.

---

## 7. The Confusion Matrix

A confusion matrix separates predictions into four groups.

| Actual outcome | Predicted stay (0) | Predicted churn (1) |
|---|---|---|
| Stay (0) | **TN — True Negative** | **FP — False Positive** |
| Churn (1) | **FN — False Negative** | **TP — True Positive** |

### Meaning in the churn problem

| Outcome | Interpretation | Possible consequence |
|---|---|---|
| TP | Correctly identified a churner | Opportunity for a retention action |
| TN | Correctly identified a customer who stays | No unnecessary intervention |
| FP | Flagged a customer who would stay | Wasted outreach or discount |
| FN | Missed a customer who churns | Lost customer or revenue |

**Memory aid:**

- **P/N** describes the model's prediction.
- **T/F** describes whether that prediction was correct.

### How the Boolean calculations work

For true positives:

`((y_pred >= t) & (y_val == 1)).sum()`

This counts customers who:

1. Were predicted to churn, **and**
2. Actually churned.

The `&` operator performs element-wise AND across arrays.

Use parentheses around comparisons. Python's `and` is not a replacement for `&` when combining Boolean arrays.

### Matrix layout

The notebook and scikit-learn use:

$$
\begin{bmatrix}
TN & FP \\
FN & TP
\end{bmatrix}
$$

Rows represent actual classes. Columns represent predicted classes.

Dividing this matrix by its total count gives each outcome as a fraction of **all customers**. It does not directly calculate recall or false positive rate.

---

## 8. Precision

**Question:** Of the customers we predicted would churn, how many actually churned?

$$
\text{Precision} = \frac{TP}{TP+FP}
$$

The denominator is the number of **predicted positives**.

### Example

If we flag 110 customers and 60 actually churn:

$$
\text{Precision} = \frac{60}{110} \approx 54.5\%
$$

Low precision means many false alarms.

Precision matters when retention actions are expensive or outreach capacity is limited.

---

## 9. Recall

**Question:** Of all customers who actually churned, how many did we identify?

$$
\text{Recall} = \frac{TP}{TP+FN}
$$

The denominator is the number of **actual positives**.

### Example

If 100 customers churn and we identify 60:

$$
\text{Recall} = \frac{60}{100} = 60\%
$$

Low recall means many churners were missed.

Recall matters when missing a positive case is costly.

### Precision versus recall

| Metric | Starts with… | Question |
|---|---|---|
| Precision | Customers we flagged | How many flags were correct? |
| Recall | Customers who actually churned | How many did we catch? |

Both have $TP$ in the numerator, but their denominators differ.

---

## 10. F1 Score

F1 combines precision and recall using their harmonic mean:

$$
F_1 =
2 \times
\frac{\text{Precision}\times\text{Recall}}
{\text{Precision}+\text{Recall}}
$$

An equivalent formula is:

$$
F_1 = \frac{2TP}{2TP+FP+FN}
$$

F1 is low when either precision or recall is low.

It does not include true negatives and does not directly account for financial costs.

### Undefined metrics

- Precision is undefined if no customers are predicted positive.
- Recall is undefined if there are no actual positives.

Scikit-learn's `zero_division=0` explicitly chooses to report zero in these cases.

---

## 11. Worked Example

Suppose we evaluate 1,000 customers:

| Actual outcome | Predicted stay | Predicted churn | Total |
|---|---:|---:|---:|
| Stay | TN = 850 | FP = 50 | 900 |
| Churn | FN = 40 | TP = 60 | 100 |

### Accuracy

$$
\frac{850+60}{1000}=91\%
$$

### Precision

$$
\frac{60}{60+50}\approx54.5\%
$$

### Recall

$$
\frac{60}{60+40}=60\%
$$

### F1

$$
\frac{2(60)}{2(60)+50+40}\approx57.1\%
$$

> The model has 91% accuracy, but almost half its churn alerts are false alarms, and it misses 40% of actual churners.

---

## 12. Choosing a Threshold

The notebook evaluates multiple thresholds using:

`np.linspace(0, 1, 21)`

This creates 21 evenly spaced values, including 0 and 1:

$0.00,\ 0.05,\ 0.10,\ \ldots,\ 1.00$

For each threshold:

1. Convert probabilities into decisions.
2. Compare decisions with actual labels.
3. Calculate the metric.
4. Plot the metric against the threshold.

| Threshold change | Effect on predictions | Recall | Typical precision behavior |
|---|---|---|---|
| Lower threshold | More customers flagged | Increases or stays equal | Often decreases |
| Higher threshold | Fewer customers flagged | Decreases or stays equal | Often increases |

**Precision is not guaranteed to change monotonically.** It can fluctuate as specific customers enter or leave the flagged group.

Choose a threshold using validation data and the costs of false positives and false negatives.

---

## 13. True Positive Rate and False Positive Rate

### True Positive Rate — TPR

$$
TPR = \frac{TP}{TP+FN}
$$

TPR is the same as **recall**.

It asks:

> Of actual churners, what fraction did we flag?

Higher is better.

### False Positive Rate — FPR

$$
FPR = \frac{FP}{FP+TN}
$$

It asks:

> Of actual non-churners, what fraction did we wrongly flag?

Lower is better.

### True Negative Rate — TNR

$$
TNR = \frac{TN}{TN+FP} = 1-FPR
$$

TNR is also called **specificity**.

**TPR and TNR are different metrics.**

### Why their denominators matter

| Rate | Denominator |
|---|---|
| TPR | All actual positives |
| FPR | All actual negatives |
| Precision | All predicted positives |

TPR and FPR are calculated within actual classes. Their formulas do not directly depend on the overall class proportions.

Precision also depends on how common the positive class is.

---

## 14. ROC Curve

ROC stands for **Receiver Operating Characteristic**.

A ROC curve plots:

- **Horizontal axis:** False Positive Rate.
- **Vertical axis:** True Positive Rate.

Each threshold creates one pair:

$$
(FPR,\ TPR)
$$

Changing the threshold traces out the curve.

### How to read it

| Location | Interpretation |
|---|---|
| Near top-left | Many positives detected, few false alarms |
| Near diagonal | Random-level ranking |
| Bottom-left | Nobody flagged |
| Top-right | Everybody flagged |

The ideal operating point is:

$$
FPR=0,\qquad TPR=1
$$

### Two plots that should not be confused

| Plot | Horizontal axis | Vertical axis |
|---|---|---|
| Rates versus threshold | Threshold | TPR and FPR |
| ROC curve | FPR | TPR |

`roc_curve(y_val, y_pred)` returns the FPR values, TPR values, and corresponding thresholds.

A manual threshold grid is useful for learning. Scikit-learn uses thresholds based on the actual scores and includes an all-negative operating point.

---

## 15. Random Model Baseline

The notebook creates random scores between 0 and 1.

These scores have no relationship with the actual churn labels.

For random ranking:

- The ROC curve is approximately diagonal.
- ROC AUC is approximately 0.5.
- Finite samples produce some variation.

### Important comparison

To calculate random-model accuracy, compare:

`y_rand >= 0.5`

with:

`y_val`

Do not compare the random decisions with `y_pred`, because `y_pred` contains the trained model's probabilities, not the real labels.

A random scoring model is different from the always-stay baseline:

- Random decisions at threshold 0.5 have expected accuracy 50%.
- Always predicting stay can have much higher accuracy when most customers stay.

---

## 16. Ideal Model Illustration

The notebook constructs an artificial perfect ranking.

### Step 1: Count the classes

- `num_neg`: number of customers who stay.
- `num_pos`: number of customers who churn.

### Step 2: Create ordered labels

`np.repeat([0, 1], [num_neg, num_pos])`

creates all the zeros first, followed by all the ones.

For example:

$[0,\ 0,\ 0,\ 1,\ 1]$

### Step 3: Create increasing scores

`np.linspace(0, 1, len(y_ideal))`

creates evenly spaced scores:

$[0.00,\ 0.25,\ 0.50,\ 0.75,\ 1.00]$

Every positive receives a higher score than every negative.

A threshold between the last negative score and the first positive score separates the classes perfectly.

### What this demonstrates

- Perfect ranking gives AUC 1.
- A separating threshold gives 100% accuracy.
- This is a constructed teaching example, not a trained model.

**Do not independently sort real labels and predictions.** They must stay aligned customer by customer.

Avoid rounding the artificial scores before evaluation, because rounding can create ties across the class boundary.

---

## 17. Area Under the ROC Curve — AUC

ROC AUC summarizes the area under the ROC curve.

It measures how well the model **ranks positives above negatives**.

| AUC | Meaning |
|---|---|
| 1.0 | Perfect ranking |
| About 0.5 | Random-level ranking |
| Below 0.5 | Worse than random ranking; check labels and score direction |

### Two ways to calculate it

| Expression | Meaning |
|---|---|
| `auc(fpr, tpr)` | Integrate a previously calculated ROC curve |
| `roc_auc_score(y_val, y_pred)` | Calculate ROC AUC directly from labels and scores |

Use continuous probabilities or scores to evaluate the full ranking.

### Pairwise interpretation

Randomly choose:

- One actual churner.
- One actual non-churner.

AUC measures how often the churner receives the higher score, with half credit for ties:

$$
AUC =
P(s_+ > s_-)
+
\frac{1}{2}P(s_+ = s_-)
$$

The notebook estimates this by repeatedly sampling positive-negative score pairs.

### What AUC does not mean

**AUC of 0.85 does not mean 85% accuracy.**

It means approximately 85% pairwise ranking success, including half credit for tied scores.

AUC also does not tell us:

- Which threshold to use.
- How many retention offers to send.
- Whether predicted probabilities are well calibrated.

A model can rank customers well while its probability estimates are inaccurate.

---

## 18. Reusable Training and Prediction Functions

The notebook separates the workflow into two functions.

### `train(df_train, y_train, C)`

This function:

1. Selects feature columns.
2. Converts rows to dictionaries.
3. Fits a new vectorizer.
4. Creates the training matrix.
5. Fits logistic regression.
6. Returns the fitted vectorizer and model.

### `predict(df, dv, model)`

This function:

1. Selects the same feature columns.
2. Converts rows to dictionaries.
3. Applies the fitted vectorizer.
4. Returns churn probabilities.

### Why does prediction not take the target?

Training needs known outcomes to learn the weights.

Prediction estimates outcomes for new rows, so it needs only:

- Input features.
- The fitted vectorizer.
- The fitted model.

Actual labels are needed afterward for evaluation.

---

## 19. K-Fold Cross-Validation

One train-validation split can give a result that depends on which customers happen to be in each subset.

Cross-validation repeats training and evaluation across several splits.

For 5 folds:

| Run | Validation fold | Training folds |
|---|---|---|
| 1 | Fold 1 | Folds 2–5 |
| 2 | Fold 2 | Folds 1, 3, 4, 5 |
| 3 | Fold 3 | Folds 1, 2, 4, 5 |
| 4 | Fold 4 | Folds 1, 2, 3, 5 |
| 5 | Fold 5 | Folds 1–4 |

Each row is used for validation once.

The test set stays outside this process.

### Understanding the code

| Expression | Meaning |
|---|---|
| `KFold(n_splits=5)` | Create five folds |
| `shuffle=True` | Shuffle rows before assigning folds |
| `random_state=1` | Make the shuffled assignment reproducible |
| `kfold.split(df_train_full)` | Generate row positions for each split |
| `next(kfold.split(...))` | Retrieve the first split only |
| `.iloc[train_idx]` | Select training rows by position |
| `.iloc[val_idx]` | Select validation rows by position |
| `tqdm(...)` | Display progress |

### Fit fresh objects inside every fold

Each run must fit:

- A new vectorizer on that fold's training rows.
- A new model on that fold's training matrix.

Fitting preprocessing on the entire dataset before cross-validation leaks validation information.

### Mean and standard deviation

$$
\text{Mean AUC} =
\frac{1}{k}\sum_{i=1}^{k} AUC_i
$$

| Summary | Meaning |
|---|---|
| Mean AUC | Average validation performance |
| Standard deviation | Variation between fold results |

`mean ± std` is a descriptive summary, not automatically a confidence interval.

For imbalanced classification, `StratifiedKFold` is a useful extension because it approximately preserves the class proportions in every fold.

ROC AUC requires both actual classes to be present.

---

## 20. Regularization and the Parameter C

Regularization discourages large model weights and helps control overfitting.

In scikit-learn logistic regression:

> **C is the inverse of regularization strength.**

| C | Regularization | Possible effect |
|---|---|---|
| Smaller | Stronger | More restricted weights; may underfit |
| Larger | Weaker | Less restricted weights; may overfit |

These are tendencies, not guaranteed outcomes.

### C versus threshold

| Setting | What it changes | Requires retraining? |
|---|---|---|
| C | Learned model weights | Yes |
| Decision threshold | Decisions made from existing scores | No |

### Choosing C with cross-validation

For every candidate value:

1. Train and validate across the same folds.
2. Calculate AUC for each fold.
3. Calculate mean AUC and standard deviation.
4. Compare candidates.
5. Select the setting using development data.

With six candidate values and five folds:

$$
6 \times 5 = 30 \text{ model fits}
$$

Using the same folds makes comparisons more consistent.

Small differences in mean AUC should be considered alongside fold variation and practical relevance.

---

## 21. Final Test Evaluation

Once model settings are fixed:

1. Combine the training and validation pool.
2. Fit a new vectorizer and model on that full pool.
3. Transform the test features with the fitted vectorizer.
4. Predict test probabilities.
5. Compare predictions with test labels.

The test labels are extracted at this stage because they are now needed for evaluation.

**Do not repeatedly tune settings based on test results.** Doing so turns the test set into another validation set.

If you need class decisions, use a threshold already chosen from development data.

---

## 22. Precision–Recall Curve

The notebook lists precision–recall curves as further exploration.

A precision–recall curve plots:

- **Horizontal axis:** Recall.
- **Vertical axis:** Precision.

It shows how these two metrics change as the threshold changes.

This is particularly useful when the positive class is rare.

| Curve | Focus |
|---|---|
| ROC | Detection rate versus false positive rate |
| Precision–recall | Reliability of positive predictions versus coverage of actual positives |

For uninformative scores, precision is around the positive-class prevalence.

### Average precision and PR area

`average_precision_score(y_val, y_pred)` calculates **average precision**, or AP.

AP and the trapezoidal area under a precision–recall curve are different summaries. Report which one you use.

The precision and recall arrays returned by `precision_recall_curve` contain one more value than its threshold array.

---

## 23. Common Mistakes

| Mistake | Correction |
|---|---|
| Calling TPR “TNR” | TPR is recall; TNR is specificity |
| Comparing random predictions with model probabilities | Compare predictions with actual labels |
| Assuming `np.linspace` generates random values | It generates evenly spaced values |
| Treating AUC as accuracy | AUC measures ranking; accuracy measures decisions |
| Ignoring ties in pairwise AUC | Give tied scores half credit |
| Assuming precision always rises with threshold | It can fluctuate |
| Fitting the vectorizer on validation data | Use the training vectorizer's `transform()` |
| Mixing vectorizers between models | Keep each model with its fitted vectorizer |
| Including `churn` in the features | Exclude the target explicitly |
| Mixing `Churn` and `churn` | Normalize column names consistently |
| Using `and` with Boolean arrays | Use element-wise `&` with parentheses |
| Assigning a number to the name `auc` | Use `auc_value` to avoid overwriting the imported function |
| Selecting C using test performance | Select it using validation or cross-validation |

---

## 24. Quick Reference

| Metric or method | Main question |
|---|---|
| Accuracy | How often are predictions correct overall? |
| Confusion matrix | How many examples fall into each prediction outcome? |
| Precision | How trustworthy are the positive predictions? |
| Recall / TPR | How many actual positives did we catch? |
| FPR | How many actual negatives did we wrongly flag? |
| F1 | What is the harmonic mean of precision and recall? |
| ROC curve | How does detection trade off against false alarms? |
| ROC AUC | How well do scores rank positives above negatives? |
| Precision–recall curve | How do precision and recall trade off? |
| Cross-validation | How does performance vary across data splits? |
| Regularization tuning | Which C gives suitable validation performance? |
| Test evaluation | How does the selected model perform on held-out data? |

> **Final mental model:** Training learns weights. Prediction produces scores. A threshold turns scores into decisions. Evaluation compares scores or decisions with actual outcomes.