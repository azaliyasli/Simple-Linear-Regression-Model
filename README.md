# 📈 Simple Linear Regression: Salary vs Experience

This project demonstrates how to use **Simple Linear Regression** to predict employee salaries based on their years of experience.

---

## 🧠 Problem Summary

Given a dataset `Salary_Data.csv` that contains:
- `Years of Experience`
- `Salary`

The goal is to predict the salary of a person based on their experience using a linear regression model.

---

## 🔧 Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

---

## 🚀 Steps Performed

1. **Data Preprocessing**
   - Load CSV using `pandas`
   - Separate independent (`X`) and dependent (`y`) variables
   - Split into **training** and **validation** sets

2. **Model Training**
   - Use `LinearRegression` from `sklearn.linear_model`
   - Train the model using the training set

3. **Prediction**
   - Predict salaries for the validation set

4. **Visualization**
   - Plot the **training set** and regression line
   - Plot the **validation set** using the same regression line
     
5.**Evaluation**
   -Evaluate the performance of model with R-Squared

---

## 📊 Output

- A blue regression line fitted to the red data points
- Two separate plots:
  - Training Set
  - Validation Set

> The same regression line is plotted in both figures because a simple linear regression model results in a **unique** line based on the training data.

---

## 📁 Dataset Info

Ensure you have a file named `Salary_Data.csv` in your working directory with the following columns:

| YearsExperience | Salary     |
|-----------------|------------|
| 1.1             | 39343.00   |
| 1.3             | 46205.00   |
| ...             | ...        |

---

## 📦 Installation

1. Clone the repo or copy the code.
2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib scikit-learn
