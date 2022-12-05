from pathlib import Path

def GetRowsFromFile():
    path = Path(__file__).with_name('5.txt')
    with path.open('r') as f:
        return f.read().split('\n')

stacks = [ 
    ['T', 'R', 'D', 'H', 'Q', 'N', 'P', 'B'][::-1], 
    ['V', 'T', 'J', 'B', 'G', 'W'][::-1], 
    ['Q', 'M', 'V', 'S', 'D', 'H', 'R', 'N'][::-1],
    ['C', 'M', 'N', 'Z', 'P'][::-1],
    ['B', 'Z', 'D'][::-1],
    ['Z', 'W', 'C', 'V'][::-1],
    ['S', 'L', 'Q', 'V', 'C', 'N', 'Z', 'G'][::-1],
    ['V', 'N', 'D', 'M', 'J', 'G', 'L'][::-1],
    ['G', 'C', 'Z', 'F', 'M', 'P', 'T'][::-1]
    ]

for row in GetRowsFromFile()[10:]:
    parts = row.split(' ')
    qty = int(parts[1])
    source = int(parts[3]) - 1
    dest = int(parts[5]) - 1
    stacks[dest].extend(stacks[source][-qty:][::-1]) # remove [::-1] to complete PART TWO
    size = len(stacks[source])
    stacks[source] = stacks[source][:size - qty]

msg = ''
for stack in stacks:
    msg += stack.pop()
print(msg)
