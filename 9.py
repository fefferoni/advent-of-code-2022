from pathlib import Path
from pprint import pprint

head = (0,0)

# PART ONE
tails = ([0, 0],)

# PART TWO
# tails = ([0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0])

no_of_tails = len(tails)
visited_pos = {"0,0"}

def get_input():
    path = Path(__file__).with_name('9.txt')
    with path.open('r') as f:
        return f.read()

def move(direction):
    if direction == 'R':
        move_head_right()
    elif direction == 'L':
        move_head_left()
    elif direction == 'U':
        move_head_up()
    elif direction == 'D':
        move_head_down()

    update_tail(head, tails[0])
    
    if no_of_tails > 1:
        for i in range(1, no_of_tails): # 1-8
            update_tail(tails[i - 1], tails[i])
            if i == no_of_tails - 1:
                visited_pos.add(f'{tails[i][0]},{tails[i][1]}')
    else:
        visited_pos.add(f'{tails[0][0]},{tails[0][1]}')

def update_tail(head, tail):
    if head[1] == tail[1]: # same x-axis
        if head[0] > tail[0]: # moved right
            if two_steps_away(head, tail):
                move_tail_right(tail)
        elif head[0] < tail[0]: # moved left
            if two_steps_away(head, tail):
                move_tail_left(tail)
    elif head[0] == tail[0]: # same y-axis
        if head[1] > tail[1]: # moved up
            if two_steps_away(head, tail):
                move_tail_up(tail)
        elif head[1] < tail[1]: # moved down
            if two_steps_away(head, tail):
                move_tail_down(tail)
    else:
        if head[0] > tail[0] and head[1] > tail[1]: # right up
            if two_steps_away(head, tail):
                move_tail_up_right(tail)
        elif head[0] > tail[0] and head[1] < tail[1]: # right down
            if two_steps_away(head, tail):
                move_tail_down_right(tail)
        elif head[0] < tail[0] and head[1] > tail[1]: #left up
            if two_steps_away(head, tail):
                move_tail_up_left(tail)
        elif head[0] < tail[0] and head[1] < tail[1]: #left down
            if two_steps_away(head, tail):
                move_tail_down_left(tail)

def two_steps_away(head, tail):
    return abs(head[0] - tail[0]) == 2 or abs(head[1] - tail[1]) == 2 

def move_head_right():
    global head
    head = (head[0] + 1, head[1])
def move_head_left():
    global head
    head = (head[0] - 1, head[1])
def move_head_up():
    global head 
    head = (head[0], head[1] + 1)
def move_head_down():
    global head 
    head = (head[0], head[1] - 1)
def move_tail_right(tail):
    tail[0] = tail[0] + 1
def move_tail_left(tail):
    tail[0] = tail[0] - 1
def move_tail_up(tail):
    tail[1] = tail[1] + 1
def move_tail_down(tail):
    tail[1] = tail[1] - 1
def move_tail_up_right(tail):
    tail[0] = tail[0] + 1
    tail[1] = tail[1] + 1
def move_tail_down_right(tail):
    tail[0] = tail[0] + 1
    tail[1] = tail[1] - 1
def move_tail_up_left(tail):
    tail[0] = tail[0] - 1
    tail[1] = tail[1] + 1
def move_tail_down_left(tail):
    tail[0] = tail[0] - 1
    tail[1] = tail[1] - 1

for d, s in [line.split() for line in get_input().splitlines()]:
    for i in range(int(s)):
        move(d)

# pprint(visited_pos)
print(len(visited_pos))
