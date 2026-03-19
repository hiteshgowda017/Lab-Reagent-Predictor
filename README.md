# AI-Driven Diagnostic Reagent Demand Predictor

An AI-powered application built using **Python**, **Streamlit**, and **Facebook Prophet** to help laboratories and researchers predict reagent demand for diagnostic tests based on historical data.

This tool analyzes past lab test data and generates **AI-based forecasts** to help labs manage reagent inventory efficiently.

---

## 🚀 Features

* Upload historical laboratory test data (CSV)
* Select a diagnostic test to analyze
* AI-powered demand forecasting
* 14-day reagent demand prediction
* Interactive dashboard using Streamlit
* Helps laboratories manage reagent inventory efficiently

---

## 📂 Project Structure

ai-diagnostic-reagent-demand-predictor

│

├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── test_data.csv

---

## ⚙️ Requirements

* Python 3.8 or higher
* pip (Python package manager)

---

## 🖥️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/hiteshgowda017/Lab-Reagent-Predictor.git

```

### 2. Go to the project folder

```bash
cd Lab-Reagent-Predictor
```

### 3. Install required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

### 5. Open in your browser

```
http://localhost:8501
```

---

## 📊 Example CSV Format

Your CSV file should look like this:

```
Date,Dengue_NS1
2024-01-01,12
2024-01-02,15
2024-01-03,10
2024-01-04,18
2024-01-05,14
```

---

## 🧠 Technologies Used

* Python
* Streamlit
* Pandas
* Facebook Prophet

---

## 👨‍💻 Author

**Hitesh Gowda**
Artificial Intelligence & Data Science Student

GitHub:
https://github.com/hiteshgowda017
