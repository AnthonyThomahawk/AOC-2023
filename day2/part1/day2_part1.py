inputFile = open('input.txt', 'r')
data = inputFile.readlines()

maxRed = 12
maxGreen = 13
maxBlue = 14

def parseGame(game):
    s1 = game.split(': ')
    ID = int(s1[0].split('Game ')[1])
    gameSets = s1[1].split(';')
    for gameSet in gameSets:
        cubes = gameSet.split(', ')
        for cube in cubes:
            count = int(cube.strip().split(' ')[0])
            color = str(cube.strip().split(' ')[1])

            if color == "blue" and count > maxBlue:
                return -1
            elif color == "green" and count > maxGreen:
                return -1
            elif color == "red" and count > maxRed:
                return -1
    return ID

s = 0
for game in data:
    res = parseGame(game)
    if (res != -1):
        s += res

print(s)