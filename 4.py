from pathlib import Path

def GetRowsFromFile():
    path = Path(__file__).with_name('4.txt')
    with path.open('r') as f:
        return f.read().split('\n')

def first_range_within_second(a0, a1, b0, b1):
    return a0 >= b0 and a1 <= b1

def second_range_within_first(a0, a1, b0, b1):
    return b0 >= a0 and b1 <= a1

def first_range_overlaps_second(a0, a1, b0, b1):
    return (a0 >= b0 and a0 <= b1) or (a1 >= b0 and a1 <= b1)

def second_range_overlaps_first(a0, a1, b0, b1):
    return (b0 >= a0 and b0 <= a1) or (b1 >= a0 and b1 <= a1)

partOneSum = 0
partTwoSum = 0
rows = GetRowsFromFile()

for row in rows:
    parts = row.split(',')
    a = parts[0].split('-')
    b = parts[1].split('-')

    a0 = int(a[0])
    a1 = int(a[1])
    b0 = int(b[0])
    b1 = int(b[1])

    if first_range_within_second(a0, a1, b0, b1):
        partOneSum += 1
    elif second_range_within_first(a0, a1, b0, b1):
        partOneSum += 1

    if first_range_overlaps_second(a0, a1, b0, b1):
        partTwoSum += 1
    elif second_range_overlaps_first(a0, a1, b0, b1):
        partTwoSum += 1

print(f'Sum first part: {partOneSum}')
print(f'Sum second part: {partTwoSum}')