import random
import math
import statistics
import matplotlib.pyplot as plt

def parts_distr(a, b):
    'This function returns a uniform random variable between a and b'
    return a + random.random() * (b - a)

def demand_distribution(mu, sigma):
    'This function returns a normal random variable with standard deviation sigma and mean mu'
    return (math.sqrt(-2 * math.log(1 - random.random())) * math.cos(2 * math.pi * random.random())) * sigma + mu

def work_distr(*args):
    'This function returns a discrete probability distribution for the workforce cost'
    R = random.random()
    for a in args[::2]:
        print(a)
    # cumulative_distr = []
    # cum = 0
    # for probability in args:
    #     cum += probability
    #     cumulative_distr.append(cum)

    # return cumulative_distr


if __name__ == '__main__':
    print(parts_distr(80, 100))

    
    demand_values = [demand_distribution(15000, 4500) for _ in range(1000)]
    print(statistics.mean(demand_values))
    print(statistics.stdev(demand_values))
    
    print(work_distr(43, 0.10, 44, 0.30, 45, 0.70, 46, 0.90, 47, 1.))
