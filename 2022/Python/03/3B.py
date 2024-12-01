# Rearrange the backpack based on priority
import string
f = open("dataset.txt", "r")
raw_data = f.readlines()

# List to work out game scores

# We are now working out the commonality between 3 groups, not sub
data = []
temp_subset = []
sum = 0
counter = 0
for line in raw_data:
    # print(counter)
    line = line.strip()
    # print(line)
    temp_subset.append(line)

    counter += 1
    if counter > 2 :
        data.append(temp_subset)
        temp_subset = []
        counter = 0

f.close()

for group in data:
    a = set(group[0])
    b = set(group[1])
    c = set(group[2])

    set1 = a.intersection(b)
    result_set = set1.intersection(c)
    final_list = list(result_set)
    el = final_list[0]
    ascii_value = string.ascii_letters.index(el) + 1
    print(f'{el} : {ascii_value}')
    sum += ascii_value
print(sum)