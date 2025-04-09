# 💊 AI-Powered Drug Information and Side Effect Prediction System

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An AI-powered web application to explore drug details, predict potential side effects, and find associated medical conditions. This system uses machine learning models and provides an easy-to-use interface with Streamlit.

---

## 🚀 Demo

<img src="https://github.com/yourusername/drug_info_ml_system/assets/demo.gif" width="100%" alt="App Demo">

> Replace the image link above with a screen recording or image showing how your app works.

---

## 🔍 Features

- 🧾 **Drug Info Search** – Find information about specific drugs and their usage.
- 🧠 **Side Effect Prediction** – Predict potential side effects using ML models.
- 🏥 **Medical Condition Mapping** – View which conditions are treated by specific drugs.
- 📊 **Visual Analytics** – Insights into top drug classes and commonly reported effects.

---

## 🗂️ Project Structure

drug_info_ml_system/ │ ├── app.py # Streamlit application ├── drug_data.csv # Drug information dataset ├── model/ │ └── side_effect_model.pkl # Trained ML model ├── utils/ │ └── helper.py # Helper functions ├── requirements.txt # Required libraries └── README.md # This file

yaml
Copy
Edit

---

## 📦 Installation

1. **Clone this repo**
```bash
git clone https://github.com/yourusername/drug_info_ml_system.git
cd drug_info_ml_system
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app

bash
Copy
Edit
streamlit run app.py
📊 Dataset
The dataset (drug_data.csv) includes fields such as:

Drug_Name

Condition

Side_Effect

Dosage

Drug_Class

Frequency

Model training and prediction is based on these features.

🤖 Machine Learning
Algorithm: RandomForestClassifier

Input: Drug attributes (e.g., class, dosage)

Output: Predicted side effects

Pre-trained model stored in model/side_effect_model.pkl

🛠 Built With
Python

Streamlit

Scikit-learn

Pandas

Matplotlib

📈 Future Scope
Integration with real-time drug APIs (e.g., FDA or DrugBank)

NLP-based search for symptoms and conditions

User feedback loop for model improvement

Export results as PDF or CSV

🙋‍♂️ Use Cases
For patients seeking awareness about medications.

For students learning pharmacology.

For clinicians looking to explore drug-condition relationships.

👨‍💻 Author
Santhosh J
A project focused on intelligent healthcare using machine learning.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
