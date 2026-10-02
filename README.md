# 🤖 Machine Learning Zoomcamp — Fall 2026

All my codelabs, homework, notes, and projects from the [Machine Learning Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp), a free four-month course on ML engineering organized by [Alexey Grigorev](https://github.com/alexeygrigorev) and [DataTalks.Club](https://datatalks.club/).

This repo tracks my progress through the **2026 live cohort** (September 2026 – January 2027), from framing an ML problem all the way to serving a model in production.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikitlearn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-189FDD?style=flat)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat&logo=tensorflow&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)
![AWS Lambda](https://img.shields.io/badge/AWS%20Lambda-FF9900?style=flat&logo=awslambda&logoColor=white)

---

## 📚 About the Course

| | |
|---|---|
| **Organizer** | Alexey Grigorev · DataTalks.Club |
| **Cohort** | Fall 2026 (started September 14, 2026) |
| **Format** | Pre-recorded lectures, weekly homework, peer-reviewed projects |
| **Course platform** | [courses.datatalks.club/ml-zoomcamp-2026](https://courses.datatalks.club/ml-zoomcamp-2026/) |
| **Official materials** | [DataTalksClub/machine-learning-zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp) |

The course covers the full ML engineering lifecycle: frame the problem, prepare the data, train and evaluate models, expose them through an API, containerize them, and deploy them to the cloud.

---

## 🗺️ Progress Tracker

**Legend:** ⬜ Not started · 🟡 In progress · ✅ Done

### Modules

| # | Module | Folder | Codelabs | Homework |
|---|---|---|:---:|:---:|
| 01 | Introduction to Machine Learning | [`01-intro`](./01-intro) | ⬜ | ⬜ |
| 02 | Machine Learning for Regression | [`02-regression`](./02-regression) | ⬜ | ⬜ |
| 03 | Machine Learning for Classification | [`03-classification`](./03-classification) | ⬜ | ⬜ |
| 04 | Evaluation Metrics for Classification | [`04-evaluation`](./04-evaluation) | ⬜ | ⬜ |
| 05 | Deploying Machine Learning Models | [`05-deployment`](./05-deployment) | ⬜ | ⬜ |
| 06 | Decision Trees & Ensemble Learning | [`06-trees`](./06-trees) | ⬜ | ⬜ |
| 08 | Neural Networks & Deep Learning | [`08-deep-learning`](./08-deep-learning) | ⬜ | ⬜ |
| 09 | Serverless Deep Learning | [`09-serverless`](./09-serverless) | ⬜ | ⬜ |
| 10 | Kubernetes & TensorFlow Serving | [`10-kubernetes`](./10-kubernetes) | ⬜ | ⬜ |

> Module numbering follows the official course repo. Week 7 is reserved for the midterm project, so there is no `07-` folder.

### Projects

| Project | Folder | Description | Status |
|---|---|---|:---:|
| Midterm Project | [`projects/midterm`](./projects/midterm) | _One-line summary of the problem and model_ | ⬜ |
| Capstone Project 1 | [`projects/capstone-1`](./projects/capstone-1) | _One-line summary of the problem and model_ | ⬜ |
| Capstone Project 2 _(optional)_ | [`projects/capstone-2`](./projects/capstone-2) | _One-line summary of the problem and model_ | ⬜ |

Each project folder has its own README covering the problem statement, dataset, EDA, model selection, and instructions for running the service locally and in the cloud.

---

## 🧠 What Each Module Covers

**01 · Intro to ML** — ML vs. rule-based systems, supervised learning, the CRISP-DM framework, model selection, and environment setup.

**02 · Regression** — Car-price prediction: EDA, linear regression from scratch and with scikit-learn, feature engineering, regularization, and validation.

**03 · Classification** — Customer-churn prediction with logistic regression, categorical encoding, feature importance, and model interpretation.

**04 · Evaluation Metrics** — Accuracy, precision, recall, F1, confusion matrices, ROC/AUC, cross-validation, and handling class imbalance.

**05 · Deployment** — Model serialization, serving predictions with FastAPI, containerizing with Docker, and deploying to the cloud.

**06 · Trees & Ensembles** — Decision trees, random forests, gradient boosting with XGBoost, hyperparameter tuning, and feature importance.

**08 · Deep Learning** — Neural network fundamentals, CNNs, and transfer learning for image classification with PyTorch and TensorFlow/Keras.

**09 · Serverless** — Deploying scikit-learn and deep learning models on AWS Lambda behind API Gateway.

**10 · Kubernetes** — Core Kubernetes concepts, TensorFlow Serving, and deploying and scaling model-serving workloads.

---

## 📁 Repository Structure

```
machine-learning-zoomcamp/
├── 01-intro/
│   ├── codelabs/        # Notebooks following along with the lectures
│   ├── homework/        # Homework solutions
│   └── notes.md         # My notes and key takeaways
├── 02-regression/
├── 03-classification/
├── 04-evaluation/
├── 05-deployment/
├── 06-trees/
├── 08-deep-learning/
├── 09-serverless/
├── 10-kubernetes/
├── projects/
│   ├── midterm/
│   ├── capstone-1/
│   └── capstone-2/
├── pyproject.toml
└── README.md
```

---

## ⚙️ Getting Started

```bash
# Clone the repo
git clone https://github.com/<your-username>/machine-learning-zoomcamp.git
cd machine-learning-zoomcamp

# Set up the environment with uv
uv sync
uv run jupyter lab

# ...or with plain pip
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

Deployment modules and projects include their own `Dockerfile` and run instructions in their folder README.

---

## 📝 Notes on Homework

Homework solutions are pushed **after** each cohort deadline, so this repo doesn't become an answer key while submissions are still open.

---

## 📣 Learning in Public

I'm sharing progress and takeaways along the way using **#mlzoomcamp**.

- _Link to post 1_
- _Link to post 2_

---

## 🔗 Useful Links

- [Official course repository](https://github.com/DataTalksClub/machine-learning-zoomcamp)
- [Course platform (2026 cohort)](https://courses.datatalks.club/ml-zoomcamp-2026/)
- [Lecture playlist on YouTube](https://www.youtube.com/playlist?list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR)
- [Course FAQ](https://datatalks.club/faq/machine-learning-zoomcamp.html)
- [DataTalks.Club Slack](https://datatalks.club/slack.html) — channel `#course-ml-zoomcamp`

---

## 🙏 Acknowledgements

Huge thanks to **Alexey Grigorev** and the **DataTalks.Club** team for making this course free and open. Course materials, datasets, and lecture content belong to DataTalks.Club; the code and notes in this repository are my own work.

---

## 👤 Author

**Pranav**
[GitHub](https://github.com/<your-username>) · [LinkedIn](https://www.linkedin.com/in/<your-handle>)
