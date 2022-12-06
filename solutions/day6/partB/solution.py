# -------------------------- GLOBAL CONSTANTS --------------------------

FILE_MODE_REAL_INPUT_MODE = True  # set to true to use problem input file 'input.txt', false for test file 'test.txt'

# -------------------------- PROGRAM DATA --------------------------

# open file for reading
with open('input.txt' if FILE_MODE_REAL_INPUT_MODE else 'test.txt', 'r') as f:
    line = f.readline()


# number of characters seen before marker
result = 14

for i in range(len(line) - 13):
    if len(set(line[i:i+14])) == 14:
        break
    result += 1


# print result
print(result)