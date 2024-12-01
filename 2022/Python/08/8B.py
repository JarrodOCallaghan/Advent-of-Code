f = open("dataset.txt", "r")
raw_data = f.readlines()
data = []
for line in raw_data:
    data.append([*line.strip()])
f.close()

width = len(data[0])
height = len(data)
hor = range(0,width)
vert = range(0, height)


def calc_scenic(x,y):
    on_left = x == 0
    on_right = x == width-1
    on_top = y == 0
    on_bottom = y == height-1
    total_score = 1
    our_height = int(data[y][x])
    
    top = 0
    left = 0
    bottom = 0
    right = 0

    if not on_top:
        r = range(y-1, -1, -1)
        view_distance = 1
        for n in r:
            next = data[n][x]
            top += 1
            if int(next) >= our_height:
                break

    if not on_left:
        r = range(x-1, -1, -1)
        for n in r:
            next = data[y][n]
            left += 1
            if int(next) >= our_height:
                break
    
    if not on_bottom:
        r = range(y+1, height)
        for n in r:
            next = data[n][x]
            bottom += 1
            if int(next)>=our_height:
                break

    if not on_right:
        r = range(x+1, width)
        for n in r:
            next = data[y][n]
            right += 1
            if int(next) >=our_height:
                break
    total_score = top * right * bottom * left
    return total_score

max = 0

for x in hor:
    for y in vert:
        tmp_score = calc_scenic(x,y)
        if max < tmp_score:
            max = tmp_score
        print(f'Pos: {x}:{y} Score: {tmp_score}')

print(f'final score: {max}')

# Score should be: 291840