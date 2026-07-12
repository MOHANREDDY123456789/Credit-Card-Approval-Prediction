# 💳 Credit Card Approval Prediction

An AI-powered Credit Card Approval Prediction System that automates credit card eligibility decisions using machine learning. The model is trained on historical applicant information such as income, employment status, education, marital status, and credit history to predict whether a credit card application should be **Approved** or **Rejected**.

The system minimizes manual verification, reduces processing time, and helps financial institutions make fast, consistent, and data-driven decisions through an intuitive Flask web application.

## Machine Learning Models

The following classification algorithms are trained and evaluated:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- XGBoost Classifier

The best-performing model (selected automatically by F1-score) is serialized and deployed using Flask. An optional IBM Watson Machine Learning deployment is also supported for cloud-based inference.

---

# 📂 Repository Structure

```text
Credit_Card_Approval_Prediction/
├── Dataset/
│   ├── application_record.csv
│   └── credit_record.csv
│
├── Flask/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   └── model/
│       ├── model.pkl
│       ├── model_columns.pkl
│       ├── scaler.pkl
│       └── encoders.pkl
│
├── Project_Documentation/
│   ├── 1.Brainstorming_&_Ideation/
│   ├── 2.Requirement_Analysis/
│   ├── 3.Project_Design_Phase/
│   ├── 4.Project_Planning_Phase/
│   ├── 5.Project_Development_Phase/
│   ├── 6.Project_Testing/
│   ├── 7.Project_Documentation/
│   └── 8.Project_Demonstration/
│
├── Training/
│   └── Credit_Card_Approval_Model_Training.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/Credit_Card_Approval_Prediction.git
cd Credit_Card_Approval_Prediction
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Dataset

The **Dataset/** folder already includes:

- `application_record.csv`
- `credit_record.csv`

These contain applicant demographic information and historical credit records used for model training. To use the real-world Kaggle "Credit Card Approval Prediction" dataset instead, replace both files with the same filenames and column structure — no code changes needed.

---

## 4. Train the Model

Open and run all cells in:

```text
Training/Credit_Card_Approval_Model_Training.ipynb
```

The notebook performs:

- Data Cleaning
- Exploratory Data Analysis (univariate, multivariate, descriptive)
- Feature Engineering
- Model Training (Logistic Regression, Decision Tree, Random Forest, XGBoost)
- Model Evaluation & Comparison

After training, the following files are generated inside `Flask/model/`:

```
model.pkl
model_columns.pkl
scaler.pkl
encoders.pkl
```

---

## 5. Run the Flask Application

```bash
cd Flask
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

Fill in the applicant details and click **Predict** to get an instant Approved / Rejected result with a confidence score.

---

# ✨ Features

- Credit Card Approval Prediction
- Data Preprocessing & Feature Engineering (EMI Paid Off, EMI Pastdues, Number of Loans)
- Multiple ML Model Comparison
- Random Forest / XGBoost-based Prediction Engine
- Responsive Flask Web Interface
- Fast Real-Time Predictions
- Model Serialization using Pickle
- Optional IBM Watson ML Deployment

---

# 📊 Project Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Model Selection
8. Flask Deployment
9. Prediction

---

# 💳 Use Cases

### Credit Card Eligibility Assessment
Predict whether a customer qualifies for a credit card based on financial and demographic information.

### Risk Assessment
Identify applicants with higher default risk before approval.

### Automated Customer Screening
Reduce manual verification effort by instantly classifying applications.

### Financial Decision Support
Assist banks and financial institutions in making faster, more accurate approval decisions.

---

# 🤖 Machine Learning Pipeline

- Data Cleaning
- Missing Value Handling
- Feature Encoding
- Feature Scaling
- Model Training
- Model Evaluation
- Performance Comparison
- Model Deployment

---

# ☁️ Optional IBM Watson Machine Learning Deployment

The trained model can be deployed to IBM Watson Machine Learning using the `ibm-watson-machine-learning` SDK. Once deployed, the Flask application can consume predictions through REST APIs instead of loading the local model, enabling scalable cloud-based inference.

---

# 🛠️ Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- XGBoost
- NumPy
- Pandas

### Data Visualization
- Matplotlib
- Seaborn

### Web Framework
- Flask
- HTML
- CSS

### Deployment
- IBM Watson Machine Learning (Optional)

---

# 📈 Models Compared

| Model | Accuracy | F1-score |
|--------|---------|---------|
| Logistic Regression | 0.902 | 0.944 |
| Decision Tree | 0.909 | 0.949 |
| **Random Forest (deployed)** | **0.939** | **0.966** |
| XGBoost | 0.921 | 0.956 |

---

# 🎯 Future Enhancements

- Explainable AI (SHAP/LIME) for approval reasoning
- REST API Integration
- User Authentication
- Database Support (see `Project_Documentation/3.Project_Design_Phase/` for the ER diagram)
- Cloud Deployment (AWS/Azure/IBM Cloud)

---

# 👥 Team

| Team Member | Role |
|---|---|
| Tupakula Rishmitha Sri | Team Lead |
| Tejomai Kondapureddy | Member |
| Korrapolu Lahari | Member |
| Saragada Tirupathi Venkata Mohan Reddy | Member |
| Vijay Kanth Kalvakuntla | Member |

Developed as part of the SmartBridge / SkillWallet Virtual Internship Program.

---

# 👨‍💻 Skills Demonstrated

- Machine Learning
- Data Analysis
- Data Preprocessing
- Feature Engineering
- Classification Algorithms
- XGBoost
- Flask Development
- Model Deployment
- Python Programming
- Scikit-learn
- NumPy
- Pandas
- Matplotlib
- Git & GitHub

---

## 📄 License

This project is developed for educational and academic purposes.
