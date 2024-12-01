f = open("dataset.txt", "r")
raw_data = f.readlines()
data = []
for line in raw_data:
    data.append([*line.strip()])

width = len(data[0])
height = len(data)
print(f'Width: {width}, height: {height}')
for y in data:
    for x in y:
        print(x, end="")
    print("\n")


hor = range(0,width)
vert = range(0, height)

def is_tree_visible(current, next):
    current = int(current)
    next = int(next)
    if next == None:
        return False
    if next > current:
        return True
    else:
        return False


visable_list = []
# Test top first:
tree_counter = 0
current = None
for x in range(width):
    print("New Row:")
    for y in range(height):
        tree = data[y][x]
        # print(tree)
        if current == None:
            current = tree
            tree_counter += 1
            new_str = str(x) + "/" + str(y)
            print(str(new_str))
            visable_list.append(new_str)
            print(f'+1, current {current}, First in row')
        if tree > current:
            current = tree
            tree_counter += 1
            new_str = str(x) + "/" + str(y)
            visable_list.append(new_str)
            print(f'+1, current {current}, next {tree}')
    current = None

# Bottom Row:
print("Bottom Up")
current = None
for x in reversed(range(width)):
    print("New Row:")
    for y in reversed(range(height)):
        tree = data[y][x]
        # print(tree)
        if current == None:
            current = tree
            tree_counter += 1
            new_str = str(x) + "/" + str(y)
            visable_list.append(new_str)
            print(f'+1, current {current}, First in row')
        if tree > current:
            current = tree
            tree_counter += 1
            new_str = str(x) + "/" + str(y)
            visable_list.append(new_str)
            print(f'+1, current {current}, next {tree}')
    current = None

# Left 
print("Left RIght")
current = None
for y in (range(height)):
    print("New Row:")
    for x in (range(width)):
        tree = data[y][x]
        # print(tree)
        if current == None:
            current = tree
            tree_counter += 1
            
            new_str = str(x) + "/" + str(y)
            visable_list.append(new_str)
            print(f'+1, current {current}, First in row')
        if tree > current:
            current = tree
            tree_counter += 1
            new_str = str(x) + "/" + str(y)
            visable_list.append(new_str)
            print(f'+1, current {current}, next {tree}')
    current = None

# Right 
print("Right Left")
current = None
for y in reversed(range(height)):
    print("New Row:")
    for x in reversed(range(width)):
        tree = data[y][x]
        # print(tree)
        if current == None:
            current = tree
            tree_counter += 1
            new_str = str(x) + "/" + str(y)
            visable_list.append(new_str)
            print(f'+1, current {current}, First in row')
        if tree > current:
            current = tree
            tree_counter += 1
            new_str = str(x) + "/" + str(y)
            visable_list.append(new_str)
            print(f'+1, current {current}, next {tree}')
    current = None

visable_list.sort()

vis_set = set(visable_list)
print(vis_set)
print(f'Total: {tree_counter}')
print(len(vis_set))

f.close()
# print(data)