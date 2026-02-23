import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier , plot_tree
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-"*40
####################################################################

# Step 1: Load the dataset

####################################################################

print(Border)
print("Step 1: Load the Dataset")
print(Border)

DatasetPath= "iris.csv"
df = pd.read_csv(DatasetPath)
print("Dataset gets loaded succesfully...")
print("Initial entries from dataset :")
print(df.head())

####################################################################
# Step 2: Data Analysis
####################################################################
print(Border)
print("Step 2: Data Analysis")
print(Border)

print("shape of dataset :",df.shape)
print("Column Names :",list(df.columns))

print("missing values per column")
print(df.isnull().sum())

print("class distribution  species count")
print(df["species"].value_counts())

print("statiscticsl summery of report")
print(df.describe())

####################################################################
# Step 3: Decide Independent and Dependent variables
####################################################################
print(Border)
print("Step 3: Decide Independent and Dependent variables")
print(Border)

# X: Independent variables / Features
# Y: Dependent variables / Labels
Feature_cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)",
]
X = df[Feature_cols]
Y = df["species"]

print("X shape",X.shape)
print("Y shape",Y.shape)


