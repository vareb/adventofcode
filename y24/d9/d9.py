from aocd import data

test = "12345"

test2= "2333133121414131402"

# Part 1

def build_list(data):
    list = []
    id = 0
    for index, num in enumerate(data):
        num = int(num)
        if index % 2 == 0:
            for i in range(num):
                list.append(id)
            id += 1
        else:
            for i in range(num):
                list.append(-1)
    return list

def swap_blocks(data):
    list = build_list(data)
    
    left = 0
    right = len(list) - 1 
    
    while left < right:
        while left < right and list[left] != -1:
            left += 1
        
        while left < right and list[right] == -1:
            right -= 1

        if left < right:
            list[left], list[right] = list[right], list[left]
            left += 1
            right -= 1

    list = list[:left] # remove free space
    
    return list

def check_sum(data):
    list = swap_blocks(data)
    sum = 0

    for index, n in enumerate(list):
        sum += index * n

    return sum

print(f'Part 1: {check_sum(data)}')

# Part 2
def swap_files(data):
    data_list = build_list(data)
    files = []
    empty = []

    pointer = 0
    while pointer < len(data_list):
        number = data_list[pointer]
        start = pointer
        while pointer < len(data_list) and data_list[pointer] == number:
            pointer += 1
        if number == -1:
            empty.append((start, pointer - 1))
        else:
            files.append((start, pointer - 1))
    files.reverse()

    for x, y in files:
        for index, (a, b) in enumerate(empty):
            if x > b:
                file_size = y - x + 1
                empty_size = b - a + 1
                if file_size <= empty_size:
                   
                    temp = data_list[x:y+1]
                    data_list[x:y+1] = data_list[a:a+file_size]
                    data_list[a:a+file_size] = temp

                    if file_size == empty_size:
                        del empty[index]
                    else:
                        empty[index] = (a + file_size, b)
                    break

    return data_list


def check_sum2(data):
    list = swap_files(data)
    sum = 0

    for index, n in enumerate(list):
        if n != -1:
            sum += index * n

    return sum

print(f'Part 2: {check_sum2(data)}')