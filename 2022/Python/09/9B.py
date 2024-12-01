f = open("dataset.txt", "r")
raw_data = f.readlines()
data = []
f.close()
rope: list = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

head = [0,0]
tail = [0,0]
tail_pos = set()

for line in raw_data:
    dir, spaces = line.strip().split(" ")
    spaces = int(spaces)
    # print(f'{dir}, {spaces} spaces')
    for move in range(1, spaces + 1):
        # Move head first
        head = rope[0]
        if (dir == 'R'):
            head[0] += 1
        elif (dir == 'L'):
            head[0] -= 1
        elif (dir == "U"):
            head[1] += 1
        elif (dir == "D"):
            head[1] -= 1
            # Update 
        for n in range(1,10):
            head = rope[n-1]
            tail = rope[n]
            x_diff = head[0] - tail[0]
            # x_dist = abs(head[0] - tail[0])
            y_diff = head[1] - tail[1]
            # y_dist = abs(head[1] - tail[1])
            if abs(x_diff) == 2 and abs(y_diff) == 2:
                tail[0] += x_diff//2
                tail[1] += y_diff//2
            else:
                if abs(x_diff) == 2:
                    tail[0] += x_diff//2
                    tail[1] = head[1]
                if abs(y_diff) == 2:
                    tail[1] += y_diff//2
                    tail[0] = head[0]
            tail_pos.add(str(rope[-1]))
        # print(f'HEAD: {head} | TAIL: {tail}')
print(f'Unique: {len(tail_pos)}')
# print(rope)