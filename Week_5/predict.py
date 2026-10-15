"""
Telco Customer Churn - Prediction Script
========================================

Loads the model saved by train.py and predicts churn probability for a customer.

Usage:
    python3 predict.py                      # scores the built-in sample customer
    python3 predict.py customer.json        # scores a customer (or list of customers) from a JSON file
"""

import json
import pickle
import sys

# Must match the file name that train.py saved
MODEL_FILE = "model_C=1.0.bin"

# Probability at or above this value is flagged as "will likely churn"
THRESHOLD = 0.5

# Example customer, used when no JSON file is given
SAMPLE_CUSTOMER = {
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


def load_model(model_file):
    """Load the (DictVectorizer, LogisticRegression) tuple saved by train.py."""
    with open(model_file, "rb") as f_in:
        dv, model = pickle.load(f_in)
    return dv, model


def clean_customer(customer):
    """
    Apply the same text cleaning used in training: lowercase, spaces -> underscores.
    This lets you pass raw values like "Month-to-month" or "Bank transfer (automatic)"
    and still match the categories the model learned.
    """
    cleaned = {}
    for key, value in customer.items():
        key = key.lower().replace(" ", "_")
        if isinstance(value, str):
            value = value.lower().replace(" ", "_")
        cleaned[key] = value
    return cleaned


def predict_churn(customer, dv, model):
    """Return the probability (0 to 1) that this customer churns."""
    customer = clean_customer(customer)

    # transform (not fit_transform): reuse the encoding learned during training
    X = dv.transform([customer])

    # predict_proba returns [P(stay), P(churn)]; we want the churn column
    return model.predict_proba(X)[0, 1]


def print_result(customer, churn_prob):
    """Print one customer's result in a readable format."""
    customer_id = customer.get("customerid", customer.get("customerID", "unknown"))
    verdict = "WILL LIKELY CHURN" if churn_prob >= THRESHOLD else "likely to stay"

    print("-" * 50)
    print(f"  Customer:          {customer_id}")
    print(f"  Churn probability: {churn_prob:.1%}")
    print(f"  Prediction:        {verdict}")


def main():
    print("\nTelco Customer Churn - Prediction")

    # Load the saved model from disk
    try:
        dv, model = load_model(MODEL_FILE)
    except FileNotFoundError:
        print(f"\n  Could not find '{MODEL_FILE}'.")
        print("  Run train.py first, and run this script from the same folder.\n")
        sys.exit(1)
    print(f"  -> Loaded model from {MODEL_FILE}")

    # Get customers: from a JSON file if given, otherwise use the sample
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            data = json.load(f)
        customers = data if isinstance(data, list) else [data]
        print(f"  -> Loaded {len(customers)} customer(s) from {sys.argv[1]}")
    else:
        customers = [SAMPLE_CUSTOMER]
        print("  -> No file given, using the built-in sample customer")

    # Score each customer and print the result
    print()
    for customer in customers:
        churn_prob = predict_churn(customer, dv, model)
        print_result(customer, churn_prob)
    print("-" * 50 + "\n")


if __name__ == "__main__":
    main()