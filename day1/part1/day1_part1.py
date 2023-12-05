inputFile = open('input.txt', 'r')
data = inputFile.readlines()

def extractFirstAndLastDigit(line):
    first = None
    last = None
    firstFound = False
    for c in line:
        if c.isdigit():
            if not firstFound:
                first = c
                firstFound = True
            else:
                last = c
    
    if last is None:
        last = first
    
    return first,last

s = 0
for line in data:
    f, l = extractFirstAndLastDigit(line)
    num = int(f+l)
    s += num

print(s)