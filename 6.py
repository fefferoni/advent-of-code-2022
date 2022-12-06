from pathlib import Path

def GetInput():
    path = Path(__file__).with_name('6.txt')
    with path.open('r') as f:
        return f.read()

def all_unique(str):
    return len(set(str)) == len(str)

def print_start_marker(str, n):
    for i in range(len(str) - n + 1):
        batch = str[i:i + n]
        if all_unique(batch):
            print(i + n)
            print(batch)
            break


input = GetInput()

# PART ONE
batchSize = 4
print_start_marker(input, batchSize)

# PART TWO
batchSize = 14
print_start_marker(input, batchSize)