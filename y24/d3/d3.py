from aocd import data


def mul(n1, n2):
    return int(n1) * int(n2)


# Part 1

sum = 0
for k in range(len(data)-3):
    word = data[k] + data[k+1] + data[k+2] + data[k+3]
    if word == "mul(":
        found_comma = False
        comma_index = 0
        nr1 = 0
        nr2 = 0
        for c in range(k+4, len(data)):
            char = data[c]
            if not char.isnumeric():
                if char == ',':
                    if found_comma:
                        break
                    found_comma = True
                    comma_index = c
                    nr1 = data[k+4:c]
                elif char == ')':
                    if comma_index+1 != c:
                        nr2 = data[comma_index+1:c]
                        sum += mul(nr1, nr2)
                        break
                    else:
                        break
                else: 
                    break
print(f'Part 1: {sum}')


# Part 2
sum = 0
status = True
for k in range(len(data)-6):
    word = data[k] + data[k+1] + data[k+2] + data[k+3]
    checkdo = data[k] + data[k+1] + data[k+2] + data[k+3]
    checkdont = data[k] + data[k+1] + data[k+2] + data[k+3] + data[k+4] + data[k+5] + data[k+6]
    if checkdo == "do()":
        status = True
    if checkdont == "don't()":
        status = False
    if word == "mul(" and status:
        found_comma = False
        comma_index = 0
        nr1 = 0
        nr2 = 0
        for c in range(k+4, len(data)):
            char = data[c]
            if not char.isnumeric():
                if char == ',':
                    if found_comma:
                        break
                    found_comma = True
                    comma_index = c
                    nr1 = data[k+4:c]
                elif char == ')':
                    if comma_index+1 != c:
                        nr2 = data[comma_index+1:c]
                        sum += mul(nr1, nr2)
                        break
                    else:
                        break
                else: 
                    break
print(f'Part 2: {sum}')
    
                
                        

                


