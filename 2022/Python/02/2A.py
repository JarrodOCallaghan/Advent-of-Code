# Calculate score based on input
# Scores:
# L = 0
# D = 3
# W = 6

# Selection scores:
# Rock = 1
# Paper = 2
# Scissors = 3

##
# Rock = A / X
# Paper = B / Y
# Scissors = C / Z

def score(a, b):
    # Remember, B is our score
    score = 0
    b = b.upper()
    if b == "X":
        score += 1
    elif b == "Y":
        score +=2
    elif b == "Z":
        score +=3

    # Win states
    # paper loses to scissors   B - Z
    # rock loses to paper       A - Y
    # scissors loses to rock    C - X
    if (a == "A" and b == "X") or (a == "B" and b == "Y") or (a == "C" and b == "Z"):
        score +=3
    if (a == "B" and b == "Z") or (a == "A" and b == "Y") or (a == "C" and b == "X"):
        score +=6
    print(score)
    return score



f = open("dataset.txt", "r")
lines = f.readlines()
# List to work out game scores
games = []
totalscore = 0
for line in lines:
    games.append(line.split())
print(games)
for game in games:
    totalscore += score(game[0], game[1])
print(totalscore)



# index = 0
# wip = []
# for line in lines:
#     line = line.replace('\n','')
#     if wip == []:
#         wip.append(int(line))
#     line.replace('\n','')
#     if line != '':
#         wip[index] += int(line)
#     else:
#         index += 1
#         wip.append(0)

# print(wip)
# print('\n')
# print(max(wip))
# test = wip
# test.sort( reverse=1)
# a = test[0] + test[1] + test[2]
# print(a)