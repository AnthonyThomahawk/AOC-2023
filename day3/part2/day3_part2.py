inputFile = open('input.txt', 'r')
data = inputFile.read().splitlines()

grid = []

class point:
    def __init__(self, i, j):
        self.i = i
        self.j = j

for ind, line in enumerate(data):
    linechars = []
    for c in line:
        linechars.append(c)
    grid.append(linechars)

def findNumber(i,j):
    numStr = grid[i][j]
    # scan left
    for x in range(j-1, -1, -1):
        if grid[i][x].isdigit():
            numStr = grid[i][x] + numStr
        else:
            break
    # scan right
    for x in range(j+1, len(data[0])):
        if grid[i][x].isdigit():
            numStr = numStr + grid[i][x]
        else:
            break
    
    return int(numStr)

def checkBounds(x,y):
    if x < 0 or x >= len(data[0]):
        return False
    if y < 0 or y >= len(data):
        return False
    return True

def checkNeighbour(x,y):
    if checkBounds(x,y) and grid[x][y].isdigit():
        return(point(x,y))
    else:
        return None

def findNeighbourNumbers(i,j):
    neighbours = []
    foundUp = False
    foundDown = False
    # Check up
    neighbours.append(checkNeighbour(i-1,j))
    if checkNeighbour(i-1,j) is not None:
        foundUp = True
    # Check down
    neighbours.append(checkNeighbour(i+1,j))
    if checkNeighbour(i+1,j) is not None:
        foundDown = True
    # Check left
    neighbours.append(checkNeighbour(i, j-1))
    # Check right
    neighbours.append(checkNeighbour(i, j+1))
    if not foundUp:
        # Check left up diag
        neighbours.append(checkNeighbour(i-1, j-1))
        # Check right up diag
        neighbours.append(checkNeighbour(i-1, j+1))
    if not foundDown:
        # Check right down diag
        neighbours.append(checkNeighbour(i+1, j+1))
        # Check left down diag
        neighbours.append(checkNeighbour(i+1, j-1))

    return neighbours

def findGears():
    gears = []
    for i in range(0, len(data)):
        for j in range(0, len(data[0])):
            if grid[i][j] == '*':
                gears.append(point(i,j))
    return gears

def getGearRatios():
    ratios = []
    gears = findGears()
    for gear in gears:
        ratio = 1
        neighbours = findNeighbourNumbers(gear.i, gear.j)
        count = 0
        for n in neighbours:
            if n is not None:
                count += 1
        
        if count != 2:
            continue

        for n in neighbours:
            if n is not None:
                ratio *= findNumber(n.i, n.j)
        
        ratios.append(ratio)
    
    return ratios

ratios = getGearRatios()
s = 0
for r in ratios:
    s += r

print(s)