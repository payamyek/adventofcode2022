# -------------------------- GLOBAL CONSTANTS --------------------------

FILE_MODE_REAL_INPUT_MODE = True  # set to true to use problem input file 'input.txt', false for test file 'test.txt'

# -------------------------- PROGRAM DATA --------------------------

# open file for reading
with open('input.txt' if FILE_MODE_REAL_INPUT_MODE else 'test.txt', 'r') as f:
    lines = f.read().splitlines()


# generate 2d matrix of ints
tree_data = [list(map(int, list(line))) for line in lines]


# helper function to compute visibility distance for trees starting at i,j
def compute_vd(trees, i, j):
    vd = 0
    for num in trees:
        vd += 1
        if num >= tree_data[i][j]:
            break
    return vd

# compute visibility distance for i,j in the above direction
def vd_above(i, j):
    trees = [tree_data[num][j] for num in range(i)][::-1]
    return compute_vd(trees, i, j)

# compute visibility distance for i,j in the below direction
def vd_below(i, j):
    trees = [tree_data[num][j] for num in range(i+1, len(tree_data))]
    return compute_vd(trees, i, j)

# compute visibility distance for i,j in the left direction
def vd_left(i, j):
    trees = tree_data[i][:j][::-1]
    return compute_vd(trees, i, j)

# compute visibility distance for i,j in the right direction
def vd_right(i, j):
    trees = tree_data[i][j+1:]
    return compute_vd(trees, i, j)


# compute visibility distances for inner trees
vds = [
    vd_left(x,y) * vd_right(x,y) * vd_above(x,y) * vd_below(x,y)
    for x in range (1, len(tree_data) - 1)
    for y in range(1, len(tree_data[x]) - 1)
]

# max viewing distance
result = max(vds)

# print answer
print(result)