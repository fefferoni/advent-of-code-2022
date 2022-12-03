from pathlib import Path

path = Path(__file__).with_name('1.txt')

with path.open('r') as f:
    kcal_per_elf = [sum(c) for c in [[int(y) for y in x.split('\n')] for x in f.read().split('\n\n')]]
    max_kcal = max(kcal_per_elf)
    print(max_kcal)
    kcal_per_elf.sort(reverse = True)
    
    top_three_sum = sum(kcal_per_elf[:3])
    print(top_three_sum)
    