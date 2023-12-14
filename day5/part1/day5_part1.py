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
seeds = [int(i) for i in seedsStr.split(' ')]


def mapPoint(p):
    for Map in allMaps:
        for mapRange in Map:
            if p >= mapRange[1] and p <= mapRange[1] + mapRange[2]:
                p = p - (mapRange[1] - mapRange[0])
                break
    return p

def getLocations():
    locations = []
    for s in seeds:
        mapped = mapPoint(s)
        print('Point {0} mapped to {1}'.format(s, mapped))
        locations.append(mapped)

    return locations
    

time_start = time.perf_counter()
locations = getLocations()
time_end = time.perf_counter()
print('All locations:')
print(locations)
print('Minimum location : {0}'.format(min(locations)))
print(f'Time taken : {time_end-time_start:.15f} seconds')