import csv
import re

def string_to_float(filename):
    'Read numbers as strings from a filename and transforms it to float format'
    pattern = "^\d*\.?\d+"
    regex = re.compile(pattern)
    with open(filename) as file:
        return [ 
                [ float(element) if regex.match(element) else element for element in row ] 
                for row in csv.reader(file, delimiter=',')
                ]

if __name__ == "__main__":
    # Load pima-indians-diabetes dataset
    filename = r"03_executing-programs\data\iris.csv"
    dataset = load_csv(filename)
    print(f"Loaded data file {filename} with {len(dataset)} rows and {len(dataset[0])} columns")

    # convert string columns to float
    ncols = len(dataset[0])
    for i in range(ncols - 1):
        column_to_float(dataset, i)

    # convert class column to integer
    lookup = column_to_integer(dataset, 4)
    print(dataset[0])
    print(lookup)

    dataset02 = string_to_float(filename)
    pprint(dataset02[0])