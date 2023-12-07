inputFile = open('input.txt', 'r')
cards = inputFile.read().splitlines()

copies = [0] * len(cards)
winNumbers = []
myNumbers = []

for card in cards:
    winning = card.split(':')[1].split('|')[0].split(' ')
    mine = card.split(':')[1].split('|')[1].split(' ')

    winNums = [int(i) for i in winning if i]
    myNums = [int(i) for i in mine if i]

    winNumbers.append(winNums)
    myNumbers.append(myNums)

for i in range(0, len(cards)):
    c = i
    for j in range(0, len(myNumbers[i])):
        if myNumbers[i][j] in winNumbers[i]:
            c += 1
    
    for j in range(i+1,c+1): # original card
        copies[j] += 1
    
    for k in range(0, copies[i]): # process copies (if they exist)
        for j in range(i+1,c+1):
                copies[j] += 1

s = 0
for c in copies:
    s += c + 1 # +1 to take account the original card
print(s)