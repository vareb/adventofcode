from aocd import data

part1, part2 = data.split('\n\n')
rules = [line.strip() for line in part1.strip().split('\n')]
rules = [list(map(int, item.split('|'))) for item in rules]

updates = [line.strip() for line in part2.strip().split('\n')]
updates = [list(map(int, item.split(','))) for item in updates]

rules_dict = {}
for x, y in rules:
    if x not in rules_dict:
        rules_dict[x] = []
    rules_dict[x].append(y)

# Part 1

def check_update(update):
    for index, page in enumerate(update):
        before = update[:index]
        for n in before:
            if n in rules_dict[page]:
                return False
    return True
    
def sum_of_updates(updates):
    sum = 0
    for update in updates:
        if check_update(update):
            sum += update[(len(update))//2]
    return sum
    
print(f'Part 1: {sum_of_updates(updates)}')

# Part 2

def swap_wrong(update):
    while not check_update(update):
        for index, page in enumerate(update):
            before_indices = range(index) 
            for n in before_indices:
                if update[n] in rules_dict[page]:
                    update[n], update[index] = update[index], update[n]
    return update

def sum_of_incorrect_updates(updates):
    sum = 0
    for update in updates:
        if not check_update(update):
           new_update = swap_wrong(update)
           sum += update[(len(new_update))//2]
    return sum

print(f'Part 2: {sum_of_incorrect_updates(updates)}')