from pprint import pprint
from pathlib import Path
import math

class Monkey:
    def __init__(self, input):
        self.no_of_inspections = 0
        self.items = [int(m) for m in input[1][17:].strip().split(', ')]
        self.operation = input[2][19:]
        self.test_divisor = int(input[3].split()[-1])
        self.throwbuddies = (int(input[4].split()[-1]), int(input[5].split()[-1]))

    def operate(self, old):
        new = eval(self.operation)
        return new

    def inspect(self, monkeys, common_divisor):
        while len(self.items) > 0:
            self.no_of_inspections += 1
            item = self.items.pop(0)
            new = self.operate(item)
            new = new % common_divisor
            if new % self.test_divisor == 0:
                monkeys[self.throwbuddies[0]].receive(new)
            else:
                monkeys[self.throwbuddies[1]].receive(new)

    def receive(self, item):
        self.items.append(item)

def get_input():
    path = Path(__file__).with_name('11.txt')
    with path.open('r') as f:
        return f.read()

def print_items(monkeys):
    for i, m in enumerate(monkeys):
        print(f'monkey {i}: {",".join(str(x) for x in m.items)}')

# Parse input
data = get_input().split('\n\n')
monkeys = []
divisors = []

for m in data:
    lines = m.splitlines()
    mon = Monkey(lines)
    divisors.append(mon.test_divisor)
    monkeys.append(mon)

common_divisor = math.lcm(*divisors)

for i in range(10000):
    for m in monkeys:
        m.inspect(monkeys, common_divisor)

inspections = []
for i, m in enumerate(monkeys):
    print(f'Monkey {i} inspected {m.no_of_inspections} times')
    inspections.append(m.no_of_inspections)

inspections.sort(reverse=True)
pprint(inspections)
print(f'Part two solution: {inspections[0] * inspections[1]}')
