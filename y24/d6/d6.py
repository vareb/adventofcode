from aocd import data
map = [line.strip() for line in data.strip().split('\n')]

test = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

test = [line.strip() for line in test.strip().split('\n')]


# Part 1

directions = { # key , [ current direction, next direction ]
    "U": [(-1, 0),"R"], 
    "D": [(1, 0),"L"],      
    "L": [(0, -1),"U"],  
    "R": [(0, 1),"D"]
}

def find_guard(map):
    for j in range(len(map)):
        for i in range(len(map[j])):
            if map[j][i] == '^':
                return j, i
    

def distinct_positions(map):
    positions = set()
    x, y = find_guard(map)
    positions.add((x,y))
    direction = "U"
    next_pos = (x + directions[direction][0][0], y + directions[direction][0][1])

    while 0 <= next_pos[0] < len(map) and 0 <= next_pos[1] < len(map):
        if map[next_pos[0]][next_pos[1]] == "#":
            direction = directions[direction][1]
        x += directions[direction][0][0]
        y += directions[direction][0][1]
        if (x,y) not in positions:
            positions.add((x,y))
        next_pos = (x + directions[direction][0][0], y + directions[direction][0][1])
    
    return positions
        
print(f'Part 1: {len(distinct_positions(map))}')

# Part 2

def check_loop(map):
    positions = set()
    x, y = find_guard(map)
    direction = "U"
    positions.add((x,y,direction))
    next_pos = (x + directions[direction][0][0], y + directions[direction][0][1])

    while 0 <= next_pos[0] < len(map) and 0 <= next_pos[1] < len(map):
        while map[next_pos[0]][next_pos[1]] == "#":
            direction = directions[direction][1]
            next_pos = (x + directions[direction][0][0], y + directions[direction][0][1])
        dx, dy = directions[direction][0]
        x += dx
        y += dy
        if (x,y,direction) in positions:
            return True
        else:
            positions.add((x,y,direction))
        next_pos = (x + dx, y + dy)

    return False


def number_blocks(map):
    sum = 0
    positions = distinct_positions(map)
    for j, i in positions:
        if map[j][i] == '.':
            map[j] = map[j][:i] + '#' + map[j][i+1:]
            if check_loop(map):
                sum += 1
            map[j] = map[j][:i] + '.' + map[j][i+1:]
    return sum

print(f'Part 2: {number_blocks(map)}')
