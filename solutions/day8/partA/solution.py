# -------------------------- GLOBAL CONSTANTS --------------------------

FILE_MODE_REAL_INPUT_MODE = True  # set to true to use problem input file 'input.txt', false for test file 'test.txt'

# -------------------------- PROGRAM DATA --------------------------

# open file for reading
with open('input.txt' if FILE_MODE_REAL_INPUT_MODE else 'test.txt', 'r') as f:
    lines = f.read().splitlines()


# generate 2d matrix of ints
tree_data = [list(map(int, list(line))) for line in lines]


# retrieve all trees above provided tree
def get_trees_above(i, j):
    return [tree_data[num][j] for num in range(i)]

# retrieve all trees below provided tree
def get_trees_below(i,j):
    return [tree_data[num][j] for num in range(i + 1, len(tree_data))]

# retrieve all trees to the left of the provided tree
def get_trees_left(i,j):
    return tree_data[i][:j]


# retrieve all trees above to the right of the provided tree
def get_trees_right(i, j):
    return tree_data[i][j+1:]


# all edge trees are visible
result = 2 * len(tree_data) + 2 * len(tree_data[0]) - 4


# process all inner trees
for x in range(1, len(tree_data) - 1):
    for y in range(1, len(tree_data[x]) - 1):

        # find largest tree on each possible path
        neighbours = [
            max(get_trees_left(x,y)),
            max(get_trees_right(x,y)),
            max(get_trees_above(x,y)),
            max(get_trees_below(x,y))
        ]

        # tree is visible
        if list(filter(lambda num: num < tree_data[x][y], neighbours)):
            result += 1

# print answer
print(result)