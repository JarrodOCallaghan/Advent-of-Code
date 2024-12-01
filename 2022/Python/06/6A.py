data = open("dataset.txt", "r").read()
for n in range(len(data)-3):
    str = data[n:n+4]
    if(len(set(str)) == len(str)):
        print(f'{str} - True - {n+4}')
        break

# Previous imp before shortening it down:
# data = ""
# f = open("dataset.txt", "r")
# raw_data = f.read()
# for line in raw_data:
#     data += line
# f.close()
# data_len = len(data)
# for n in range(data_len-13):
#     str = data[n:n+14]
#     str_set = set(str)
#     if(len(str_set) == len(str)):
#         print(f'{str} - True - {n+14}')
#         break