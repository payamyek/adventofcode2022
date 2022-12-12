# -------------------------- GLOBAL CONSTANTS --------------------------

FILE_MODE_REAL_INPUT_MODE = True  # set to true to use problem input file 'input.txt', false for test file 'test.txt'

 # constants for knot moving directions
UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'

X_CORD = 0
Y_CORD = 1

# -------------------------- PROGRAM DATA --------------------------

# open file for reading
with open('input.txt' if FILE_MODE_REAL_INPUT_MODE else 'test.txt', 'r') as f:
    lines = f.read().splitlines()

# store location of ten knots
head = [0, 0]
tail = [0, 0]

# store all tail positions
seen = {tuple(tail)}


# ---------------------------- HELPER LAMBDA FUNCTIONS ----------------------------

is_head_two_right = lambda: head[X_CORD] - tail[X_CORD] == 2 and head[Y_CORD] == tail[Y_CORD]

is_head_two_left = lambda: tail[X_CORD] - head[X_CORD] == 2  and head[Y_CORD] == tail[Y_CORD]

is_head_two_up = lambda: head[Y_CORD] - tail[Y_CORD] == 2 and head[X_CORD] == tail[X_CORD]

is_head_two_down = lambda: tail[Y_CORD] - head[Y_CORD] == 2 and head[X_CORD] == tail[X_CORD]

is_head_up_right = lambda: (head[Y_CORD] - tail[Y_CORD] == 2 and head[X_CORD] - tail[X_CORD] == 1) or (head[Y_CORD] - tail[Y_CORD] == 1 and head[X_CORD] - tail[X_CORD] == 2)

is_head_up_left = lambda: (head[Y_CORD] - tail[Y_CORD] == 2 and tail[X_CORD] - head[X_CORD] == 1) or (head[Y_CORD] - tail[Y_CORD] == 1 and tail[X_CORD] - head[X_CORD] == 2)

is_head_down_left = lambda: (tail[Y_CORD] - head[Y_CORD] == 2 and tail[X_CORD] - head[X_CORD] == 1) or (tail[Y_CORD] - head[Y_CORD] == 1 and tail[X_CORD] - head[X_CORD] == 2)

is_head_down_right = lambda: (tail[Y_CORD] - head[Y_CORD] == 2 and head[X_CORD] - tail[X_CORD] == 1) or (tail[Y_CORD] - head[Y_CORD] == 1 and head[X_CORD] - tail[X_CORD] == 2)


# determines which move needs to be made
def move_handler(direction, units):
    if direction == UP:
        move_head_up(units)
    elif direction == DOWN:
        move_head_down(units)
    elif direction == LEFT:
        move_head_left(units)
    elif direction == RIGHT:
        move_head_right(units)


# moves head up
def move_head_up(units):
    for _ in range(units):
        head[Y_CORD] += 1
        update_tail_position()

# moves head down
def move_head_down(units):
    for _ in range(units):
        head[Y_CORD] -= 1
        update_tail_position()


# moves head left
def move_head_left(units):
    for _ in range(units):
        head[X_CORD] -= 1
        update_tail_position()


# moves head right
def move_head_right(units):
    for _ in range(units):
        head[X_CORD] += 1
        update_tail_position()



# after head moves, update location of tail
def update_tail_position():
    if is_head_two_right(): # move tail right
        tail[X_CORD] += 1
    elif is_head_two_left(): # move tail left
        tail[X_CORD] -= 1
    elif is_head_two_up(): # move tail up
        tail[Y_CORD] += 1
    elif is_head_two_down(): # move tail down
        tail[Y_CORD] -= 1
    elif is_head_up_right():
        tail[X_CORD] += 1
        tail[Y_CORD] += 1
    elif is_head_up_left():
        tail[X_CORD] -= 1
        tail[Y_CORD] += 1
    elif is_head_down_left():
        tail[X_CORD] -= 1
        tail[Y_CORD] -= 1
    elif is_head_down_right():
        tail[X_CORD] += 1
        tail[Y_CORD] -= 1

    # record new tail position
    seen.add(tuple(tail))


for line in lines:
    tokens = line.split(" ")

    # make moves
    move_handler(tokens[0], int(tokens[1]))

print(len(seen))