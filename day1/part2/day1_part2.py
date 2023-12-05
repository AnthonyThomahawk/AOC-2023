inputFile = open('input.txt', 'r')
data = inputFile.readlines()

def getFirstAndLastDigit(line):
    first = None
    last = None
    firstFound = False
    word_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    i = 0
    while i < len(line):
        if i >= len(line):
            break

        wordFound = False

        for idx, word in enumerate(word_numbers):
            f_ind = line.find(word, i)
            if f_ind != -1:
                if f_ind != i:
                    continue
                i += len(word)-1
                if not firstFound:
                    first = str(idx+1)
                    firstFound = True
                else:
                    last = str(idx+1)
                wordFound = True
                break

        if wordFound:
            continue

        if line[i].isdigit():
            if not firstFound:
                first = line[i]
                firstFound = True
            else:
                last = line[i]
        
        i += 1
        
        
    
    if last is None:
        last = first
    
    return first,last

s = 0
for line in data:
    f, l = getFirstAndLastDigit(line)
    num = int(f+l)
    s += num

print(s)