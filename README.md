# Project: Medical Data Analysis and Visualization

This project demonstrates how to preprocess, analyze, and visualize medical examination data, focusing on BMI calculation, normalization of health indicators, and correlation analysis.

## Objectives:

1. **Data Preprocessing**:
    - Load and clean the dataset using pandas.
    - Calculate the Body Mass Index (BMI) and create a new column `overweight` to indicate individuals with a BMI greater than 25.
    - Normalize the `cholesterol` and `gluc` columns by adjusting the values to either `0` (normal) or `1` (above normal).

2. **Categorical Analysis**:
    - Transform the dataset into a long format using `pd.melt()` to facilitate categorical plotting.
    - Create a categorical plot to compare the distribution of health indicators (cholesterol, glucose, smoking, alcohol consumption, activity, and overweight) for individuals with and without cardiovascular disease.

3. **Outlier Removal**:
    - Filter the dataset to remove inconsistent and extreme values:
        - Ensure systolic blood pressure (`ap_hi`) is greater than or equal to diastolic blood pressure (`ap_lo`).
        - Remove outliers based on height and weight using the 2.5th and 97.5th percentiles.

4. **Correlation Analysis**:
    - Calculate a correlation matrix for numerical variables in the cleaned dataset.
    - Visualize the correlations using a heatmap, masking the upper triangle to improve readability.

## Tools and Libraries:

- **Pandas**: For data loading, manipulation, and cleaning.
- **NumPy**: For numerical operations and matrix calculations.
- **Matplotlib & Seaborn**: For data visualization, including categorical plots and heatmaps.

## Outcomes:

- A cleaned and preprocessed dataset ready for analysis.
- Visualization of the distribution of health indicators based on cardiovascular disease presence.
- Identification of key correlations between medical variables using a heatmap.
- Understanding of how cholesterol, glucose levels, smoking, alcohol consumption, activity, and BMI relate to cardiovascular disease.
