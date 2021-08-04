import csv
from pprint import pprint

def load_csv(filename):
    with open(filename, "r") as file:
        data = [*csv.reader(file)]
    return data

def column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

def column_to_integer(datasets, column):
    'Function that transforms string to an integer'
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = {value:i for i, value in enumerate(unique)}
    print(lookup)
    for row in dataset:
        row[column] = lookup[ row[column] ]
    return lookup


if __name__ == "__main__":
    # Load pima-indians-diabetes dataset
    filename = r"03_executing-programs\data\iris.csv"
    dataset = load_csv(filename)
    print(f"Loaded data file {filename} with {len(dataset)} rows and {len(dataset[0])} columns")

    # convert string columns to float
    ncols = len(dataset[0])
    for i in range(ncols - 1):
        column_to_float(dataset, i)
    print(dataset[0])

    # convert class column to integer
    lookup = column_to_integer(dataset, 4)
    print(dataset[0])
    print(lookup)
