from pathlib import Path
import string

path = Path(__file__).with_name('3.txt')
partOneSum = 0
with path.open('r') as f:
    # PART ONE
    rows = f.read().split('\n')
    for row in rows:
        n = len(row)
        partOne = row[0:n//2]
        partTwo = row[n//2:]
        common = ''.join(set(partOne).intersection(partTwo))
        #print(common)
        if common.islower():
            #print(string.ascii_lowercase.index(common) + 1)
            partOneSum += (string.ascii_lowercase.index(common) + 1)
        else:
            #print(string.ascii_uppercase.index(common) + 27)
            partOneSum += (string.ascii_uppercase.index(common) + 27)
    print(partOneSum)

    # PART TWO
    start = 0
    end = len(rows)
    step = 3
    partTwoSum = 0
    for i in range(start, end, step):
        three_strings = rows[i:i + step]
        common = set.intersection(*map(set, three_strings)).pop()
        if common.islower():
            partTwoSum += (string.ascii_lowercase.index(common) + 1)
        else:
            partTwoSum += (string.ascii_uppercase.index(common) + 27)
    print(partTwoSum)

