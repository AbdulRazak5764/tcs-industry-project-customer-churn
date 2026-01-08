# Customer Churn Prediction Using Machine Learning

## 📌 Project Overview
Customer churn prediction is a critical business problem where organizations aim to identify customers who are likely to discontinue their services. Retaining existing customers is significantly more cost-effective than acquiring new ones.

This project implements a complete end-to-end machine learning pipeline to predict customer churn using supervised learning techniques. The project is developed as part of the **TCS Industry Project (Academic Year 2024–2025)**.

---

## 🎯 Objectives
- Analyze customer behavior using demographic and service usage data  
- Predict whether a customer is likely to churn  
- Handle class imbalance using SMOTE  
- Compare multiple machine learning models  
- Provide business insights and retention strategies  

---

## 📂 Dataset
- **Source:** IBM Watson Telco Customer Churn Dataset  
- **Total Records:** 7043  
- **Total Features:** 21  
- **Target Variable:** Churn (Yes / No)

### Feature Categories
- **Demographic:** Gender, Senior Citizen, Partner, Dependents  
- **Service:** Internet Service, Streaming, Online Security, Tech Support  
- **Account:** Tenure, Contract Type, Monthly Charges, Total Charges  

---

## 🛠️ Tools & Technologies
- **Programming Language:** Python  
- **Environment:** Jupyter Notebook  

### Libraries Used
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  
- Imbalanced-learn (SMOTE)  
- XGBoost  

---

## ⚙️ Methodology
1. **Data Loading & Exploratory Data Analysis**
   - Missing value handling
   - Churn distribution analysis
   - Feature-wise churn insights

2. **Data Preprocessing**
   - Encoding categorical variables
   - Feature scaling
   - Train-test split (80:20)

3. **Feature Engineering**
   - Service count features
   - Contract-based risk features
   - Customer value score

4. **Model Training**
   - Logistic Regression  
   - Random Forest  
   - Gradient Boosting  
   - XGBoost  
   - Extra Trees  

5. **Class Imbalance Handling**
   - Applied SMOTE on training data

6. **Ensemble Learning**
   - Voting Classifier  
   - Stacking Classifier  

7. **Model Evaluation**
   - Accuracy, Precision, Recall, F1-Score  
   - ROC-AUC, PR-AUC  
   - Confusion Matrix & Visualizations  

---

## 📊 Results
- **Best Model:** Ensemble / Gradient Boosting based model  
- **Accuracy:** ~80–85%  
- **ROC-AUC:** ~0.86  
- Improved recall for churn customers after SMOTE  

---

## 💼 Business Impact
- Early identification of high-risk customers  
- Reduced customer acquisition cost  
- Improved retention strategy planning  
- Estimated significant annual cost savings  

---

## 🚀 Deployment Readiness
- Trained model saved using `joblib`  
- Preprocessing pipeline saved  
- Feature names and metadata stored  
- Deployment-ready prediction class included  

---

## 📁 Project Structure
├── Dataset/
│ └── WA_Fn-UseC_-Telco-Customer-Churn.xlsx
├── eda_visualizations.png
├── model_evaluation.png
├── best_churn_model.pkl
├── preprocessing_pipeline.pkl
├── feature_names.json
├── model_metadata.json
├── churn_predictor.py
├── requirements.txt
├── project_final_report.txt
└── README.md


---

## 📌 Conclusion
This project successfully demonstrates how supervised machine learning techniques can be used to predict customer churn with high accuracy and strong business relevance. The system is scalable and ready for real-world deployment with further enhancements.

---

## 🔮 Future Scope
- Real-time churn prediction dashboard  
- Integration with live customer data  
- Advanced deep learning models  
- Customer sentiment analysis  

---

## 👤 Author
**Shaik Abdul Razak**  
B.Tech – Computer Science Engineering  
TCS Industry Project (2024–2025)

---

## 📚 References
- IBM Watson Telco Customer Churn Dataset  
- Scikit-learn Documentation  
- GeeksforGeeks – Machine Learning Tutorials  


