# Rearrange the backpack based on priority
import string
f = open("dataset.txt", "r")
raw_data = f.readlines()

# List to work out game scores
data = []
sum = 0
for line in raw_data:
    # Removed the \n char as it was adding +1 to str len
    line = line.strip()
    a = line[:len(line)//2]
    b = line[len(line)//2:]
    data.append([a,b])
    # We probs dont need to store it
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        ch = a_set & b_set
        for el in ch:
            ascii_value = string.ascii_letters.index(el) + 1
            print(f'{el} : {ascii_value}')
            sum += ascii_value
        #string.ascii_letters.index(ch)
    else:
        print("none")
f.close()
print(sum)