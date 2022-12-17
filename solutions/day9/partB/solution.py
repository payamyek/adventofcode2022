# -------------------------- GLOBAL CONSTANTS --------------------------

FILE_MODE_REAL_INPUT_MODE = True  # set to true to use problem input file 'input.txt', false for test file 'test.txt'

# constants for knot moving directions
UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'

X_CORD = 0
Y_CORD = 1

NUM_OF_KNOTS = 10

# -------------------------- PROGRAM DATA --------------------------

# open file for reading
with open('input.txt' if FILE_MODE_REAL_INPUT_MODE else 'test.txt', 'r') as f:
    lines = f.read().splitlines()

# store location of ten knots
knots = [[0, 0] for _ in range(NUM_OF_KNOTS)]

# store all tail positions
seen = {tuple([0, 0])}

# ---------------------------- HELPER LAMBDA FUNCTIONS ----------------------------

is_head_two_right = lambda head, tail: head[X_CORD] - tail[X_CORD] == 2 and head[Y_CORD] == tail[Y_CORD]

is_head_two_left = lambda head, tail: tail[X_CORD] - head[X_CORD] == 2  and head[Y_CORD] == tail[Y_CORD]

is_head_two_up = lambda head, tail: head[Y_CORD] - tail[Y_CORD] == 2 and head[X_CORD] == tail[X_CORD]

is_head_two_down = lambda head, tail: tail[Y_CORD] - head[Y_CORD] == 2 and head[X_CORD] == tail[X_CORD]

is_head_up_right = lambda head, tail: (head[Y_CORD] - tail[Y_CORD] == 2 and head[X_CORD] - tail[X_CORD] == 2) or (head[Y_CORD] - tail[Y_CORD] == 2 and head[X_CORD] - tail[X_CORD] == 1) or (head[Y_CORD] - tail[Y_CORD] == 1 and head[X_CORD] - tail[X_CORD] == 2)

is_head_up_left = lambda head, tail: (head[Y_CORD] - tail[Y_CORD] == 2 and tail[X_CORD] - head[X_CORD] == 2)  or (head[Y_CORD] - tail[Y_CORD] == 2 and tail[X_CORD] - head[X_CORD] == 1) or (head[Y_CORD] - tail[Y_CORD] == 1 and tail[X_CORD] - head[X_CORD] == 2)

is_head_down_left = lambda head, tail: (tail[Y_CORD] - head[Y_CORD] == 2 and tail[X_CORD] - head[X_CORD] == 2)  or (tail[Y_CORD] - head[Y_CORD] == 2 and tail[X_CORD] - head[X_CORD] == 1) or (tail[Y_CORD] - head[Y_CORD] == 1 and tail[X_CORD] - head[X_CORD] == 2)

is_head_down_right = lambda head, tail: (tail[Y_CORD] - head[Y_CORD] == 2 and head[X_CORD] - tail[X_CORD] == 2) or (tail[Y_CORD] - head[Y_CORD] == 2 and head[X_CORD] - tail[X_CORD] == 1) or (tail[Y_CORD] - head[Y_CORD] == 1 and head[X_CORD] - tail[X_CORD] == 2)


# determines which move needs to be made
def move_handler(direction, units):
    # process move individually so changes can be cascaded properly
    for _ in range(units):

        # go through all knots
        for i in range(NUM_OF_KNOTS - 1, 0, -1):
            head, tail = knots[i], knots[i-1]

            move_head = i == NUM_OF_KNOTS - 1
            tail_moved = i == 1

            if direction == UP:
                move_head_up(head, tail, 1, move_head, tail_moved)
            elif direction == DOWN:
                move_head_down(head, tail, 1, move_head, tail_moved)
            elif direction == LEFT:
                move_head_left(head, tail, 1, move_head, tail_moved)
            elif direction == RIGHT:
                move_head_right(head, tail, 1, move_head, tail_moved)


# moves head up
def move_head_up(head, tail, units, move_head, tail_moved):
    for _ in range(units):
        if move_head:
            head[Y_CORD] += 1
        update_tail_position(head, tail, tail_moved)

# moves head down
def move_head_down(head, tail, units, move_head, tail_moved):
    for _ in range(units):
        if move_head:
            head[Y_CORD] -= 1
        update_tail_position(head, tail, tail_moved)


# moves head left
def move_head_left(head, tail, units, move_head, tail_moved):
    for _ in range(units):
        if move_head:
            head[X_CORD] -= 1
        update_tail_position(head, tail, tail_moved)


# moves head right
def move_head_right(head, tail, units, move_head, tail_moved):
    for _ in range(units):
        if move_head:
            head[X_CORD] += 1
        update_tail_position(head, tail, tail_moved)


# after head moves, update location of tail
def update_tail_position(head, tail, tail_moved):
    if is_head_two_right(head, tail): # move tail right
        tail[X_CORD] += 1
    elif is_head_two_left(head, tail): # move tail left
        tail[X_CORD] -= 1
    elif is_head_two_up(head, tail): # move tail up
        tail[Y_CORD] += 1
    elif is_head_two_down(head, tail): # move tail down
        tail[Y_CORD] -= 1
    elif is_head_up_right(head, tail):
        tail[X_CORD] += 1
        tail[Y_CORD] += 1
    elif is_head_up_left(head, tail):
        tail[X_CORD] -= 1
        tail[Y_CORD] += 1
    elif is_head_down_left(head, tail):
        tail[X_CORD] -= 1
        tail[Y_CORD] -= 1
    elif is_head_down_right(head, tail):
        tail[X_CORD] += 1
        tail[Y_CORD] -= 1

    # record new tail position
    if tail_moved:
        seen.add(tuple(tail))


for line in lines:
    tokens = line.split(" ")

    # make moves
    move_handler(tokens[0], int(tokens[1]))


print(len(seen))