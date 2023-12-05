inputFile = open('input.txt', 'r')
data = inputFile.readlines()

def getMinPower(game):
    maxRed = -1
    maxGreen = -1
    maxBlue = -1
    gameSets = game.split(': ')[1].split(';')
    for gameSet in gameSets:
        cubes = gameSet.split(', ')
        for cube in cubes:
            count = int(cube.strip().split(' ')[0])
            color = str(cube.strip().split(' ')[1])

            if color == "red" and count > maxRed:
                maxRed = count
            elif color == "green" and count > maxGreen:
                maxGreen = count
            elif color == "blue" and count > maxBlue:
                maxBlue = count
    
    minPower = maxRed * maxGreen * maxBlue
    return minPower

s = 0
for game in data:
    s += getMinPower(game)
print(s)