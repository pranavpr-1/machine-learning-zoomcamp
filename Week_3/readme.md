# Codelab Notes: Feature Importance, Churn Rates, Differences, and Risk Ratios

> These notes use a customer-churn example. Assume `df_full_train` is the training table and `churn` is encoded as `1` for a customer who left and `0` for a customer who stayed, with no missing target values.
>
> *The worked numbers below are illustrative, not results from your dataset.*

---

## 1. What are we checking when we explore feature importance?

A **feature** is an input column, such as `partner`, `contract`, or `tenure`. The **target** is the outcome we want to predict: `churn`.

For a categorical feature, we ask:

> **Does the observed churn rate change when we look at different values of this feature?**

For example, do customers with `partner = 'yes'` and `partner = 'no'` have different churn rates?

Differences across sufficiently large groups suggest that the feature may help predict churn.

> **Note:** This is an **exploratory check** of each feature's relationship with churn.
> - It does **not** yet measure a trained model's feature importance.
> - It does **not** establish a cause of churn.
> - A feature with similar group rates can still become useful when combined with other features.

---

## 2. Global churn rate: the overall baseline

Here, **global** means all customers in `df_full_train`.

$$
\text{global churn rate} = \frac{\text{customers who churned in the training table}}{\text{all customers in the training table}}
$$

```python
global_churn = df_full_train['churn'].mean()
```

**Why does `.mean()` give a churn rate?** Every churned customer contributes `1` and every other customer contributes `0`. Adding those values counts the churned customers, and the mean divides that count by the number of customers.

**Example:** `[1, 0, 0, 1, 0]` has a mean of 2 / 5 = 0.40, so its churn rate is **40%**.

---

## 3. Group churn rate: the baseline for a subset

A **group** is a subset sharing one feature value, such as customers with `partner = 'no'`.

$$
\text{group churn rate} = \frac{\text{customers who churned within the group}}{\text{all customers within the group}}
$$

```python
no_partner = df_full_train[df_full_train['partner'] == 'no']
group_churn = no_partner['churn'].mean()
```

> **Note:** The denominator is the size of *this group*, rather than the size of the entire training table.

---

## 4. One worked example

Imagine a training table containing these two groups:

| Customers | Total customers | Churned | Churn rate |
|---|---:|---:|---:|
| All customers | 1,000 | 250 | 250 / 1,000 = **25%** |
| `partner = 'no'` | 400 | 160 | 160 / 400 = **40%** |
| `partner = 'yes'` | 600 | 90 | 90 / 600 = **15%** |

The two groups make up the overall table. The global rate is **weighted by group size**:

$$
\frac{400 \times 0.40 + 600 \times 0.15}{1000} = 0.25
$$

> **Watch out:** Simply averaging the two group rates would give 27.5%, which is incorrect here because the group sizes differ.

---

## 5. Difference: how far above or below the global rate?

Define the difference as **group minus global**:

$$
\text{difference} = \text{group churn rate} - \text{global churn rate}
$$

```python
diff = group_churn - global_churn
```

**Customers with no partner:**

$$
0.40 - 0.25 = +0.15
$$

This group's churn rate is **15 percentage points above** the global rate.

**Customers with a partner:**

$$
0.15 - 0.25 = -0.10
$$

This group's churn rate is **10 percentage points below** the global rate.

| Difference | Interpretation |
|---|---|
| Positive | Group churn rate is above the global rate |
| Zero | Group churn rate equals the global rate |
| Negative | Group churn rate is below the global rate |

> **Tip:** Check the subtraction order in your code: `global - group` reverses these signs. Multiplying the decimal difference by 100 expresses it in percentage points.

---

## 6. Risk ratio: how many times the global rate?

In these notes, the **risk ratio** compares a group's observed churn rate with the global rate:

$$
\text{risk ratio} = \frac{\text{group churn rate}}{\text{global churn rate}}
$$

```python
risk_ratio = group_churn / global_churn
```

**Customers with no partner:**

$$
0.40 / 0.25 = 1.60
$$

Their observed churn rate is **1.6 times** the global rate, or **60% higher** relative to the global rate: (1.60 − 1) × 100 = 60%.

**Customers with a partner:**

$$
0.15 / 0.25 = 0.60
$$

Their observed churn rate is **0.6 times** the global rate, or **40% lower** relative to the global rate.

| Risk ratio | Interpretation |
|---|---|
| Greater than 1 | Group churn rate is above the global rate |
| Equal to 1 | Group churn rate equals the global rate |
| Less than 1 | Group churn rate is below the global rate |

> **Note:**
> - The ratio has no percentage-point unit.
> - Keep its denominator explicit: here the reference is the overall training table, which includes each group.
> - If the global churn rate is zero, this ratio is undefined.

---

## 7. Difference versus risk ratio

| Group | Group churn rate | Difference from 25% global rate | Risk ratio |
|---|---:|---:|---:|
| `partner = 'no'` | 40% | +15 percentage points | 1.60 |
| `partner = 'yes'` | 15% | −10 percentage points | 0.60 |

The same change from 25% to 40% can be described as **15 percentage points higher** or **60% higher relative to the baseline**. Both are correct; they answer different questions.

---

## 8. Calculate all groups of one feature with pandas

```python
# Overall churn rate in the training table.
global_churn = df_full_train['churn'].mean()

# Split customers by partner status and summarize churn in each group.
df_group = (
    df_full_train
    .groupby('partner')['churn']
    .agg(['mean', 'count'])
)

# Add the absolute and relative comparisons with the overall rate.
df_group['diff'] = df_group['mean'] - global_churn
df_group['risk'] = df_group['mean'] / global_churn

df_group
```

| Code | What it does |
|---|---|
| `.groupby('partner')` | Splits rows into groups sharing the same `partner` value |
| `['churn']` | Selects the target values within each group |
| `.agg(['mean', 'count'])` | Calculates each group's churn rate and number of nonmissing churn values |
| `df_group['mean']` | Contains one churn rate for each group |
| `df_group['diff']` | Stores group rate minus global rate |
| `df_group['risk']` | Stores group rate divided by global rate |

The subtraction and division apply to every value in the `mean` column, so you do not need to write a separate calculation for each group.

**Reading the output:** In Jupyter, the final `df_group` line displays the table.
- The `mean` and `diff` columns contain decimals: `0.40` in `mean` means 40% churn, and `0.15` in `diff` means +15 percentage points.
- The `risk` column contains ratios: `1.60` means 1.6 times the global rate.

Replacing `'partner'` with `'contract'` produces the same analysis for contract categories.

---

## 9. How to use these results for feature exploration

- **Group rates close to the global rate** suggest little association with churn when looking at that feature alone.
- **Clear differences across well-represented groups** suggest a feature worth investigating for prediction.
- **Always inspect `count`:** an extreme rate based on a handful of customers can be unstable.
- **Association ≠ causation:** these comparisons describe observed associations. They do not prove that changing the feature would change a customer's churn outcome.
- **Train vs. held-out:** calculate these summaries on the training data and evaluate predictive usefulness on held-out data.

> **Memory aid**
> - **global** = overall rate
> - **group** = subset rate
> - **difference** = how many percentage points
> - **risk ratio** = how many times the baseline

---

### Reference

The pandas grouping and aggregation syntax follows the official [pandas GroupBy guide](https://pandas.pydata.org/docs/user_guide/groupby.html), including the section on applying multiple functions at once. All worked churn numbers in these notes are hypothetical examples.