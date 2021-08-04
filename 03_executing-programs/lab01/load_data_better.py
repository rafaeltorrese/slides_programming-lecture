import csv
from pprint import pprint

def load_csv(filename):
    with open(filename, "r") as file:
        data = [*csv.reader(file)]
    return data

def column_to_string(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

if __name__ == "__main__":
    # Load pima-indians-diabetes dataset
    filename = "03_executing-programs\lab01\pima-indians-diabetes.csv"
    dataset = load_csv(filename)
    print(f"Loaded data file {filename} with {len(dataset)} rows and {len(dataset[0])} columns")
    print(dataset[0])

    # convert string columns to float
    ncols = len(dataset[0])
    for i in range(ncols):
        column_to_string(dataset, i)
    print(dataset[0])
