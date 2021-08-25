#%%
import csv
import matplotlib.pyplot as plt
#%%

with open('data/students.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    data = [*csv_reader]

grades, students_count = [*zip(*data)]
students_count = [int(number) for number in students_count]

colors = ('green', *tuple(['gray'] * 4), 'red')
#%%
plt.title('Grades Bar Plot For Biology Class')
plt.xlabel('Grade')
plt.ylabel('Num Students')

plt.bar(grades, students_count, color=colors)
plt.show()