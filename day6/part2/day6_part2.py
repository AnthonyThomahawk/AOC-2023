inputFile = open('input.txt', 'r')
data = inputFile.readlines()
timevals = data[0].split("Time:      ")[1].strip()
distvals = data[1].split("Distance:  ")[1]
time = timevals.split()
records = distvals.split()
for i in range(len(time)):
    time[i] = int(time[i])
    records[i] = int(records[i])

prod = 1
for i in range(len(time)):
    victories = 0
    for s in range(1, time[i]+1):
        d = time[i] - s
        total = s * d
        if total > records[i]:
            victories += 1
    prod *= victories

print(prod)