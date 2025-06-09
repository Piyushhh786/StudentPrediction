# 📊 Student Performance Prediction Web App

A full-stack **Machine Learning web application** that predicts a student’s expected score based on key input parameters like study hours, past scores, sleep, and extracurricular activities. This project integrates **Linear Regression**, **Flask API**, a **PostgreSQL** database, and a frontend built using **Next.js**.

---

## 🚀 Features

- 🔍 Predicts student scores using a trained ML model
- 💡 Clean and simple web UI for input
- 🔄 Backend served via Flask API
- 🛢️ Stores submitted inputs into PostgreSQL
- 📊 Model trained using Linear Regression (scikit-learn)
- 🌐 Deployed frontend (e.g., on Vercel) and backend (e.g., Render)

---

## 🎯 Tech Stack

| Layer        | Technology        |
|--------------|-------------------|
| Frontend     | Next.js, React, TypeScript |
| Backend API  | Flask (Python)     |
| ML Model     | Scikit-learn (Linear Regression) |
| Database     | PostgreSQL         |
| Styling      | Tailwind CSS (optional) |
| Deployment   | Vercel (frontend), Render (backend) |

---

## 📈 Model Details

- **Algorithm**: Linear Regression
- **Inputs**:  
  - Hours Studied  
  - Previous Score  
  - Sleep Hours  
  - Extracurricular Activities  
  - Sample Papers Practiced

- **Target**: Predicted Final Exam Score

---

## 🧪 Sample Input (JSON)

{
  "hours_studied": 4,
  "previous_score": 65,
  "sleep_hours": 7,
  "extracurricular_activities": 1,
  "sample_papers_practiced": 3
}
---
## 🌍 Live Demo
🔗 Frontend: [!Demo](https://student-prediction-web.vercel.app)


