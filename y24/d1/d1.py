from aocd import data
from collections import Counter

column1, column2 = zip(*[map(int, line.split()) for line in data.splitlines()])

column1 = list(column1)
column2 = list(column2)

column1 = sorted(column1)
column2 = sorted(column2)

# Part 1

sum = 0
for n in range(0, len(column1)):
    sum += abs(column1[n] - column2[n])
print(f'Part 1: {sum}')


# Part 2
occurences = dict(Counter(column2))

score = 0
for number in column1:
    if number in occurences:
        score += occurences[number] * number
print(f'Part 2: {score}')


