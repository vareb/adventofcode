from aocd import data


reports = [list(map(int, line.split())) for line in data.strip().split('\n')]

# Part 1
def check_safe(report):
    if all(report[k] < report[k+1] for k in range(len(report) - 1)) or all(report[k] > report[k+1] for k in range(len(report) - 1)):
        for n in range(0, len(report) - 1):
            change = abs(report[n] - report[n+1])
            if change > 3 or change < 1:
                break
        else: #if loop dont break
            return True
    return False

safe = 0
for report in reports:
    if check_safe(report):
        safe += 1
print(f'Part 1: {safe}')

# Part 2
safe2 = 0
for report in reports:
    if not check_safe(report):
        k = 0
        while k < len(report):
            removed = report.pop(k)
            if not check_safe(report):
                report.insert(k, removed) 
            else:
                safe2 += 1
                break
            k += 1
    else:
        safe2 += 1
print(f'Part 2: {safe2}')

    