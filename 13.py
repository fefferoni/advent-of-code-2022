from pathlib import Path
from itertools import zip_longest
import functools

def get_input():
    path = Path(__file__).with_name('13.txt')
    with path.open('r') as f:
        return f.read()

def compare(first, second) -> bool:
    if isinstance(first, int) and isinstance(second, int):
        if first < second:
            return True
        if first > second:
            return False
        return None
    
    if isinstance(first, int):
        first = [first]
    if isinstance(second, int):
        second = [second]
    
    for f, s in zip_longest(first, second):
        if s == None:
            return False
        if f == None:
            return True
            
        val = compare(f, s)
        if val == True:
            return True
        if val == False:
            return False

def compare_revised(first, second) -> int:
    if isinstance(first, int) and isinstance(second, int):
        if first < second:
            return 1
        if first > second:
            return -1
        return 0
    
    if isinstance(first, int):
        first = [first]
    if isinstance(second, int):
        second = [second]
    
    for f, s in zip_longest(first, second):
        if s == None:
            return -1
        if f == None:
            return 1
            
        val = compare(f, s)
        if val == True:
            return 1
        if val == False:
            return -1

# PART ONE
input = get_input().split('\n\n')
data = [x.split() for x in input]
inp = [[eval(p) for p in x] for x in data]
sum = 0
for i, p in enumerate(inp):
    if compare(p[0], p[1]):
        sum += (i + 1)
print(f'Part one sum: {sum}')

# PART TWO
input2 = [l for l in get_input().split('\n') if l != '']
input2.extend(['[[2]]', '[[6]]'])
inp2 = [eval(p) for p in input2]
inp2 = sorted(inp2, key=functools.cmp_to_key(compare_revised), reverse=True)
decoder_key = (inp2.index([[2]]) + 1) * (inp2.index([[6]]) + 1)
print(decoder_key)