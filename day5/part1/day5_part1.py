import time
import threading
inputFile = open('input.txt', 'r')
data = inputFile.read()

def strMapToIntMap(strMap):
    intMap = []
    lines = strMap.split('\n')
    for l in lines:
        if l:
            intMap.append([int(i) for i in l.split(' ')])
    return intMap

seedsStr = data.split('seeds: ')[1].split('seed-to-soil map:\n')[0].strip()
seedToSoilMapStr = data.split('seed-to-soil map:\n')[1].split('\nsoil-to-fertilizer map:')[0]
soilToFertilizerMapStr = data.split('soil-to-fertilizer map:\n')[1].split('\nfertilizer-to-water map:')[0]
fertilizerToWaterMapStr = data.split('fertilizer-to-water map:\n')[1].split('\nwater-to-light map:')[0]
waterToLightMapStr = data.split('water-to-light map:\n')[1].split('\nlight-to-temperature map:')[0]
lightToTempMapStr = data.split('light-to-temperature map:\n')[1].split('\ntemperature-to-humidity map:')[0]
tempToHumidityMapStr = data.split('temperature-to-humidity map:\n')[1].split('\nhumidity-to-location map:')[0]
humidityToLocationMapStr = data.split('humidity-to-location map:\n')[1]

seeds = [int(i) for i in seedsStr.split(' ')]

seedToSoilMap = strMapToIntMap(seedToSoilMapStr)
soilToFertilizerMap = strMapToIntMap(soilToFertilizerMapStr)
fertilizerToWaterMap = strMapToIntMap(fertilizerToWaterMapStr)
waterToLightMap = strMapToIntMap(waterToLightMapStr)
lightToTempMap = strMapToIntMap(lightToTempMapStr)
tempToHumidityMap = strMapToIntMap(tempToHumidityMapStr)
humidityToLocationMap = strMapToIntMap(humidityToLocationMapStr)

def mapPoint(mapList, point):
    for m in mapList:
        if point >= m[1] and point <= m[1]+m[2]:
            return point - (m[1]-m[0])

    return point

def getLocations():
    locations = []
    for s in seeds:
        soil = mapPoint(seedToSoilMap, s)
        print('Seed {0} mapped to {1} soil.'.format(s, soil))
        fertilizer = mapPoint(soilToFertilizerMap, soil)
        print('Soil {0} mapped to {1} fertilizer'.format(soil, fertilizer))
        water = mapPoint(fertilizerToWaterMap, fertilizer)
        print('Fertilizer {0} mapped to {1} water'.format(fertilizer, water))
        light = mapPoint(waterToLightMap, water)
        print('Water {0} mapped to {1} light'.format(water, light))
        temp = mapPoint(lightToTempMap, light)
        print('Light {0} mapped to {1} temp'.format(light, temp))
        humidity = mapPoint(tempToHumidityMap, temp)
        print('Temp {0} mapped to {1} humidity'.format(temp, humidity))
        location = mapPoint(humidityToLocationMap, humidity)
        print('Humidity {0} mapped to {1} location'.format(humidity, location))
        locations.append(location)
    return locations
    

time_start = time.perf_counter()
locations = getLocations()
time_end = time.perf_counter()
print('All locations:')
print(locations)
print('Minimum location : {0}'.format(min(locations)))
print(f'Time taken : {time_end-time_start:.15f} seconds')