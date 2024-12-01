# Find the elf with the most calories
# Empty line denotes a new elf

f = open("dataset.txt", "r")
lines = f.readlines()
# print(lines)

index = 0
wip = []
for line in lines:
    line = line.replace('\n','')
    if wip == []:
        wip.append(int(line))
    line.replace('\n','')
    if line != '':
        wip[index] += int(line)
    else:
        index += 1
        wip.append(0)

print(wip)
print('\n')
print(max(wip))
test = wip
test.sort( reverse=1)
a = test[0] + test[1] + test[2]
print(a)