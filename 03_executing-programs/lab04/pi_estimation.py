"""
Estimation of pi number
"""
import pifunction

trials = 50000
success = 0

for _ in range(trials):
    success += pifunction.inside_circle()
pi_estimation = 4 * (success / trials)


print(f"Estimation of pi number is {pi_estimation:0.4f}")