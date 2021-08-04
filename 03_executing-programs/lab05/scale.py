from pprint import pprint
def data_minmax(dataset):
    minmax = []
    ncols = len(dataset[0])
    for i in range(ncols):
        col_values = [row[i] for row in dataset]
        value_min = min(col_values)
        value_max = max(col_values)
        minmax.append([value_min, value_max])
    return minmax

if __name__ == '__main__':
    dataset = [[50, 30], [20, 90]]
    pprint(dataset)
    
    # Calculate min and max for each colum
    minmax = data_minmax(dataset)
    print()
    pprint(minmax)