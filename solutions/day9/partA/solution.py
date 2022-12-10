# -------------------------- GLOBAL CONSTANTS --------------------------

FILE_MODE_REAL_INPUT_MODE = True      # set to true to use problem input file 'input.txt', false for test file 'test.txt'

# -------------------------- PROGRAM DATA --------------------------

# open file for reading
with open('input.txt' if FILE_MODE_REAL_INPUT_MODE else 'test.txt', 'r') as f:
    lines = f.read().splitlines()

# starting positions for rope head and tail
tail_pos = (0, 0)
head_pos = (0, 0)

# store all tail positions
tail_pos_set = {tail_pos}

def move_right(head, tail):
    # extract co-ordinates
    head_x, head_y = head
    tail_x, tail_y = tail

    # move tail according to head's position
    if head_is_top_right(head_x, head_y, tail_x, tail_y):
        tail_x += 1
        tail_y += 1
    elif head_is_right(head_x, head_y, tail_x, tail_y):
        tail_x += 1
    elif head_is_bottom_right(head_x, head_y, tail_x, tail_y):
        tail_x += 1
        tail_y -= 1

    # move head right
    head_x += 1

    # new head and tail positions
    return (head_x, head_y), (tail_x, tail_y)


def move_left(head, tail):
    # extract co-ordinates
    head_x, head_y = head
    tail_x, tail_y = tail

    # move tail according to head's position
    if head_is_top_left(head_x, head_y, tail_x, tail_y):
        tail_x -= 1
        tail_y += 1
    elif head_is_left(head_x, head_y, tail_x, tail_y):
        tail_x -= 1
    elif head_is_bottom_left(head_x, head_y, tail_x, tail_y):
        tail_x -= 1
        tail_y -= 1

    # move head right
    head_x -= 1

    # new head and tail positions
    return (head_x, head_y), (tail_x, tail_y)


def move_up(head, tail):
    # extract co-ordinates
    head_x, head_y = head
    tail_x, tail_y = tail

    # move tail according to head's position
    if head_is_top_left(head_x, head_y, tail_x, tail_y):
        tail_x -= 1
        tail_y += 1
    elif head_is_top(head_x, head_y, tail_x, tail_y):
        tail_y += 1
    elif head_is_top_right(head_x, head_y, tail_x, tail_y):
        tail_x += 1
        tail_y += 1

    # move head right
    head_y += 1

    # new head and tail positions
    return (head_x, head_y), (tail_x, tail_y)


def move_down(head, tail):
    # extract co-ordinates
    head_x, head_y = head
    tail_x, tail_y = tail

    # move tail according to head's position
    if head_is_bottom_left(head_x, head_y, tail_x, tail_y):
        tail_x -= 1
        tail_y -= 1
    elif head_is_bottom(head_x, head_y, tail_x, tail_y):
        tail_y -= 1
    elif head_is_bottom_right(head_x, head_y, tail_x, tail_y):
        tail_x += 1
        tail_y -= 1

    # move head right
    head_y -= 1

    # new head and tail positions
    return (head_x, head_y), (tail_x, tail_y)


def head_is_top_left(head_x, head_y, tail_x, tail_y):
    return head_x + 1 == tail_x and head_y - 1 == tail_y

def head_is_top(head_x, head_y, tail_x, tail_y):
    return head_x == tail_x and head_y - 1 == tail_y

def head_is_top_right(head_x, head_y, tail_x, tail_y):
    return head_x - 1 == tail_x and head_y - 1 == tail_y

def head_is_left(head_x, head_y, tail_x, tail_y):
    return head_x + 1 == tail_x and head_y == tail_y

def head_is_right(head_x, head_y, tail_x, tail_y):
    return head_x - 1 == tail_x and head_y == tail_y

def head_is_bottom_left(head_x, head_y, tail_x, tail_y):
    return head_x + 1 == tail_x and head_y + 1 == tail_y

def head_is_bottom(head_x, head_y, tail_x, tail_y):
    return head_x == tail_x and head_y + 1 == tail_y

def head_is_bottom_right(head_x, head_y, tail_x, tail_y):
    return head_x - 1 == tail_x and head_y + 1 == tail_y


def move_rope(head, tail, direction, amount):
    for _ in range(amount):
        head, tail = execute_move(head, tail, direction)

        # update seen tail positions
        tail_pos_set.add(tail)

    return head, tail

def execute_move(head, tail, direction):
    if direction == 'R':
        return move_right(head, tail)
    elif direction == 'L':
        return move_left(head, tail)
    elif direction == 'U':
        return move_up(head, tail)
    return move_down(head, tail)



# process all moves
for move in lines:
    # parse txt file
    tokens = move.split(" ")

    # move head
    head_pos, tail_pos = move_rope(head_pos, tail_pos, tokens[0], int(tokens[1]))


# get number of elements in set
result = len(tail_pos_set)

# print answer
print(result)