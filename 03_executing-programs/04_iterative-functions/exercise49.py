#%% [markdown]
# # Exiting th function during the for loop
def is_prime(x):
    for i in range(2, x):
        return False if (x % i) == 0 else True

if __name__ == '__main__':
    print(is_prime(7))