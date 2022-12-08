# -------------------------- GLOBAL CONSTANTS --------------------------

FILE_MODE_REAL_INPUT_MODE = True  # set to true to use problem input file 'input.txt', false for test file 'test.txt'

TOTAL_AVAILABLE_SPACE = 70000000

TOTAL_REQUIRED_SPACE = 30000000

# -------------------------- PROGRAM DATA --------------------------

# open file for reading
with open('input.txt' if FILE_MODE_REAL_INPUT_MODE else 'test.txt', 'r') as f:
    lines = f.read().splitlines()

def get_parent(path):
    if path.count('/') == 1:
        return '/'

    index = path[:len(path) - 1].rindex('/')
    return path[:index + 1]

def safe_dict_update (dict_obj, key, value):
    if dict_obj.get(key) is None:
        directory_dict[key] = value
    else:
        directory_dict[key] += value


# store absolute paths for all files
files_dict = dict()

# current working directory
cwd = ''

# process file input
for line in lines:
    tokens = line.split(' ')

    if '$' in line and 'cd' in line and tokens[2] == '/':
        cwd = '/'
    elif '$' in line and 'cd' in line and tokens[2] == '..':
        cwd = get_parent(cwd)
    elif '$' in line and 'cd' in line:
        cwd = f"{cwd}{tokens[2]}/"
    elif '$' not in line and 'dir' not in line:
        file_path = f"{cwd}{tokens[1]}"
        files_dict[file_path] = int(tokens[0])


# define custom class comparison function
class CustomerComparator(tuple):
    def __lt__(self, other):
        return self[0].count('/') > other[0].count('/')

# store total size of each dict
directory_dict = dict()

# sort files by nestation level
files = sorted(files_dict.items(), key=CustomerComparator)

def cascade_size_changes(path_name, size):
    parent_path = get_parent(path_name)

    while parent_path != '/':
        safe_dict_update(directory_dict, parent_path, size)
        parent_path = get_parent(parent_path)

    # update root directory size
    safe_dict_update(directory_dict, '/', size)

# calculate sizes of each directory
for k, v in files:
    cascade_size_changes(k, v)

# store all directories that will free up enough space
candidates_for_removal = []

# current unused space
unused_space = TOTAL_AVAILABLE_SPACE - directory_dict["/"]

for v in directory_dict.values():
    if v + unused_space >= TOTAL_REQUIRED_SPACE:
        candidates_for_removal.append(v)

# answer is the min amongst all candidates
result = min(candidates_for_removal)

# print answer
print(result)