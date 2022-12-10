from pathlib import Path

class FileSystem:
    def __init__(self) -> None:
        self.dirs = {"root" : Directory("root")}
        self.currentDir = "root"  
    def enter_dir(self, name):
        self.currentDir = self.currentDir + '/' + name
    def move_out_of_dir(self):
        self.currentDir = self.dirs[self.currentDir].parent
    def add_file(self, name, size):
        self.dirs[self.currentDir].add(File(name, size))
    def add_dir(self, name):
        self.dirs[self.currentDir + "/" + name] = Directory(name, self.currentDir)
    def build_tree(self):
        for k, dir in self.dirs.items():
            if dir.parent:
                fs.dirs[dir.parent].add(dir)
    def get_part_one_sum(self):
        partOneSum = 0
        for _,v in self.dirs.items():
            # print(f'{v.name} \t {v.get_size()}')
            size = v.get_size()
            if size <= 100000:
                partOneSum += size
        return partOneSum
    def get_part_two_dir_size(self):
        rootDirSize = fs.dirs["root"].get_size()
        freeSpace = 70000000 - rootDirSize
        spaceNeeded = 30000000 - freeSpace

        dir_sizes = []
        for _, dir in self.dirs.items():
            dir_sizes.append(dir.get_size())
        dir_sizes.sort()
        for s in dir_sizes:
            if s >= spaceNeeded:
                return s

class Content:
    def __init__(self, name):
        self.name = name
        
class Directory(Content):
    def __init__(self, name, parent = ''):
        if parent:
            super().__init__(parent + '/' + name)
        else:    
            super().__init__(name)
        self.contents = []
        self.parent = parent

    def add(self, fileOrDir):
        self.contents.append(fileOrDir)

    def get_size(self):
        size = 0
        for c in self.contents:
            size += c.get_size()
        return size

class File(Content):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size
    def get_size(self):
        return self.size

def is_file(row):
    return row[0].isnumeric()
def is_enter_dir_cmd(row):
    return row.startswith('$ cd') and not row.endswith('..')
def is_dir(row):
    return row.startswith('dir ')
def is_move_out_of_dir_cmd(row):
    return row == '$ cd ..'
def row_can_be_ignored(row):
    return row == '$ ls' or not row
def get_input():
    path = Path(__file__).with_name('7.txt')
    with path.open('r') as f:
        return f.read()

input = get_input()
rows = input.split('\n')
fs = FileSystem()
for row in rows[2:]:
    if row_can_be_ignored(row):
        continue
    if is_file(row):
        fileParts = row.split(' ')
        fs.add_file(fileParts[1], int(fileParts[0]))
    elif is_dir(row):
        fs.add_dir(row.split(' ')[1])
    elif is_enter_dir_cmd(row):
        fs.enter_dir(row.split(' ')[2])
    elif is_move_out_of_dir_cmd(row):
        fs.move_out_of_dir()

# PART ONE
fs.build_tree()
partOneSum = fs.get_part_one_sum()
print(partOneSum)

# PART TWO
smallestPossibleDir = fs.get_part_two_dir_size()
print(smallestPossibleDir)
