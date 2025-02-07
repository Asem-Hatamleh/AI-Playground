# Spambase Classification Competition - Top Score Achievement

## Overview
This repository documents my participation and success in the private competition focused on classifying emails as spam or non-spam using the **Spambase dataset**. The dataset consists of 4,601 instances, each described by 57 features, including a mix of categorical and numerical attributes derived from email content and structure. The primary task was to build a model capable of accurately predicting whether an email is spam (1) or not (0).

The competition ran from **May 26, 2024**, to **June 8, 2024**, and I achieved the **top score** in the competition. This README provides a high-level overview of my approach and  results.




![Screenshot 2025-02-07 183034](https://github.com/user-attachments/assets/905cb52a-3984-4afb-aa32-c9b9cf04b270)



---

## Dataset
The dataset used in this competition is the **Spambase dataset**, cited as:
- **Hopkins, Mark, Reeber, Erik, Forman, George, and Suermondt, Jaap. (1999). Spambase. UCI Machine Learning Repository.** [DOI: 10.24432/C53G6X](https://doi.org/10.24432/C53G6X).

The dataset was provided in CSV format, and the task involved loading the data, preprocessing it, and building a classification model to predict the target variable (`spam`).

---

## Approach
To achieve the top score, I followed a structured approach:

1. **Data Exploration and Visualization**:
   - Analyzed the distribution of the target variable (`spam`) to understand class imbalance.
   - Visualized key insights to guide preprocessing and modeling decisions.

2. **Data Preprocessing**:
   - Split the dataset into features (`X`) and target (`y`).
   - Further divided the training data into training and validation sets to evaluate model performance.

3. **Model Selection and Training**:
   - Utilized a **Random Forest Classifier** due to its robustness and ability to handle high-dimensional data.
   - Trained the model on the training split and tuned hyperparameters for optimal performance.

4. **Feature Importance Analysis**:
   - Extracted and visualized feature importances to identify the most influential attributes in the dataset.

5. **Model Evaluation**:
   - Evaluated the model on the validation set using the **F1 score**, the competition's evaluation metric.
   - Achieved a high F1 score, indicating strong performance in classifying spam and non-spam emails.

6. **Prediction and Submission**:
   - Generated predictions for the test dataset and formatted the results as per the competition's submission guidelines.
   - Saved the predictions in a CSV file for submission.

---

## Results
- **Competition Metric**: F1 Score
- **Achievement**: **Top Score** in the competition.
- **Key Insights**:
  - The Random Forest model demonstrated excellent performance in handling the dataset's complexity.
  - Feature importance analysis revealed the most critical attributes for spam detection, aligning with domain expectations.

---

## Repository Structure
- **Code**: The complete implementation is available in the associated Python script or notebook.
- **Submission File**: The final submission file (`submission.csv`) is included in the repository.
- **Visualizations**: Key plots and charts are saved for reference.

---

## Acknowledgments
I would like to thank the competition organizers for providing this challenging dataset and opportunity. Special thanks to the creators of the Spambase dataset for making it publicly available for research and learning purposes.

---

## How to Use
To replicate or build upon this work:
1. Clone the repository.
2. Ensure the dataset is placed in the correct directory.
3. Run the provided code to preprocess the data, train the model, and generate predictions.


