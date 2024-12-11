from aocd import data

m = [line.strip() for line in data.strip().split('\n')]
length = len(m)
print(m[2][1])

def find_xmas(grid):
    directions = [
        (0, 1),   
        (0, -1),  
        (1, 0),   
        (-1, 0),  
        (1, 1),   
        (-1, -1), 
        (1, -1),  
        (-1, 1),  
    ]
    
    rows = len(grid) 
    cols = len(grid[0])  
    count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'X': 
                for direction in directions:
                    # Try to form "XMAS" in this direction
                    if check_direction(grid, i, j, direction, rows, cols):
                        count += 1
    return count

def check_direction(grid, x, y, direction, rows, cols):
    word = "XMAS"
    letter_index = 1 
    current_x, current_y = x, y
    
    # Move through the grid in the given direction, looking for 'M', 'A', and 'S'
    while True:
        current_x += direction[0]
        current_y += direction[1]

        if not (0 <= current_x < rows and 0 <= current_y < cols):
            return False

        if grid[current_x][current_y] != word[letter_index]:
            return False  

        letter_index += 1

        if letter_index == len(word): 
            return True

print(f'Part 1: {find_xmas(m)}')

# Part 2

def find_xmas2(grid):
    directions = [
        (1, 1),   
        (1, -1),
        (-1, 1),
        (-1, -1), 
    ]
    
    rows = len(grid) - 1
    cols = len(grid[0]) - 1
    count = 0

    for i in range(1, rows):
        for j in range(1, cols):
            if grid[i][j] == 'A': 
                if check_cross(grid, i, j, directions):
                    count += 1
    return count

def check_cross(grid, x, y, directions):
    combinations = ["SMSM", "SSMM", "MMSS", "MSMS"]
    word = ""
    for direction in directions:
        new_x = x + direction[0]
        new_y = y + direction[1]
        word += grid[new_x][new_y]
        if word in combinations:
            return True
    return False

print(f'Part 2: {find_xmas2(m)}')