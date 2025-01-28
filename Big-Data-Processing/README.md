# US Accidents Dataset Analysis (2016-2023)

This project focuses on analyzing the US Accidents dataset to identify patterns and trends in traffic accidents across the United States from 2016 to 2023. The analysis involves clustering accident records based on shared attributes such as severity, weather conditions, and road infrastructure to aid in traffic management and safety planning.

## Problem Definition
The goal of this project is to perform a clustering task on the US Accidents dataset to group accident records based on shared attributes. The objective is to identify patterns that reveal:
- Accident hotspots
- Weather-related risks
- Temporal trends

These insights can help authorities improve traffic management and safety planning.

## Objectives
1. **Weather-Based Risk Assessment**: Group accidents by similar weather conditions to analyze how weather impacts accident frequency and severity.
   - **Features**: Temperature(F), Visibility(mi), Wind_Speed(mph), Weather_Condition, Precipitation(in), Humidity(%).
   - **Use Case**: Helps authorities issue targeted weather-related driving advisories.

2. **Infrastructure Impact on Accidents**: Understand the role of road infrastructure and nearby features in accident occurrence.
   - **Features**: Traffic_Signal, Station, Junction, Crossing, Roundabout, Bump, Railway.
   - **Use Case**: Provides insights into whether specific infrastructure elements contribute to accident frequency or severity.

3. **Driver Behavior and Risk Identification**: Cluster accidents to analyze driver-related factors influencing accidents.
   - **Features**: Distance(mi), Visibility(mi), Traffic_Calming, Traffic_Signal, No_Exit.
   - **Use Case**: Aids in designing better awareness campaigns or behavioral interventions.

## Dataset Overview
The dataset used for this project is sourced from [Kaggle](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents/data) and contains approximately 7 million records of traffic accidents in the United States from 2016 to 2023. Key attributes include:
- Date and time of the accident
- Location (latitude and longitude)
- Weather conditions
- Accident severity (minor, major, fatal)
- Number of vehicles involved
- Road conditions

## Data Sampling
To facilitate manageable analysis, a sample of 2 million records was extracted from the full dataset. This sample was split into 3 parts for parallel analysis by different team members, simulating the MapReduce function. Each member worked on a file containing approximately 666,666 records.

## Preprocessing Steps
1. **Data Splitting**: The dataset was split into smaller files, each containing about 666,667 records.
2. **Filtering and Dropping Columns**:
   - Numerical Columns: Identified all numerical columns (float64, int64).
   - Categorical Columns: Identified all categorical columns (object data type).
   - Dropped categorical columns with more than 5 unique values to avoid memory allocation errors.
3. **Data Cleaning**:
   - Filled missing categorical values with the mode.
   - Filled missing numerical values with the median.
4. **Handling Categorical Variables**:
   - Selected categorical variables with 5 or fewer unique values for one-hot encoding.
   - Applied one-hot encoding using `pd.get_dummies()` with `drop_first=True` to avoid multicollinearity.
   - Removed columns with only one unique value to prevent redundancy.
5. **Feature Scaling**: Applied `StandardScaler` to standardize numerical features, ensuring all features are on the same scale.

## Determining the Optimal Number of Clusters (Elbow Method)
- **Inertia Calculation**: Calculated inertia for different values of k (number of clusters) and plotted the inertia values against the number of clusters.
- **Optimal Number of Clusters**: Identified the "elbow" of the curve, which occurred around 15-16 clusters, indicating the best number of clusters for the model.

## Final Clustering and Saving the Results
- **Fitting the K-Means Model**: Applied the k-means clustering algorithm to the scaled data using the optimal number of clusters (16).
- **Adding Cluster Labels**: Added cluster labels as a new column ('Cluster') to the original dataset.
- **Saving the Clustered Dataset**: Saved the dataset with cluster labels to a CSV file (`clustered_dataset.csv`).

## Code

Click [here]( https://github.com/Asem-Hatamleh/AI-Playground/blob/Big-Data-Processing/Code.ipynb ) to access the code for this project.
 

 
