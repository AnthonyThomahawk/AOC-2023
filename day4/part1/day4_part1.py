inputFile = open('input.txt', 'r')
cards = inputFile.read().splitlines()

pileTotal = 0

for card in cards:
    winning = card.split(':')[1].split('|')[0].split(' ')
    mine = card.split(':')[1].split('|')[1].split(' ')

    winNums = [int(i) for i in winning if i]
    myNums = [int(i) for i in mine if i]

    cardPoints = 0

    for num in myNums:
        if num in winNums:
            if cardPoints == 0:
                cardPoints = 1
            else:
                cardPoints *= 2

    pileTotal += cardPoints
    
print(pileTotal)