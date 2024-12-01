# Rearrange the backpack based on priority
import string
f = open("dataset.txt", "r")
raw_data = f.readlines()

# Example data:
# 2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8



# Find how many elves range are fully in their partners

# List to work out game scores
data = []
counter = 0
for line in raw_data:
    pair = line.strip().split(",")
    # [2-4],[6-8]
    tmp = []
    for elf in pair:
        range_coord = elf.split("-")
        actual_range = range(int(range_coord[0]), int(range_coord[1]) +1)
        tmp.append(actual_range)
    data.append(tmp)
f.close()
for row in data:
    print("Row:")
    a = row[0]
    b = row[1]
    print(f'{a[0]} -> {a[-1]}')
    print(f'{b[0]} -> {b[-1]}')
    if((a[0] in b and a[-1] in b) or (b[0] in a and b[-1] in a)):
        print("RANGE WAS IN ONE")
        counter += 1

print(f'\nCounter: {counter}')