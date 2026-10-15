"""
Telco Customer Churn - Train, Validate, Save, and Test a Model
==============================================================

What this script does, end to end:
    1. Downloads the Telco churn dataset from Kaggle
    2. Cleans and prepares the data
    3. Splits it into a full-train set (80%) and a test set (20%)
    4. Cross-validates a logistic regression model (K-Fold) to check stability
    5. Trains the final model on the full-train set and evaluates on the test set
    6. Saves the trained model (DictVectorizer + LogisticRegression) to a .bin file
    7. Reloads the saved file and runs a sample prediction to prove it works

Usage:
    python churn_train.py
"""

import pickle
import time

import numpy as np
import pandas as pd
import kagglehub

from sklearn.model_selection import train_test_split, KFold
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score


# ----------------------------------------------------------------------------
# Parameters
# ----------------------------------------------------------------------------
C = 1.0                 # Regularization strength for logistic regression (smaller = stronger)
N_SPLITS = 5            # Number of folds for cross-validation
RANDOM_STATE = 1        # Seed so results are reproducible
TEST_SIZE = 0.2         # Fraction of data held out for the final test
OUTPUT_FILE = f"model_C={C}.bin"   # Where the trained model gets saved

# Feature lists: which columns the model uses as input
NUMERICAL = ["tenure", "monthlycharges", "totalcharges"]

CATEGORICAL = [
    "gender",
    "seniorcitizen",
    "partner",
    "dependents",
    "phoneservice",
    "multiplelines",
    "internetservice",
    "onlinesecurity",
    "onlinebackup",
    "deviceprotection",
    "techsupport",
    "streamingtv",
    "streamingmovies",
    "contract",
    "paperlessbilling",
    "paymentmethod",
]


# ----------------------------------------------------------------------------
# Small helpers for readable terminal output
# ----------------------------------------------------------------------------
def banner(title):
    """Print a clear section header so progress is easy to follow."""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def info(message):
    """Print an indented status line."""
    print(f"  -> {message}")


# ----------------------------------------------------------------------------
# Step 1: Load the data
# ----------------------------------------------------------------------------
def load_data():
    """Download the dataset from Kaggle (cached after the first run) and read it."""
    banner("STEP 1/7: Loading data")

    # kagglehub downloads the dataset and returns the local folder path
    path = kagglehub.dataset_download("blastchar/telco-customer-churn")
    info(f"Dataset location: {path}")

    df = pd.read_csv(f"{path}/WA_Fn-UseC_-Telco-Customer-Churn.csv")
    info(f"Loaded {len(df):,} rows and {df.shape[1]} columns")
    return df


# ----------------------------------------------------------------------------
# Step 2: Clean the data
# ----------------------------------------------------------------------------
def clean_data(df):
    """Standardize names/values and fix data types so the model gets consistent input."""
    banner("STEP 2/7: Cleaning data")

    # Column names -> lowercase with underscores (e.g. "Total Charges" -> "total_charges")
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    info("Standardized column names")

    # Text values -> lowercase with underscores (e.g. "Bank transfer" -> "bank_transfer")
    # is_string_dtype works for both older pandas ('object') and newer pandas ('str')
    text_columns = [c for c in df.columns if pd.api.types.is_string_dtype(df[c])]
    for col in text_columns:
        df[col] = df[col].str.lower().str.replace(" ", "_")
    info(f"Standardized text values in {len(text_columns)} text columns")

    # totalcharges is stored as text because some rows contain blanks.
    # errors='coerce' turns unparseable values into NaN; we then fill them with 0
    # (these are brand-new customers with tenure 0, so 0 total charges makes sense).
    df["totalcharges"] = pd.to_numeric(df["totalcharges"], errors="coerce")
    n_missing = int(df["totalcharges"].isna().sum())
    df["totalcharges"] = df["totalcharges"].fillna(0)
    info(f"Converted totalcharges to numeric ({n_missing} blank values filled with 0)")

    # Target variable: convert 'yes'/'no' to 1/0
    df["churn"] = (df["churn"].astype("string").str.strip().str.lower() == "yes").astype(int)
    churn_rate = df["churn"].mean()
    info(f"Converted churn to 0/1 labels (overall churn rate: {churn_rate:.1%})")

    return df


# ----------------------------------------------------------------------------
# Core model functions
# ----------------------------------------------------------------------------
def train(df_train, y_train, C=1.0):
    """
    Fit a DictVectorizer + LogisticRegression on the given data.
    Returns both, because both are needed later to make predictions.
    """
    # Turn each row into a dictionary: {'gender': 'female', 'tenure': 41, ...}
    dicts = df_train[CATEGORICAL + NUMERICAL].to_dict(orient="records")

    # DictVectorizer one-hot encodes text columns and passes numbers through unchanged
    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)

    # Logistic regression with the liblinear solver, which handles our unscaled
    # features (tenure vs. totalcharges) without convergence warnings
    model = LogisticRegression(C=C, solver="liblinear")
    model.fit(X_train, y_train)

    return dv, model


def predict(df, dv, model):
    """Return the predicted probability of churn (a value between 0 and 1) for each row."""
    dicts = df[CATEGORICAL + NUMERICAL].to_dict(orient="records")

    # IMPORTANT: use transform (not fit_transform) so encoding matches training
    X = dv.transform(dicts)

    # predict_proba returns [P(no churn), P(churn)]; we want the second column
    return model.predict_proba(X)[:, 1]


# ----------------------------------------------------------------------------
# Step 3: Split the data
# ----------------------------------------------------------------------------
def split_data(df):
    """Hold out a test set that the model never sees until the very end."""
    banner("STEP 3/7: Splitting data")

    df_full_train, df_test = train_test_split(df, test_size=TEST_SIZE, random_state=RANDOM_STATE)

    info(f"Full-train set: {len(df_full_train):,} rows (churn rate {df_full_train['churn'].mean():.1%})")
    info(f"Test set:       {len(df_test):,} rows (churn rate {df_test['churn'].mean():.1%})")
    return df_full_train, df_test


# ----------------------------------------------------------------------------
# Step 4: Cross-validation
# ----------------------------------------------------------------------------
def cross_validate(df_full_train):
    """
    K-Fold cross-validation: train on K-1 folds, validate on the remaining fold,
    repeat K times. A small standard deviation across folds means a stable model.
    """
    banner(f"STEP 4/7: {N_SPLITS}-Fold cross-validation (C={C})")

    kfold = KFold(n_splits=N_SPLITS, shuffle=True, random_state=RANDOM_STATE)
    scores = []

    for fold, (train_idx, val_idx) in enumerate(kfold.split(df_full_train), start=1):
        # Split this fold's rows into training and validation portions
        df_train = df_full_train.iloc[train_idx]
        df_val = df_full_train.iloc[val_idx]

        y_train = df_train["churn"].values
        y_val = df_val["churn"].values

        # Train on the training portion, score on the validation portion
        dv, model = train(df_train, y_train, C=C)
        y_pred = predict(df_val, dv, model)

        # AUC: 0.5 = random guessing, 1.0 = perfect ranking
        auc = roc_auc_score(y_val, y_pred)
        scores.append(auc)
        info(f"Fold {fold}/{N_SPLITS}: AUC = {auc:.3f}")

    print(f"\n  Cross-validation result: AUC = {np.mean(scores):.3f} +- {np.std(scores):.3f}")


# ----------------------------------------------------------------------------
# Step 5: Train the final model and evaluate on the test set
# ----------------------------------------------------------------------------
def train_final_model(df_full_train, df_test):
    """Train on all training data, then measure performance on the untouched test set."""
    banner("STEP 5/7: Training final model & testing")

    dv, model = train(df_full_train, df_full_train["churn"].values, C=C)
    info(f"Trained on {len(df_full_train):,} rows")

    y_pred = predict(df_test, dv, model)
    y_test = df_test["churn"].values
    auc = roc_auc_score(y_test, y_pred)
    info(f"Test set AUC: {auc:.3f}")

    return dv, model


# ----------------------------------------------------------------------------
# Step 6: Save the model
# ----------------------------------------------------------------------------
def save_model(dv, model, output_file):
    """
    Pickle the vectorizer and model together. Both are required at prediction
    time, so we store them as a single tuple. 'with' closes the file automatically.
    """
    banner("STEP 6/7: Saving model")

    with open(output_file, "wb") as f_out:
        pickle.dump((dv, model), f_out)

    info(f"Model saved to: {output_file}")


# ----------------------------------------------------------------------------
# Step 7: Reload the model and run a sample prediction
# ----------------------------------------------------------------------------
def load_model(model_file):
    """Load a saved (DictVectorizer, model) tuple from disk."""
    with open(model_file, "rb") as f_in:
        dv, model = pickle.load(f_in)
    return dv, model


def sanity_check(model_file):
    """Reload the saved model and score one example customer, as a deployment smoke test."""
    banner("STEP 7/7: Sanity check on the saved model")

    dv, model = load_model(model_file)
    info("Reloaded model from disk")

    # An example customer, using the same cleaned format as the training data.
    # (customerid is not a model feature, so it's simply ignored.)
    customer = {
        "customerid": "8879-zkjof",
        "gender": "female",
        "seniorcitizen": 0,
        "partner": "no",
        "dependents": "no",
        "tenure": 41,
        "phoneservice": "yes",
        "multiplelines": "no",
        "internetservice": "dsl",
        "onlinesecurity": "yes",
        "onlinebackup": "no",
        "deviceprotection": "yes",
        "techsupport": "yes",
        "streamingtv": "yes",
        "streamingmovies": "yes",
        "contract": "one_year",
        "paperlessbilling": "yes",
        "paymentmethod": "bank_transfer_(automatic)",
        "monthlycharges": 79.85,
        "totalcharges": 3320.75,
    }

    # Single-customer prediction: wrap the dict in a list, take the churn probability
    X = dv.transform([customer])
    churn_prob = model.predict_proba(X)[0, 1]

    info(f"Sample customer: {customer['customerid']}")
    info(f"Predicted churn probability: {churn_prob:.1%}")
    info("Prediction: " + ("WILL LIKELY CHURN" if churn_prob >= 0.5 else "likely to stay"))


# ----------------------------------------------------------------------------
# Main: run all steps in order
# ----------------------------------------------------------------------------
def main():
    start = time.time()
    print("\nTelco Customer Churn - Training Pipeline")

    df = load_data()
    df = clean_data(df)
    df_full_train, df_test = split_data(df)
    cross_validate(df_full_train)
    dv, model = train_final_model(df_full_train, df_test)
    save_model(dv, model, OUTPUT_FILE)
    sanity_check(OUTPUT_FILE)

    banner("DONE")
    info(f"Pipeline finished in {time.time() - start:.1f} seconds")
    print()


# Only run when executed directly (not when imported by another script)
if __name__ == "__main__":
    main()