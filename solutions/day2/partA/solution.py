# -------------------------- GLOBAL CONSTANTS --------------------------

FILE_MODE_REAL_INPUT_MODE = True  # set to true to use problem input file 'input.txt', false for test file 'test.txt'

# points won depending on the game's result
GAME_RESULT_LOST_POINTS = 0
GAME_RESULT_DRAW_POINTS = 3
GAME_RESULT_WIN_POINTS = 6

# constants for move types
ROCK_P1 = 'A'
PAPER_P1 = 'B'
SCISSORS_P1 = 'C'

ROCK_P2 = 'X'
PAPER_P2 = 'Y'
SCISSORS_P2 = 'Z'

# points each move grants
MOVE_POINTS = {
    ROCK_P1: 1,
    PAPER_P1: 2,
    SCISSORS_P1: 3,
    ROCK_P2: 1,
    PAPER_P2: 2,
    SCISSORS_P2: 3,
}

# -------------------------- PROGRAM DATA --------------------------

# open file for reading
with open('input.txt' if FILE_MODE_REAL_INPUT_MODE else 'test.txt', 'r') as f:
    lines = f.read().splitlines()
    moves = [tuple(line.split(" ")) for line in lines]


# given player one and player two's moves calculate points player two receives
def points(p1_move, p2_move):
    # brute force all possible move combinations
    if MOVE_POINTS[p1_move] == MOVE_POINTS[p2_move]:  # same move if both moves carry the same amount of points
        return MOVE_POINTS[p2_move] + GAME_RESULT_DRAW_POINTS
    elif p1_move == ROCK_P1 and p2_move == SCISSORS_P2:
        return MOVE_POINTS[p2_move] + GAME_RESULT_LOST_POINTS
    elif p1_move == PAPER_P1 and p2_move == ROCK_P2:
        return MOVE_POINTS[p2_move] + GAME_RESULT_LOST_POINTS
    elif p1_move == SCISSORS_P1 and p2_move == PAPER_P2:
        return MOVE_POINTS[p2_move] + GAME_RESULT_LOST_POINTS
    elif p1_move == ROCK_P1 and p2_move == PAPER_P2:
        return MOVE_POINTS[p2_move] + GAME_RESULT_WIN_POINTS
    elif p1_move == PAPER_P1 and p2_move == SCISSORS_P2:
        return MOVE_POINTS[p2_move] + GAME_RESULT_WIN_POINTS
    elif p1_move == SCISSORS_P1 and p2_move == ROCK_P2:
        return MOVE_POINTS[p2_move] + GAME_RESULT_WIN_POINTS
    return 0


# calculate total points
total_points = sum([points(p1_move, p2_move) for p1_move, p2_move in moves])

# print results
print(total_points)
