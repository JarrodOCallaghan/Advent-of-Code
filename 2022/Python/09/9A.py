f = open("dataset.txt", "r")
raw_data = f.readlines()
data = []
# for line in raw_data:
#     data.append([*line.strip()])
f.close()


# [x,y]
head = [0,0]
tail = [0,0]
tail_visited = []

for line in raw_data:
    dir: str
    spaces: int
    dir, spaces = line.strip().split(" ")
    spaces = int(spaces)
    prev = head.copy()
    print(f'\nStart: H {head}, T {tail}')
    print(f'{dir}, {spaces} spaces')
    moves = range(1, spaces + 1)
    for move in moves:
        if (dir == 'R'):
            prev[0] = head[0]
            head[0] += 1
        elif (dir == 'L'):
            prev[0] = head[0]
            head[0] -= 1
        elif (dir == "U"):
            prev[1] = head[1]
            head[1] += 1
        elif (dir == "D"):
            prev[1] = head[1]
            head[1] -= 1
        x_dif = abs(head[0] - tail[0])
        y_dif = abs(head[1] - tail[1])
        if x_dif > 1 or y_dif > 1:
            tail[0] = prev[0]
            tail[1] = prev[1]
        temp: str = str(tail[0]) + ':' + str(tail[1])
        tail_visited.append(temp)
        print(f'HEAD: {head} | TAIL: {tail}')


a = set(tail_visited)
print(f'Total: {len(tail_visited)}, Unique: {len(a)}')
# print(f'Visited: {a}')