from pathlib import Path

scores_part1 = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6 
}

scores_part2 = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7 
}

path = Path(__file__).with_name('2.txt')
sum_part1 = 0
sum_part2 = 0
with path.open('r') as f:
    for row in f.read().split('\n'):
        sum_part1 += scores_part1[row]
        sum_part2 += scores_part2[row]
print(sum_part1)
print(sum_part2)