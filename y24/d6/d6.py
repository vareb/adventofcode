from aocd import data
map = [line.strip() for line in data.strip().split('\n')]

test = """
....#.....
....^....#
..........
..#.......
.......#..
..........
.#........
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
    
    return len(positions)
        
print(f'Part 1: {distinct_positions(map)}')

# Part 2
