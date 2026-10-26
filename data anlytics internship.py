import os

folder = r"C:\Users\MANIKHAN\Downloads\chronic+kidney+disease\Chronic_Kidney_Disease\Chronic_Kidney_Disease"

print(os.listdir(folder))
import pandas as pd
from scipy.io import arff
#Step 1 Dataset Path
file_path = r"C:\Users\MANIKHAN\Downloads\chronic+kidney+disease\Chronic_Kidney_Disease\Chronic_Kidney_Disease\chronic_kidney_disease.arff"
# Step 2 Dataset Load
file_path = r"C:\Users\MANIKHAN\Downloads\chronic+kidney+disease\Chronic_Kidney_Disease\Chronic_Kidney_Disease\chronic_kidney_disease.arff"

reading_data = False

with open(file_path, "r") as file:
    for line_number, line in enumerate(file, start=1):
        line = line.strip()

        if line.lower() == "@data":
            reading_data = True
            continue

        if reading_data and line:
            number_of_values = len(line.split(","))

            if number_of_values != 25:
                print("Line:", line_number)
                print("Number of values:", number_of_values)
                print("Row:", line)
                print("-" * 50)
import pandas as pd
print("Pandas ready")
rows = []
print(rows)
with open(file_path,"r") as file:
    rows=file.readlines()
    print(len(rows))
    print(rows[0])
    print(rows[2])
    print(repr(rows[1]))
    import pandas as pd
import csv

file_path = r"C:\Users\MANIKHAN\Downloads\chronic+kidney+disease\Chronic_Kidney_Disease\Chronic_Kidney_Disease\chronic_kidney_disease.arff"

columns = []
rows = []
reading_data = False

with open(file_path, "r") as file:
    for line in file:
        line = line.strip()

        if line.lower() == "@data":
            reading_data = True
            continue

        if not reading_data:
            if line.lower().startswith("@attribute"):
                columns.append(line.split()[1].strip("'\""))
            continue

        if line:
            row = next(csv.reader([line]))
            row = [value.strip() for value in row]

            if len(row) == len(columns) + 1 and row[-1] == "":
                row = row[:-1]

            if len(row) == len(columns):
                rows.append(row)

df = pd.DataFrame(rows, columns=columns)

print(df.head())
print("Rows and columns:", df.shape)
print(df.isnull().sum())
print("Total missing values:",df.isnull().sum())
df.replace("?",pd.NA,inplace=True)
print("Total missing values:", df.isnull().sum().sum())
print("Duplicate rows:",df.duplicated().sum())
print("Total rows before cleaning:",len(df))
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

print(df["class"].value_counts(dropna=False))
print(df.dtypes)
numeric_cols = ["age", "bp", "bgr", "bu", "sc", "sod", "pot", "hemo"]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print(df[numeric_cols].dtypes)
more_numeric = ["sg", "al", "su", "pcv", "wbcc", "rbcc"]

for col in more_numeric:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print(df[more_numeric].dtypes)
print("Missing values per column:")
print(df.isnull().sum())
numeric_cols = df.select_dtypes(include="number").columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())
print("Remaining missing values:", df.isnull().sum().sum())
text_cols = df.select_dtypes(include="object").columns

for col in text_cols:
    df[col] = df[col].fillna("Unknown")

print("Remaining missing values:", df.isnull().sum().sum())
df.to_csv("cleaned_kidney_disease.csv", index=False)
print("Dataset saved successfully!")
for col in ["rbc", "pc", "pcc", "ba", "htn", "dm", "cad", "appet", "pe", "ane", "class"]:
    print("\n", col)
    print(df[col].value_counts(dropna=False))
    df.to_csv(r"C:\Users\MANIKHAN\Downloads\cleaned_kidney_disease.csv", index=False)
print("Dataset saved successfully!")