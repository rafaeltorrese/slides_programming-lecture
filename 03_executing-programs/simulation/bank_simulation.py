import random

def interarrival_time_distr(a, b):
    'This function returns a uniform random between (a, b)'
    return a + random.random() * (b - a)


if __name__ == "__main__":
    inter_arrival_time = interarrival_time_distr(0, 5)
    