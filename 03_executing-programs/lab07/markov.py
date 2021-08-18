import numpy as np
def markov_chain(data):
    states = {k:v for v, k in enumerate(set(data))}
    num_states = len(states)
    count_matrix = np.zeros((num_states, num_states))
    for i, j in zip(data, data[1:]):
        count_matrix[ states[i], states[j]] += 1
    totals = count_matrix.sum(axis=1)
    return np.divide(count_matrix, totals[:, np.newaxis])


for i, j in zip(data, data[1:]):
    count_matrix[ states[i], states[j]] += 1    

if __name__ == '__main__':

    data = list("CCSWRRWSSCCCRCSSWRCRRRRRCWSSWRWWRCRRRRCWSSWRWCCSWRRWSSCCCRCSSWSSWRWWRCRRRRCWSSWRWCCSWRRWSSS")

    print(len(data))

    states = {k:v for v, k in enumerate(set(data))}
    print(states)

    num_states = len(states)
    count_matrix = np.zeros((num_states, num_states))

    for i, j in zip(data, data[1:]):
        count_matrix[ states[i], states[j]] += 1

    print(count_matrix)

    print(count_matrix.sum())

    totals = count_matrix.sum(axis=1)
    probabilities = np.divide(count_matrix, totals[:, np.newaxis])
    print(probabilities)

    print(probabilities.sum(axis=1))