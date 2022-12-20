from pathlib import Path

def get_input():
    path = Path(__file__).with_name('10.txt')
    with path.open('r') as f:
        return f.read()

# PART ONE AND TWO 
data = get_input().splitlines()
x = 1
cycle = 1
i = 0
ongoing_cycle = True
n = 20
signal_sum = 0
pixel_pos = 0
while i < len(data):
    if (cycle - 20) % n == 0: # 20, 60, 100, 140, 180
        #print(f'1 cycle: {cycle} signal: {cycle * x} x: {x}')
        signal_sum += cycle * x
        n = 40

    if (cycle - 40) % 40 == 0:
        if pixel_pos == x or pixel_pos + 1 == x or pixel_pos -1 == x:
            print('#')
        else:
            print('.')
        pixel_pos = 0
    else:
        if pixel_pos == x or pixel_pos + 1 == x or pixel_pos -1 == x:
            print('#', end='')
        else:
            print('.', end='')
        pixel_pos += 1

    if data[i].startswith('noop'):
        i += 1
    else:
        if ongoing_cycle:
            ongoing_cycle = False
        else:
            v = int(data[i].split()[1])
            x += v
            i += 1
            ongoing_cycle = True
    cycle += 1
    
print(f'Signal strength sum: {signal_sum}')
