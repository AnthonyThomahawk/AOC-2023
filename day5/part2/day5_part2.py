import time
inputFile = open('input.txt', 'r')
data = inputFile.read()

def strMapToIntMap(strMap):
    intMap = []
    lines = strMap.split('\n')
    for l in lines:
        if l:
            intMap.append([int(i) for i in l.split(' ')])
    return intMap

strMaps = []
strMaps.append(data.split('seed-to-soil map:\n')[1].split('\nsoil-to-fertilizer map:')[0])
strMaps.append(data.split('soil-to-fertilizer map:\n')[1].split('\nfertilizer-to-water map:')[0])
strMaps.append(data.split('fertilizer-to-water map:\n')[1].split('\nwater-to-light map:')[0])
strMaps.append(data.split('water-to-light map:\n')[1].split('\nlight-to-temperature map:')[0])
strMaps.append(data.split('light-to-temperature map:\n')[1].split('\ntemperature-to-humidity map:')[0])
strMaps.append(data.split('temperature-to-humidity map:\n')[1].split('\nhumidity-to-location map:')[0])
strMaps.append(data.split('humidity-to-location map:\n')[1])

allMaps = []

for strMap in strMaps:
    allMaps.append(strMapToIntMap(strMap))

seedsStr = data.split('seeds: ')[1].split('seed-to-soil map:\n')[0].strip()
seedRanges = [int(i) for i in seedsStr.split(' ')]

def mapPoint(p):
    for Map in allMaps:
        for mapRange in Map:
            if p >= mapRange[1] and p <= mapRange[1] + mapRange[2]:
                p = p - (mapRange[1] - mapRange[0])
                break
    return p

def getMinLocation():
    minLoc = None

    for i in range(0, len(seedRanges), 2):
        j = seedRanges[i]
        while j <= seedRanges[i] + seedRanges[i + 1]:
            mapped = mapPoint(j)
            
            if minLoc is None:
                minLoc = mapped
            elif minLoc > mapped:
                minLoc = mapped

            end = seedRanges[i] + seedRanges[i + 1]
            mapped_end = mapPoint(end)

            while abs(j - end) != abs(mapped - mapped_end):
                end = j + ((end - j) // 2)
                mapped_end = mapPoint(end)
                
            print('Point {0} mapped to {1}'.format(j, mapped))
            
            if abs(j - end) == 0:
                print('No skip')
                j += 1
            else:
                print('Skipped {0}'.format(abs(j - end)))
                j += abs(j - end)
                

    return minLoc


time_start = time.perf_counter()
minLoc = getMinLocation()
time_end = time.perf_counter()
print('Minimum location : {0}'.format(minLoc))
print(f'Time taken : {time_end-time_start:.15f} seconds')
