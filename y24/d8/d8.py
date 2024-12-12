from aocd import data
m = [line.strip() for line in data.strip().split('\n')]

test = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

test = [line.strip() for line in test.strip().split('\n')]

def build_dict(m):
    antennas = {}
    rows = len(m)
    cols = len(m[0])
    for y in range(rows):
            for x in range(cols):
                char = m[y][x]
                if char != '.': 
                    if char not in antennas:
                        antennas[char] = []
                    antennas[char].append((y,x))
    return antennas


# Part 1

def total_antinodes(matrix):
    antennas = build_dict(matrix)
    antinodes = set()
    for antenna in antennas:
        coords = antennas[antenna]
        for i in range(len(coords)):
            x, y = coords[i]
            for j in range(i + 1, len(coords)):
                x2, y2 = coords[j]
                dx, dy = x2 - x, y2 - y
                a1 = (x - dx, y - dy)
                a2 = (x2 + dx, y2 + dy)
                if 0 <= a1[0] < len(matrix) and 0 <= a1[1] < len(matrix):
                    if a1 not in antinodes:
                        antinodes.add(a1)
                if 0 <= a2[0] < len(matrix) and 0 <= a2[1] < len(matrix):
                    if a2 not in antinodes:
                        antinodes.add(a2)
    return len(antinodes)
        
                  
print(f'Part 1: {total_antinodes(m)}')

# Part 2
def total_antinodes2(matrix):
    antennas = build_dict(matrix)
    antinodes = set()
    for antenna in antennas:
        coords = antennas[antenna]
        for i in range(len(coords)):
            x, y = coords[i]
            antinodes.add((x, y))
            for j in range(i + 1, len(coords)):
                x2, y2 = coords[j]
                dx, dy = x2 - x, y2 - y

                nx, ny = x - dx, y - dy
                while 0 <= nx < len(matrix) and 0 <= ny < len(matrix):
                    antinodes.add((nx, ny))
                    nx -= dx
                    ny -= dy

                nx, ny = x2 + dx, y2 + dy
                while 0 <= nx < len(matrix) and 0 <= ny < len(matrix):
                    antinodes.add((nx, ny))
                    nx += dx
                    ny += dy
    return len(antinodes)

print(f'Part 2: {total_antinodes2(m)}')
