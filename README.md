# 📊 CSV Reader – Streamlit App

A beginner-friendly **Streamlit web app** that allows users to upload CSV files, explore their data, and filter rows based on column values using an interactive interface.

---

## 📌 What This Project Does

This project lets users:

- Upload a CSV file
- View the full dataset interactively
- Filter data by a selected column
- Display:
  - All values from a column
  - Rows matching an exact value

---

## 🧠 How the Project Works


### 1️⃣ CSV Upload

- User uploads a `.csv` file
- The file is read using **pandas**
- Data is displayed in an interactive table

---

### 2️⃣ Column Selection

- User enters the column name they want to filter by
- The column is confirmed using a button
- Session state stores the confirmation

---

### 3️⃣ Data Filtering

- User enters a value to filter rows
- Special case:
  - Typing `all` shows the entire selected column
- Otherwise:
  - Rows are filtered using an exact match


---

## 🚫 What This Project Does NOT Do

- No advanced filtering (contains / regex)
- No multiple column filtering
- No database integration
- No CSV export (yet)

---

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **Pandas**


---

## ▶️ How to Run the Project

```bash
pip install streamlit pandas numpy
```
```bash
streamlit run app.py
```

## 👤 Author

Roshan Karki  
Python & Web Scraping Learner