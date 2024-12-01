cycles = 0
x = 1
checkpoints = []

def check_cycle():
    current_pixel = (cycles-1) % 40
    if current_pixel == 0:
        print()
    if x -1 <= current_pixel <= x + 1:
        print("#", end="")
    else:
        print(".", end="")
    # sprite_bound = range(x-1,x+2)
    
with open('dataset.txt') as f:
    raw = f.readlines()
for line in raw:
    line = line.strip()
    if line == "noop":
        cycles += 1
        check_cycle()
    else:
        cycles += 1
        check_cycle()
        cycles += 1
        check_cycle()
        inst, val = line.split(" ")
        x += int(val)

print('\n')
# print(checkpoints)
# total = 0
# for item in checkpoints:
#     total += item