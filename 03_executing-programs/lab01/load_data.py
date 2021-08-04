import csv

def load_csv(filename):
    file = open(filename, "r")
    lines = csv.reader(file)
    dataset = [*lines]
    file.close()
    return dataset

if __name__ == "__main__":
    filename = "03_executing-programs\lab01\pima-indians-diabetes.csv"
    dataset = load_csv(filename)
    print(f"Loaded data file {filename} with {len(dataset)} rows and {len(dataset[0])} columns")
