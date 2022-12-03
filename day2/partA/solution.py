# -------------------------- GLOBAL CONSTANTS --------------------------

FILE_MODE_REAL_INPUT_MODE = True  # set to true to use problem input file 'input.txt', false for test file 'test.txt'

# points won depending on the game's result
GAME_RESULT_POINTS_LOSS = 0
GAME_RESULT_POINTS_DRAW = 3
GAME_RESULT_POINTS_WIN = 6

# player moves as keys and values as points (also used to uniquely identify type of moves, ex. 3 is a rock mvoe)
MOVE = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

ROCK = 1
PAPER = 2
SCISSORS = 3

# -------------------------- PROGRAM DATA --------------------------

# open file for reading
with open('input.txt' if FILE_MODE_REAL_INPUT_MODE else 'test.txt', 'r') as f:
    lines = f.readlines()
    moves = [tuple(line.strip().split(" ")) for line in lines]


# given player one and player two's moves it calculates the total points player two receives
def points(p1_move, p2_move):
    result = 0

    # brute force all possible move combinations
    if MOVE[p1_move] == MOVE[p2_move]:
        result = MOVE[p2_move] + GAME_RESULT_POINTS_DRAW
    elif MOVE[p1_move] == ROCK and MOVE[p2_move] == SCISSORS:
        result = MOVE[p2_move] + GAME_RESULT_POINTS_LOSS
    elif MOVE[p1_move] == PAPER and MOVE[p2_move] == ROCK:
        result = MOVE[p2_move] + GAME_RESULT_POINTS_LOSS
    elif MOVE[p1_move] == SCISSORS and MOVE[p2_move] == PAPER:
        result = MOVE[p2_move] + GAME_RESULT_POINTS_LOSS
    elif MOVE[p1_move] == ROCK and MOVE[p2_move] == PAPER:
        result = MOVE[p2_move] + GAME_RESULT_POINTS_WIN
    elif MOVE[p1_move] == PAPER and MOVE[p2_move] == SCISSORS:
        result = MOVE[p2_move] + GAME_RESULT_POINTS_WIN
    elif MOVE[p1_move] == SCISSORS and MOVE[p2_move] == ROCK:
        result = MOVE[p2_move] + GAME_RESULT_POINTS_WIN
    return result


# calculate total points
total_points = sum([points(p1_move, p2_move) for p1_move, p2_move in moves])

# print results
print(total_points)
