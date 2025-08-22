# Predictive Analysis of School Performance
An end-to-end data science pipeline using Azure Databricks.

**Predictive Analysis of School Performance**

This project demonstrates a complete approach to data analysis and machine learning, from cloud data ingestion to the construction of a predictive model. The goal is to predict students' final grades, which can be a valuable tool for identifying at-risk students and directing educational interventions.

The end-to-end approach of this project reflects industry best practices, using a data pipeline that integrates the Azure ecosystem and the most popular analysis tools.

**1. Project Structure and Technologies**

This project was built using the following tools and technologies:

* **Cloud Data Management:** Azure Blob Storage
* **Analytics and Machine Learning:** Azure Databricks (using Python)
* **Programming Language:** Python (with libraries such as `pandas`, `scikit-learn`)

**2. Methodology and Workflow**

The project followed a structured workflow to ensure that the analysis and the model were robust and reproducible.

* **Data Ingestion:** The student performance dataset was securely loaded and stored in Azure Blob Storage.
* **Analysis and Modeling:** An Azure Databricks notebook was used to connect to Blob Storage, perform data cleaning, and conduct exploratory data analysis. The Databricks environment was chosen for its ability to efficiently process large volumes of data.
* **Model Building:** A Linear Regression model was trained to predict students' final grades (G3) based on variables such as age, study time, and previous grades (G1, G2).
* **Evaluation and Projection:** The model's performance was evaluated using metrics like R-squared (R²) and Mean Squared Error (MSE). The model was then used to make a projection of the final grade for a hypothetical student, demonstrating its ability to generate actionable insights.

**3. Insights and Impact**

The data analysis revealed that study time, previous exam performance, and absences are the main factors influencing a student's final performance. The ability to predict a student's final grade can have a significant impact on educational strategies, allowing teams to:

* **Identify At-Risk Students:** The model can be used to proactively identify students who are at risk of low performance.
* **Optimize Interventions:** The analysis of risk factors can inform decision-making on where to allocate resources for support programs.
* **Monitor Progress:** The analysis pipeline can be transformed into a dashboard in Power BI to monitor the educational program's performance in real time.

**4. How to Run the Project**

To replicate this project, follow these steps:

* Download the `student-mat.csv` file.
* Create a storage account in Azure Blob Storage and upload the file.
* Create a workspace in Azure Databricks.
* Copy the source code from the `databricksnotebook.ipynb` notebook (this file) and run the cells. Be sure to fill in your Azure credentials.


