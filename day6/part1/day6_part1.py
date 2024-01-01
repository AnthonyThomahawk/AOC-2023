inputFile = open('day6/part2/input.txt', 'r')
data = inputFile.readlines()
timevals = data[0].split("Time:      ")[1].strip()
distvals = data[1].split("Distance:  ")[1]
time = int(timevals.replace(" ", ""))
record = int(distvals.replace(" ", ""))


prod = 1
victories = 0
for s in range(1, time+1):
    d = time - s
    total = s * d
    if total > record:
        victories += 1
prod *= victories

print(prod)