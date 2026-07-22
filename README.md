# 💳 Credit Card Approval Prediction

An AI-powered Credit Card Approval Prediction System built using **Python, Flask, Scikit-learn, and XGBoost**. The application predicts whether a credit card application should be **Approved** or **Rejected** based on applicant information such as income, employment status, education, marital status, family status, housing type, and credit history.

The project automates the credit approval process, reduces manual effort, and enables financial institutions to make fast, accurate, and data-driven decisions through a simple web interface.

---

# 🌐 Live Demo

🚀 **Application:**
https://credit-card-approval-prediction-kpw8.onrender.com

# 🎥 Demo Video

https://drive.google.com/file/d/1Qk3qG3yrosbwSEixqFXPavIxflBmvkVM/view?usp=sharing

---

# 📂 Repository Structure

```text
Credit-Card-Approval-Prediction/
│
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
├── pyproject.toml
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/MOHANREDDY123456789/Credit-Card-Approval-Prediction.git

cd Credit-Card-Approval-Prediction
```

---

## 2. Create a Virtual Environment (Optional)

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Train the Machine Learning Model

Open and run all cells in:

```text
Training/Credit_Card_Approval_Model_Training.ipynb
```

This trains all four models on `Dataset/application_record.csv` and `Dataset/credit_record.csv`, compares them, and saves the best-performing model into `Flask/model/` as `model.pkl`, `model_columns.pkl`, `scaler.pkl`, and `encoders.pkl`.

---

## 5. Run the Flask Application

```bash
cd Flask
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

# ✨ Features

- Credit Card Approval Prediction
- Data Preprocessing
- Feature Engineering
- Multiple Machine Learning Algorithms
- Automatic Best Model Selection
- Flask Web Application
- Responsive User Interface
- Real-Time Prediction
- Pickle Model Serialization
- Live Deployment on Render

---

# 🤖 Machine Learning Models

The following classification models were trained and evaluated:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

The best-performing model is automatically selected and saved for deployment.

---

# 📊 Project Workflow

1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Data Preprocessing
5. Model Training
6. Model Evaluation
7. Best Model Selection
8. Flask Deployment
9. Prediction

---

# 💳 Use Cases

- Credit Card Approval Prediction
- Risk Assessment
- Automated Customer Screening
- Banking Decision Support
- Financial Analytics

---

# 🛠️ Technologies Used

## Programming Language

- Python

## Machine Learning

- Scikit-learn
- XGBoost
- Pandas
- NumPy

## Data Visualization

- Matplotlib
- Seaborn

## Web Development

- Flask
- HTML
- CSS
- JavaScript

## Deployment

- Render

---

# 📈 Models Compared

| Model | Accuracy | F1-score |
|--------|----------|---------|
| Logistic Regression | 90.2% | 0.944 |
| Decision Tree | 90.9% | 0.949 |
| Random Forest | **93.9%** | **0.966** |
| XGBoost | 92.1% | 0.956 |

---

# 🎯 Future Enhancements

- User Authentication
- REST API
- Explainable AI (SHAP/LIME)
- Dashboard & Analytics
- Database Integration
- Docker Deployment
- CI/CD Pipeline

---

# 👥 Team

| Team Member | Role |
|-------------|------|
| Tupakula Rishmitha Sri | Team Lead |
| Tejomai Kondapureddy | Member |
| Korrapolu Lahari | Member |
| Saragada Tirupathi Venkata Mohan Reddy | Member |
| Vijay Kanth Kalvakuntla | Member |

Developed as part of the **SmartBridge × SkillWallet Virtual Internship Program**.

---

# 👨‍💻 Skills Demonstrated

- Machine Learning
- Data Preprocessing
- Feature Engineering
- Classification Algorithms
- XGBoost
- Flask Development
- Model Deployment
- Python
- Scikit-learn
- Pandas
- NumPy
- Git & GitHub

---

# 📄 License

This project is developed for educational and academic purposes.
