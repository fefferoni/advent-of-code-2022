from pathlib import Path
# from pprint import pprint

def get_input():
    path = Path(__file__).with_name('8.txt')
    with path.open('r') as f:
        return f.read()

rows = [[int(i) for i in r] for r in get_input().splitlines()]
columns = list(map(list, zip(*rows)))
trees_around = len(rows) * 4 - 4

rowcount = len(rows)
colcount = len(rows[0])

visible_trees = set()
for i in range(1, len(rows) - 1):
    index = i
    for c in range(1, len(rows) - 1):
        inner_index = c        
        row_val = rows[index][inner_index]
        col_val = columns[index][inner_index]
        
        trees_before = rows[index][:inner_index]
        if all(x < row_val for x in trees_before):
            visible_trees.add(f'{index},{inner_index}')
        
        trees_after = rows[index][inner_index+1:]
        if all(x < row_val for x in trees_after):
            visible_trees.add(f'{index},{inner_index}')

        trees_above = columns[index][:inner_index]
        if all(x < col_val for x in trees_above):
            visible_trees.add(f'{inner_index},{index}')

        trees_below = columns[index][inner_index+1:]
        if all(x < col_val for x in trees_below):
            visible_trees.add(f'{inner_index},{index}')

total_trees = len(visible_trees) + trees_around
print(len(visible_trees))
print(total_trees)