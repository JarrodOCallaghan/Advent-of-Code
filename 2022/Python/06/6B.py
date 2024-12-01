data = open("dataset.txt", "r").read()
for n in range(len(data)-13):
    str = data[n:n+14]
    if(len(set(str)) == len(str)):
        print(f'{str} - True - {n+14}')
        break