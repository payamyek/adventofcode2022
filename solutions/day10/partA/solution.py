# -------------------------- GLOBAL CONSTANTS --------------------------

FILE_MODE_REAL_INPUT_MODE = True  # set to true to use problem input file 'input.txt', false for test file 'test.txt'

# -------------------------- PROGRAM DATA --------------------------

# open file for reading
with open('input.txt' if FILE_MODE_REAL_INPUT_MODE else 'test.txt', 'r') as f:
    lines = f.read().splitlines()


total_cycles = 1
register_contents = 1

snapshots = []


def check_snapshot():
    # check if at any of these intervals
    if total_cycles in [20, 60, 100, 140, 180, 220]:
        snapshots.append(total_cycles * register_contents)


for line in lines:
    if line == 'noop':
        total_cycles += 1
        check_snapshot()
        continue

    # extract value
    value = int(line.split(" ")[1])

    # go to next cycle
    total_cycles += 1

    # check if we need to update snapshots
    check_snapshot()

    # go to next cycle
    total_cycles += 1

    # update register contents
    register_contents += value

    # check if we need to update snapshots
    check_snapshot()


# sum all snapshots
result = sum(snapshots)

# print answer
print(result)


