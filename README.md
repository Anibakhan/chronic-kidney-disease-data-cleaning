Chronic Kidney Disease Dataset — Data Cleaning

Project Overview

This project focuses on cleaning the Chronic Kidney Disease dataset for a data analytics internship assignment.



Dataset

Format: ARFF (original), CSV (cleaned)

Records loaded: 399

Columns: 25



Data Cleaning Steps

1\. Loaded the dataset into a Pandas DataFrame.

2\. Identified missing values represented by `?`.

3\. Checked for duplicate rows. No exact duplicate rows were found.

4\. Removed leading and trailing spaces from text values.

5\. Converted selected numeric columns to numeric data types.

6\. Filled missing numeric values with each column's median.

7\. Marked remaining missing text values as `Unknown`.

8\. Exported the cleaned dataset to CSV format.



&#x20;Important Notes

\- The loaded dataset contained 399 records. The original expected record count should be verified.

\- Missing values were imputed or marked as `Unknown`; these changes should be considered when interpreting the data.

\- This dataset is intended for data-cleaning practice, not for clinical decision-making.



&#x20;Tools Used

\- Python

\- Pandas

\- Thonny



Output

`cleaned\_kidney\_disease.csv`







