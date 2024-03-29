# https://adventofcode.com/2023/day/5

import re
import myMap
import sys

def main():
    try: 
        # Open file containing the words separated by a line
        theFile = open("./day5.txt")
        #theFile = open("./day5-practice.txt")
              
    except:
        print("NO FILE")

    load_data(theFile)
    
    

def load_data(theFile):
    

    iterable = iter(theFile)
    seeds = []
    seed_to_soil_map = myMap.myMap()
    soil_to_fertilizer_map = myMap.myMap()
    fertilizer_to_water_map = myMap.myMap()
    water_to_light_map = myMap.myMap()
    light_to_temperature_map = myMap.myMap()
    temperature_to_humidity_map = myMap.myMap()
    humidity_to_location_map = myMap.myMap()

    while True:
        try:
            out = next(iterable)
            if(re.match("seeds: ", out)):
                seeds = re.findall("[0-9]*[0-9]", out)
                print("seeds: ", seeds)
            elif re.match("seed-to-soil map:", out):
                out = next(iterable)
                while out != "\n":
                    seed_to_soil_map = seed_to_soil_map | handle_map_input(out)
                    out = next(iterable)
            elif re.match("soil-to-fertilizer map:", out):
                out = next(iterable)
                while out != "\n":
                    soil_to_fertilizer_map = soil_to_fertilizer_map| handle_map_input(out)
                    out = next(iterable)
            elif re.match("fertilizer-to-water map:", out):
                out = next(iterable)
                while out != "\n":
                    fertilizer_to_water_map = fertilizer_to_water_map| handle_map_input(out)
                    out = next(iterable)
            elif re.match("water-to-light map:", out):
                out = next(iterable)
                while out != "\n":
                    water_to_light_map = water_to_light_map| handle_map_input(out)
                    out = next(iterable)
            elif re.match("light-to-temperature map:", out):
                out = next(iterable)
                while out != "\n":
                    light_to_temperature_map = light_to_temperature_map| handle_map_input(out)
                    out = next(iterable)
            elif re.match("temperature-to-humidity map:", out):
                out = next(iterable)
                while out != "\n":
                    temperature_to_humidity_map = temperature_to_humidity_map| handle_map_input(out)
                    out = next(iterable)
            elif re.match("humidity-to-location map:", out):
                out = next(iterable)
                while out != "\n":
                    humidity_to_location_map = humidity_to_location_map| handle_map_input(out)
                    out = next(iterable)
            
        except StopIteration:
            print("StopIteration triggered")
            break
    
    """Solution to Day 5 Part 1
    seeds = [int(x) for x in seeds]
    solutions = [[] for x in range(0, 8)]
    for i, seed in enumerate(seeds):
        solutions[0].append(seed)
        solutions[1].append(seed_to_soil_map.get(seed))
        solutions[2].append(soil_to_fertilizer_map.get(solutions[1][i]))
        solutions[3].append(fertilizer_to_water_map.get(solutions[2][i]))
        solutions[4].append(water_to_light_map.get(solutions[3][i]))
        solutions[5].append(light_to_temperature_map.get(solutions[4][i]))
        solutions[6].append(temperature_to_humidity_map.get(solutions[5][i]))
        solutions[7].append(humidity_to_location_map.get(solutions[6][i]))
    """
    seeds = [int(x) for x in seeds]
    iterable = iter(seeds)
    element = next(iterable)
    seed_range_pairs = []

    while True:
        try: 
            theSeed = element
            element = next(iterable)
            theRange = element
            seed_range_pairs.append([theSeed, theRange])
            element = next(iterable)
        except StopIteration:
            break
    
    print(seed_range_pairs)
    
    solutions = [[] for x in range(0, 8)]
    for i, elem in enumerate(seed_range_pairs):
        #print("elem: ",elem)
        solutions[0].append(elem)
        solutions[1].append(getRange(elem, seed_to_soil_map))
        solutions[2].append(getValues(solutions[1][i], soil_to_fertilizer_map))
        solutions[3].append(getValues(solutions[2][i], fertilizer_to_water_map))
        solutions[4].append(getValues(solutions[3][i], water_to_light_map))
        solutions[5].append(getValues(solutions[4][i], light_to_temperature_map))
        solutions[6].append(getValues(solutions[5][i], temperature_to_humidity_map))
        solutions[7].append(getValues(solutions[6][i], humidity_to_location_map))
    
    for i, x in enumerate(solutions):
        print(i,x)
        
    min_location = sys.maxsize
    for elem in solutions[7]:

        for pair in elem:
            local_min_location = pair[0]
            if local_min_location < min_location:
                min_location = local_min_location

    print("min_location: ", min_location)


def getRange(thePair, theMap):
    print("getRange thePair: ", thePair)
    theSourcePairList = theMap.find(thePair)
    print("getRange theSourcePairList ", theSourcePairList)

    theDestinationPairList = []

    for x in theSourcePairList:
        destStart = theMap.get(x[0])
        destRange = x[1]
        theDestinationPairList.append([destStart, destRange])
    
    print("getRange() theDestinationPairList: ", theDestinationPairList)
    print()


    return theDestinationPairList
def getValues(valuesPairList, theMap):
    theSourcePairList = []
    theDestinationPairList = []

    for pair in valuesPairList:
        theSourcePairList = theMap.find(pair)

        for sourcePair in theSourcePairList:
            destStart = theMap.get(sourcePair[0])
            destRange = sourcePair[1]
            theDestinationPairList.append([destStart, destRange])

    return theDestinationPairList



def handle_map_input(theLine):

    map_input = re.findall("[0-9]*[0-9]", theLine)
    map_input = [int(x) for x in map_input]
    theMap = myMap.myMap(map_input)
    return theMap

# Call main()
main()
