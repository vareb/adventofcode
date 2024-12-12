from aocd import data
strings = [line.strip() for line in data.strip().split('\n')]
numbers = []
for line in strings:
    parts = line.split(':')
    id_number = int(parts[0].strip())
    number_list = list(map(int, parts[1].strip().split()))  
    numbers.append([id_number] + number_list)

# Part 1

def can_create_goal(test):
    goal = test[0]
    
    def recursive_helper(current_value, remaining_numbers):
        if not remaining_numbers:
            return current_value == goal
        
        next_number = remaining_numbers[0]
        return (recursive_helper(current_value + next_number, remaining_numbers[1:]) or
                recursive_helper(current_value * next_number, remaining_numbers[1:]))

    return recursive_helper(test[1], test[2:])

    
    
def total_test_values(tests):
    sum = 0
    for test in tests:
        if can_create_goal(test):
            sum += test[0]
    return sum

print(f'Part 1: {total_test_values(numbers)}')

# Part 2

def concat(n, m):
    n_str = str(n)
    m_str = str(m)

    return int(n_str + m_str)
    
def can_create_goal2(test):
    goal = test[0]
    
    def recursive_helper(current_value, remaining_numbers):
        if not remaining_numbers:
            return current_value == goal
        
        next_number = remaining_numbers[0]
        return (recursive_helper(current_value + next_number, remaining_numbers[1:]) or
                recursive_helper(current_value * next_number, remaining_numbers[1:]) or 
                recursive_helper(concat(current_value, next_number), remaining_numbers[1:]))

    return recursive_helper(test[1], test[2:])

    
    
def total_test_values2(tests):
    sum = 0
    for test in tests:
        if can_create_goal2(test):
            sum += test[0]
    return sum


print(f'Part 2: {total_test_values2(numbers)}')
