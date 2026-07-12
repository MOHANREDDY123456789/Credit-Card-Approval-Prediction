import pickle

import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)
with open("model/model_columns.pkl", "rb") as f:
    feature_columns = pickle.load(f)
with open("model/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)
with open("model/encoders.pkl", "rb") as f:
    encoders = pickle.load(f)

model_name = "Random Forest (best of 4 models)"


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", prediction=None, model_name=model_name)


@app.route("/predict", methods=["POST"])
def predict():
    form = request.form

    def safe_encode(col, value):
        le = encoders[col]
        if value not in le.classes_:
            value = le.classes_[0]
        return le.transform([value])[0]

    gender_enc = safe_encode("CODE_GENDER", form.get("gender"))
    car_enc = safe_encode("FLAG_OWN_CAR", form.get("own_car"))
    realty_enc = safe_encode("FLAG_OWN_REALTY", form.get("own_realty"))
    income_type_enc = safe_encode("NAME_INCOME_TYPE", form.get("income_type"))
    education_enc = safe_encode("NAME_EDUCATION_TYPE", form.get("education"))
    family_status_enc = safe_encode("NAME_FAMILY_STATUS", form.get("family_status"))
    housing_enc = safe_encode("NAME_HOUSING_TYPE", form.get("housing_type"))

    annual_income = float(form.get("annual_income", 0))
    days_birth = abs(float(form.get("days_birth", 0)))
    days_employed = abs(float(form.get("days_employed", 0)))
    family_members = int(form.get("family_members", 1))
    emi_paid_off = int(form.get("emi_paid_off", 0))
    emi_pastdues = int(form.get("emi_pastdues", 0))
    number_of_loans = int(form.get("number_of_loans", 0))
    cnt_children = max(0, family_members - 2)

    row = [
        gender_enc, car_enc, realty_enc, cnt_children, annual_income,
        income_type_enc, education_enc, family_status_enc, housing_enc,
        days_birth, days_employed, family_members,
        emi_paid_off, emi_pastdues, number_of_loans,
    ]

    X_scaled = scaler.transform([row])
    pred = model.predict(X_scaled)[0]
    prob = model.predict_proba(X_scaled)[0][1]

    result = "Approved" if pred == 1 else "Rejected"
    confidence = round((prob if pred == 1 else 1 - prob) * 100, 2)

    return render_template(
        "index.html",
        prediction=result,
        confidence=confidence,
        model_name=model_name,
    )


if __name__ == "__main__":
    app.run(debug=True)
