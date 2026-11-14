# 🚚 Industrial Supply Chain Late-Delivery Risk Predictor

Predicting high-risk late deliveries at order intake to optimize manufacturing dispatch schedules, prevent contract penalties, and improve B2B customer satisfaction.

🔗 *Live Web App:* [https://industrial-order-risk-analyzer-kb6yy6dhrvlthg6dlntvi5.streamlit.app/]  
📊 *Dataset Source:* [DataCo Smart Supply Chain Dataset (Kaggle)](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis)

---

## 📌 Problem Framing & Business Objective
Manufacturing facilities and industrial plants often struggle with unexpected delivery delays, especially under tight dispatch windows or high-priority shipping modes. This project builds an end-to-end Machine Learning classification pipeline (Late_delivery_risk: 1 = Late Risk, 0 = On-Time) prioritizing *Recall* and *F1-Score* to flag risky orders before dispatch.

---

## 📈 Model Comparison Results (5-Fold Cross-Validation)

| Model | CV Recall | CV F1-Score | CV Accuracy |
| :--- | :---: | :---: | :---: |
| *Baseline (Majority Class)* | 1.0000 | 0.6846 | 0.5204 |
| *Logistic Regression* | 0.5041 | 0.6230 | 0.6827 |
| *Random Forest* | 0.5994 | 0.6367 | 0.6442 |
| *Gradient Boosting (Tuned)* | *0.5078* | *0.6274* | *0.6863* |

---

## 🛠️ How to Run Locally
1. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/supply-chain-delay-predictor.git](https://github.com/YOUR_USERNAME/supply-chain-delay-predictor.git)
