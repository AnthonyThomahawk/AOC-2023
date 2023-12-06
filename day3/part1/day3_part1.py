inputFile = open('input.txt', 'r')
data = inputFile.read().splitlines()

numbers = []
grid = []

class number:
    def __init__(self, val, start, end, lineNo):
        self.val = val
        self.start = start
        self.end = end
        self.lineNo = lineNo

def findNumbers(line, lineNo):
    numStr = ''
    start = -1
    end = -1
    for ind, c in enumerate(line):
        if c.isdigit():
            numStr += c
            if start == -1:
                start = ind
            if end == -1:
                indNext = ind + 1
                if indNext >= len(line):
                    end = ind
                    n = number(numStr, start, end, lineNo)
                    numbers.append(n)
                    numStr = ''
                    start = -1
                    end = -1
                    break
                if not line[indNext].isdigit():
                    end = ind
                    n = number(numStr, start, end, lineNo)
                    numbers.append(n)
                    numStr = ''
                    start = -1
                    end = -1

def findNeighbour(num):
    # Check up
    for i in range(num.start, num.end+1):
        if num.lineNo-1 < 0:
            break
        if grid[num.lineNo-1][i] != '.':
            return True
    # Check down
    for i in range(num.start, num.end+1):
        if num.lineNo+1 >= len(data):
            break
        if grid[num.lineNo+1][i] != '.':
            return True
    # Check left
    i = num.start - 1
    if i > 0:
        if grid[num.lineNo][i] != '.':
            return True
    # Check right
    i = num.end + 1
    if i < len(data[0]):
        if grid[num.lineNo][i] != '.':
            return True
    # Check left up diag
    j = num.start - 1
    if j >= 0:
        i = num.lineNo - 1
        if i >= 0:
            if grid[i][j] != '.':
                return True
    # Check left down diag
    j = num.start - 1
    if j >= 0:
        i = num.lineNo + 1
        if i < len(data):
            if grid[i][j] != '.':
                return True

    # Check right up diag
    j = num.end + 1
    if j < len(data[0]):
        i = num.lineNo - 1
        if i >= 0:
            if grid[i][j] != '.':
                return True
    # Check right down diag
    j = num.end + 1
    if j < len(data[0]):
        i = num.lineNo + 1
        if i < len(data):
            if grid[i][j] != '.':
                return True
    
    return False


for ind, line in enumerate(data):
    linechars = []
    findNumbers(line, ind)
    for c in line:
        linechars.append(c)
    grid.append(linechars)

s = 0
for num in numbers:
    if findNeighbour(num):
        s += int(num.val)

print(s)