# 🎓 Smart Student Performance & Placement Predictor

An end-to-end Machine Learning project that predicts:
1. **Student academic performance (Pass/Fail)**
2. **Expected placement package based on CGPA**

This project demonstrates the complete ML workflow — from data preprocessing and model training to deployment using a web interface.

---

## 📌 Project Motivation

Educational institutions and students often lack data-driven insights to evaluate academic performance and placement readiness.  
This project aims to:
- Predict whether a student is likely to **pass or fail**
- Estimate the **expected placement package** based on academic performance

The system helps students understand their current standing and areas of improvement.

---

## 🧠 Machine Learning Approach

The project uses **two different ML models**, selected based on data characteristics:

### 1️⃣ Academic Performance Prediction
- **Problem Type:** Binary Classification
- **Target:** Pass / Fail
- **Model Used:** Logistic Regression
- **Key Features:**
  - Study time
  - Absences
  - Past failures
  - First and second period grades (G1, G2)

### 2️⃣ Placement Package Prediction
- **Problem Type:** Regression
- **Target:** Placement Package (LPA)
- **Model Used:** Linear Regression
- **Key Feature:**
  - CGPA

> The placement problem was modeled as a regression task after analyzing the dataset and identifying that all students were placed.

---

## 🛠 Tech Stack

- **Programming Language:** Python  
- **Libraries:**  
  - NumPy  
  - Pandas  
  - Scikit-learn  
- **Visualization:** Matplotlib, Seaborn  
- **Deployment:** Streamlit  
- **Version Control:** Git & GitHub  

---

## 📂 Project Structure

Smart-Student-ML/
│
├── data/
│   ├── student-por.csv
│   └── placement.csv
│
├── notebooks/
│   ├── EDA.ipynb
│   └── Model_Training.ipynb
│
├── academic_model.pkl
├── academic_scaler.pkl
├── placement_model.pkl
├── placement_scaler.pkl
│
├── app.py
├── requirements.txt
└── README.md

---

## ▶ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/shaheerasara7604/Smart-Student-ML.git
cd Smart-Student-ML

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the Streamlit App

streamlit run app.py

The application will open in your browser and allow real-time predictions.

⸻

📊 Results & Evaluation
	•	Academic Performance Model
	•	Accuracy achieved: ~70–85%
	•	Placement Package Model
	•	Evaluated using MAE and R² score

The models were chosen for interpretability and reliability, making them suitable for real-world use and interviews.

⸻

🧑‍💼 What This Project Demonstrates
	•	End-to-end machine learning pipeline
	•	Proper feature selection and preprocessing
	•	Model evaluation and interpretation
	•	Deployment of ML models using Streamlit
	•	Clean project structure and GitHub version control

⸻

🚀 Future Enhancements
	•	Add more placement-related features (internships, skills, aptitude scores)
	•	Improve models using ensemble techniques
	•	Deploy the app on cloud platforms (Heroku / Streamlit Cloud)
	•	Add authentication for multiple users

⸻

👩‍💻 Author

Sara
Aspiring Machine Learning Engineer / Data Science Enthusiast

⸻

⭐ If you find this project useful, feel free to star the repository!

---

### ✅ Why this README is strong
- Clear problem statement  
- Honest modeling decisions  
- Interview-safe explanations  
- Professional structure
- No overclaiming  

If you want, I can next:
- Rewrite this README to sound **even more recruiter-oriented**
- Add **screenshots section**
- Prepare a **project explanation script for interviews**
- Optimize this for **LinkedIn + resume**

Just tell me what you want next.
