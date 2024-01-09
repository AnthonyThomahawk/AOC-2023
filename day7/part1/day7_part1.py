from enum import Enum
import time
inputFile = open('day7/part1/input.txt', 'r')
hands = []
bids = []
for line in inputFile:
    parsed = line.split()
    hands.append(parsed[0])
    bids.append(parsed[1])

handTypes = {
    'FiveOfAKind' : 7,
    'FourOfAKind' : 6,
    'FullHouse' : 5,
    'ThreeOfAKind' : 4,
    'TwoPair' : 3,
    'OnePair' : 2,
    'HighCard' : 1
}

Cards = {
    'A' : 13,
    'K' : 12,
    'Q' : 11,
    'J' : 10,
    'T' : 9,
    '9' : 8,
    '8' : 7,
    '7' : 6,
    '6' : 5,
    '5' : 4,
    '4' : 3,
    '3' : 2,
    '2' : 1
}

def getHandType(h):
    if h.count(h[0]) == 5:
        return handTypes['FiveOfAKind']
    else:
        s = set(h)
        if len(s) == len(h):
            return handTypes['HighCard']
        for c in s:
            if h.count(c) == 4:
                return handTypes['FourOfAKind']
            elif h.count(c) == 3:
                if len(s) == 2:
                    return handTypes['FullHouse']
                else:
                    return handTypes['ThreeOfAKind']
            elif h.count(c) == 2:
                if len(s) == 2:
                    return handTypes['FullHouse']
                else:
                    s.remove(c)
                    for x in s:
                        if h.count(x) == 2:
                            return handTypes['TwoPair']
                    return handTypes['OnePair']


# A similar solution that did NOT ALWAYS work, some times it returned None?!

# def getHandType(h):
#     if h.count(h[0]) == 5:
#         return handTypes['FiveOfAKind']
#     else:
#         s = set(h)
#         if len(s) == len(h):
#             return handTypes['HighCard']
#         foundThree = False
#         foundTwo = False
#         for c in s:
#             if foundThree:
#                 if h.count(c) == 2:
#                     return handTypes['FullHouse']
#                 else:
#                     return handTypes['ThreeOfAKind']
#             if foundTwo:
#                 if h.count(c) == 3:
#                     return handTypes['FullHouse']
#                 elif h.count(c) == 2:
#                     return handTypes['TwoPair']
#                 else:
#                     return handTypes['OnePair']

#             if h.count(c) == 4:
#                 return handTypes['FourOfAKind']
#             elif h.count(c) == 3:
#                 foundThree = True
#                 continue
#             elif h.count(c) == 2:
#                 foundTwo = True
#                 continue

def compareHands(h1, h2):
    t1 = getHandType(h1)
    t2 = getHandType(h2)

    if t1 == t2:
        for i in range(len(h1)):
            if h1[i] == h2[i]:
                continue
            else:
                return Cards[h1[i]] > Cards[h2[i]]
    else:
        return t1 > t2


def sortHands(hands, bids):
    n = len(hands)
    swap = False
    for i in range(n):
        for j in range(0, n-i-1):
            if compareHands(hands[j], hands[j+1]):
                hands[j], hands[j+1] = hands[j+1], hands[j]
                bids[j], bids[j+1] = bids[j+1], bids[j]
                swap = True
        
        if not swap:
            break

sortHands(hands, bids)
total = 0
for i, bid in enumerate(bids):
    total += int(bid) * (i+1)
print(total)