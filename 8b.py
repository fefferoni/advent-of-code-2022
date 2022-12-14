from pathlib import Path
# from pprint import pprint

def get_input():
    path = Path(__file__).with_name('8.txt')
    with path.open('r') as f:
        return f.read()    

def get_row_points(r, c):
    val = rows[r][c]
    leftPoints = 0
    rightPoints = 0
    index = c - 1
    
    while index >= 0:
        if val <= rows[r][index]:
            leftPoints += 1
            break    
        leftPoints += 1
        index += -1
    
    index = c + 1 
    while index < len:
        if val <= rows[r][index]:
            rightPoints += 1
            break
        rightPoints += 1
        index += 1
    
    if leftPoints == 0: 
        leftPoints = 1
    if rightPoints == 0:
        rightPoints = 1

    return leftPoints * rightPoints

def get_col_points(r, c):
    val = rows[r][c]
    abovePoints = 0
    belowPoints = 0
    index = r - 1

    while index >= 0:
        if val <= rows[index][c]:
            abovePoints += 1
            break    
        abovePoints += 1
        index += -1
    
    index = r + 1
    while index < len:
        if val <= rows[index][c]:
            belowPoints += 1
            break
        belowPoints += 1
        index += 1
    
    if abovePoints == 0: 
        abovePoints = 1
    if belowPoints == 0:
        belowPoints = 1

    return abovePoints * belowPoints

rows = [[int(i) for i in r] for r in get_input().splitlines()]
columns = list(map(list, zip(*rows)))
trees_around = len(rows) * 4 - 4
len = len(rows)

points_dict = {}
tree_points = []
for r in range(1, len - 1):
    for c in range(1, len - 1):
        scenic_points = get_row_points(r, c) * get_col_points(r, c)
        tree_points.append(scenic_points)

print(max(tree_points))