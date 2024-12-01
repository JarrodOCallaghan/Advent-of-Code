class Directory: 
    def __init__(self, name, parent_dir = None) -> None:
        self.files = {}
        self.sub_dir = {}
        self.size = 0
        self.parent_dir = parent_dir
        self.name = name
        self.sub_sum = 0

    def add_sub_dir(self, dir):
        self.sub_dir[dir.name] = dir

    def add_file(self, file):
        self.files[file.name] = file
        self.size += file.get_size()
    
    def get_size(self):
        return self.size

    def print_all(self):
        print(f'PWD: {self.name}, size: {self.get_size()}')
        for file in self.files.values():
            print(f'{file.get_size()} {file.get_name()}')
        for dir in self.sub_dir:
            print("dir " + dir + " Size: ")
        for sub in self.sub_dir.values():
            sub.print_all()

    # def set_size_recursive(self):
    #     current_size = 0
    #     for size in self.files.values():
    #         current_size += size.get_size()
    #     # sub_size = 0
    #     if self.sub_dir.values() != None:
    #         for sub in self.sub_dir.values():
    #             current_size += sub.set_size_recursive()
    #     self.size = current_size

    def get_this_child_total_size(self):
        size = self.size
        for dir in self.sub_dir.values():
            size += dir.get_this_child_total_size()
        self.size = size
        return size

    def ls(self):
        print(f'{self.size}, {self.name}')
        for dir in self.sub_dir.values():
            dir.ls()

    def get_lt_100000(self):
        if(self.size <= 100000):
            size = self.size
        else:
            size = 0
        for dir in self.sub_dir.values():
            size += dir.get_lt_100000()
        self.size = size
        return size

class file:
    def __init__(self, size, name) -> None:
        self.size = size
        self.name = name
    
    def get_size(self):
        return self.size
    
    def get_name(self):
        return self.name


f = open("dataset.txt", "r")
raw_data = f.readlines()
data = []
root = Directory("/")
current_dir = root
total_size = 0
# We probs dont need to save the log
for line in raw_data:
    line = line.strip()
    if (line.__contains__('$')):
        if (line == "$ cd /"):
            current_dir = root
        elif (line == "$ cd .."):
            current_dir = current_dir.parent_dir
        elif (line == "$ ls"):
            pass
        else:
            dir_name = line.replace("$ cd ","")
            # print(f'CD Info: {dir_name}')
            if (dir_name not in current_dir.sub_dir):
                new_dir = Directory(dir_name, current_dir)
                current_dir.add_sub_dir(new_dir)
            # print(current_dir.sub_dir)
            current_dir = current_dir.sub_dir[dir_name]
        pass
    else:
        inf, name = line.split(" ")
        if(inf == "dir"):
            if (name not in current_dir.sub_dir):
                new_dir = Directory(name, current_dir)
                current_dir.add_sub_dir(new_dir)
        else:
            # Aka file
            if (name not in current_dir.files):
                new_file = file(int(inf), name)
                current_dir.add_file(new_file)
        # Is File
    # data.append(line)
# TODO:
# Reconstruct the Dir
# 
# print(root.get_this_child_total_size())
# root.print_all()
root.get_this_child_total_size()
sum = 0
# root.get_size_lt_100000()
print(root.get_lt_100000())

# Cheat the thingy
    

# print(data)
f.close()