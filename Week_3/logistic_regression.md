# Logistic Regression — Telco Customer Churn

## 1. What does logistic regression predict?

In our Telco project, we want to predict **whether a customer will churn**.

Our target variable is:

- **`y = 1`**: the customer churns.
- **`y = 0`**: the customer stays.

Logistic regression uses customer features to estimate the **probability of churn**:

$$
p = P(y=1 \mid \mathbf{x})
$$

This means: “The probability that the customer churns, given their features.”

For example, `p = 0.80` means the model estimates an **80% chance of churn**. It does not guarantee that the customer will churn.

---

## 2. Linear regression versus logistic regression

| Aspect | Linear regression | Logistic regression |
|---|---|---|
| Purpose | Predict a numerical value | Predict the probability of a category |
| Telco example | Predict monthly charges | Predict customer churn |
| Training target | A number, such as $75 | A label: `0` or `1` |
| Model output | Any real number | A probability between 0 and 1 |
| Common loss function | Mean squared error | Binary log loss |

**Despite its name, logistic regression is used for classification.**

---

## 3. Step 1: Calculate a weighted score

Linear regression calculates a weighted sum:

$$
\hat{y} = b + w_1x_1 + w_2x_2 + \cdots + w_mx_m
$$

Logistic regression starts with the same calculation, but calls the result a **score**, represented by `z`:

$$
z = b + w_1x_1 + w_2x_2 + \cdots + w_mx_m
$$

| Symbol | Meaning |
|---|---|
| $b$ | Intercept: the starting score |
| $x_j$ | Value of feature $j$ for one customer |
| $w_j$ | Learned weight for feature $j$ |
| $m$ | Number of features |
| $z$ | Score before conversion into a probability |

For a simplified model using tenure and monthly charges:

$$
z = b
+ w_{\text{tenure}} \times \text{tenure}
+ w_{\text{charges}} \times \text{monthlycharges}
$$

**Problem:** this score could be negative or greater than 1. It cannot directly represent a probability.

---

## 4. Step 2: Convert the score into a probability

We pass the score through the **sigmoid function**:

$$
p = \sigma(z) = \frac{1}{1 + e^{-z}}
$$

Here, $e$ is a mathematical constant approximately equal to 2.718.

The sigmoid converts any finite score into a value **between 0 and 1**.

| Score $z$ | Probability $p$, approximately | Interpretation |
|---:|---:|---|
| -3 | 0.047 | 4.7% predicted chance of churn |
| -1 | 0.269 | 26.9% predicted chance of churn |
| 0 | 0.500 | 50% predicted chance of churn |
| 1 | 0.731 | 73.1% predicted chance of churn |
| 3 | 0.953 | 95.3% predicted chance of churn |

**Higher score → higher predicted churn probability.**

The complete prediction formula is:

$$
p = \frac{1}{1 + e^{-(b + w_1x_1 + \cdots + w_mx_m)}}
$$

---

## 5. Worked example: one Telco customer

Suppose our model has the following weights:

$$
b = -1
$$

$$
w_{\text{tenure}} = -0.05
$$

$$
w_{\text{charges}} = 0.02
$$

> These weights are made up to explain the calculation. They are not findings from the Telco dataset.

The customer has:

- **Tenure:** 10 months.
- **Monthly charges:** $80.

### Calculate the score

$$
z = -1 + (-0.05 \times 10) + (0.02 \times 80)
$$

$$
z = -1 - 0.5 + 1.6 = 0.1
$$

### Apply the sigmoid

$$
p = \frac{1}{1 + e^{-0.1}} \approx 0.525
$$

The model estimates a **52.5% chance of churn** for this customer.

---

## 6. Step 3: Convert the probability into a class

The probability is the model's estimate. To make a yes/no prediction, we choose a **threshold**.

With a threshold of 0.50:

$$
\hat{y} =
\begin{cases}
1 & \text{if } p \geq 0.50 \\
0 & \text{if } p < 0.50
\end{cases}
$$

| Predicted probability | Predicted class |
|---:|---|
| 0.20 | `0`: stays |
| 0.49 | `0`: stays |
| 0.525 | `1`: churns |
| 0.80 | `1`: churns |

Our example customer has `p = 0.525`, so we predict **churn** at this threshold.

### Why might we change the threshold?

For a retention campaign:

- A **lower threshold** flags more customers, potentially catching more churners but also flagging more customers who would stay.
- A **higher threshold** flags fewer customers, potentially missing more churners.

The threshold changes the **decision**, not the underlying probability.

---

## 7. How does the model learn its weights?

During training, the model adjusts its weights to reduce prediction error.

### Linear regression: mean squared error

$$
\text{MSE} =
\frac{1}{n}
\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

This measures the squared distance between predicted and actual numerical values.

### Logistic regression: binary log loss

$$
L =
-\frac{1}{n}
\sum_{i=1}^{n}
\left[
y_i\ln(p_i) + (1-y_i)\ln(1-p_i)
\right]
$$

Where:

| Symbol | Meaning |
|---|---|
| $n$ | Number of training customers |
| $y_i$ | Actual churn label for customer $i$ |
| $p_i$ | Predicted churn probability for customer $i$ |
| $\ln$ | Natural logarithm |

For one customer:

$$
\text{Loss} =
\begin{cases}
-\ln(p) & \text{if } y=1 \\
-\ln(1-p) & \text{if } y=0
\end{cases}
$$

In plain language: **the loss is smaller when the model assigns a high probability to the outcome that actually happened.**

### Example: the customer actually churned

| Predicted churn probability | Loss, approximately |
|---:|---:|
| 0.90 | 0.105 |
| 0.50 | 0.693 |
| 0.10 | 2.303 |

Predicting only a 10% chance of churn for someone who churned produces a larger loss than predicting a 90% chance.

**Log loss penalizes confident mistakes heavily.**

Training reduces average log loss, often with an additional regularization penalty.

---

## 8. How do we interpret the weights?

Holding all other features fixed:

- A **positive weight** means increasing that feature increases the score and predicted churn probability.
- A **negative weight** means increasing that feature decreases the score and predicted churn probability.

In our illustrative example:

| Feature | Weight | Interpretation |
|---|---:|---|
| Tenure | -0.05 | Longer tenure lowers predicted churn probability |
| Monthly charges | +0.02 | Higher charges raise predicted churn probability |

> A weight is not a fixed percentage-point change in probability. The sigmoid is curved, so the probability change depends on the starting score.

These are associations learned by the model; they do not establish causation.

### Optional: the connection to log-odds

Logistic regression models **log-odds** as a linear combination of features:

$$
\ln\left(\frac{p}{1-p}\right)
= b + w_1x_1 + \cdots + w_mx_m
$$

Here:

$$
\text{Odds} = \frac{p}{1-p}
$$

Holding other features fixed, a one-unit increase in feature $j$ multiplies the odds by $e^{w_j}$.

You can understand the basic prediction process without memorizing this connection.

---

## 9. What about categorical features?

Features such as `contract` and `internetservice` must be converted into numerical inputs.

For example:

- `contract_month_to_month = 1`: customer has a month-to-month contract.
- `contract_month_to_month = 0`: customer does not.

This indicator becomes another feature in the weighted score. Its weight interpretation depends on the encoding used.

---

## What to remember

**Linear regression:**

Weighted sum → predicted numerical value.

**Logistic regression:**

Weighted sum → sigmoid → predicted probability → optional threshold → predicted class.

For our Telco project, logistic regression estimates:

**“Given this customer's features, how likely are they to churn?”**

## Understanding the sigmoid graph and its range

The sigmoid function is:

$$
p = \sigma(z) = \frac{1}{1 + e^{-z}}
$$

Its graph is an **S-shaped curve**:

- The horizontal axis shows the score $z$.
- The vertical axis shows the probability $p$.
- Moving from left to right, the curve rises smoothly from near 0 to near 1.
- It passes through $(0, 0.5)$.
- It is steepest around $z=0$ and flattens at both ends.

### 1. Why is the output always between 0 and 1?

The key mathematical fact is:

$$
e^{-z} > 0
$$

An exponential is always positive, regardless of whether $z$ is positive, negative, or zero.

Therefore, the denominator is always greater than 1:

$$
1 + e^{-z} > 1
$$

We are dividing 1 by a positive number greater than 1, so:

$$
0 < \frac{1}{1 + e^{-z}} < 1
$$

Thus:

$$
0 < \sigma(z) < 1
$$

**For any finite score, the sigmoid never equals exactly 0 or exactly 1 mathematically. It can get arbitrarily close to either.**

Computer calculations may round extremely small or large results to 0 or 1.

### 2. What happens when the score is zero?

Substitute $z=0$:

$$
\sigma(0) = \frac{1}{1 + e^{0}}
$$

Since $e^0=1$:

$$
\sigma(0) = \frac{1}{1+1} = 0.5
$$

This explains why the graph passes through **$(0, 0.5)$**.

For our churn model, a score of zero corresponds to a predicted churn probability of 50%.

### 3. What happens when the score is very positive?

Let $z=5$:

$$
e^{-5} \approx 0.0067
$$

Therefore:

$$
\sigma(5) = \frac{1}{1 + 0.0067} \approx 0.9933
$$

As $z$ becomes more positive, $e^{-z}$ approaches zero. The denominator approaches 1, and the output approaches 1:

$$
\lim_{z \to +\infty}\sigma(z) = 1
$$

**Large positive score → probability close to 1.**

### 4. What happens when the score is very negative?

Let $z=-5$. Notice how the two negative signs cancel:

$$
e^{-z} = e^{-(-5)} = e^5 \approx 148.4
$$

Therefore:

$$
\sigma(-5) = \frac{1}{1 + 148.4} \approx 0.0067
$$

As $z$ becomes more negative, $e^{-z}$ becomes very large. Dividing 1 by this large denominator produces a value close to zero:

$$
\lim_{z \to -\infty}\sigma(z) = 0
$$

**Large negative score → probability close to 0.**

### 5. Values that trace the S-shaped curve

| Score $z$ | $e^{-z}$, approximately | Probability $\sigma(z)$, approximately |
|---:|---:|---:|
| -5 | 148.413 | 0.0067 |
| -3 | 20.086 | 0.0474 |
| -1 | 2.718 | 0.2689 |
| 0 | 1.000 | 0.5000 |
| 1 | 0.368 | 0.7311 |
| 3 | 0.050 | 0.9526 |
| 5 | 0.007 | 0.9933 |

The horizontal lines $p=0$ and $p=1$ are called **asymptotes**: the curve approaches them without reaching them for a finite score.

### 6. Why is the curve steep in the middle and flat at the ends?

The derivative tells us how quickly the probability changes as the score changes:

$$
\frac{dp}{dz} = \sigma(z)\left(1-\sigma(z)\right)
$$

Since $p=\sigma(z)$, we can write:

$$
\frac{dp}{dz} = p(1-p)
$$

We can rewrite this expression as:

$$
p(1-p) = \frac{1}{4} - \left(p-\frac{1}{2}\right)^2
$$

The squared term is always nonnegative, so the largest possible slope is $\frac{1}{4}$, reached when $p=0.5$.

| Probability $p$ | Slope $p(1-p)$ |
|---:|---:|
| 0.01 | 0.0099 |
| 0.10 | 0.0900 |
| 0.50 | 0.2500 |
| 0.90 | 0.0900 |
| 0.99 | 0.0099 |

This explains the shape:

- **Near 0.5:** a small change in score produces a relatively larger change in probability.
- **Near 0 or 1:** the same change in score produces a smaller change in probability.

The derivative is positive for every finite score, so the curve always rises as the score increases.

### Connection to our Telco model

The model first calculates:

$$
z = b + w_1x_1 + \cdots + w_mx_m
$$

The sigmoid then converts that score into a churn probability.

The same increase in score does not always produce the same increase in probability:

- Moving from $z=0$ to $z=1$ raises probability from about **50% to 73.1%**.
- Moving from $z=4$ to $z=5$ raises probability from about **98.2% to 99.3%**.

That is why a logistic regression weight is not a fixed percentage-point change in churn probability.