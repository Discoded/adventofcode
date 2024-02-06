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
    seeds = [int(x) for x in seeds]
    print(seeds)

    iterable = iter(seeds)
    out = next(iterable)
    seed_range_pair = []
    while True:
        try:
            ##print(out)
            theSeed = out
            out = next(iterable)
            theRange = out
            seed_range_pair.append([theSeed, theRange])

            out = next(iterable)

        except StopIteration:
                print("StopIteration triggered")
                break
    
    min_location = sys.maxsize
    for pair in seed_range_pair:
        soils = getRange(pair, seed_to_soil_map)
        fertilizers = getValues(soils, soil_to_fertilizer_map)
        waters = getValues(fertilizers, fertilizer_to_water_map)
        lights = getValues(waters, water_to_light_map)
        temperature = getValues(lights, light_to_temperature_map)
        humiditys = getValues(temperature, temperature_to_humidity_map)
        locations = getValues(humiditys, humidity_to_location_map)
        print(locations)
        for location in locations:
            if(location[0] < min_location):
                
                min_location = location[0]

    print("min_location: ", min_location)

def getRange(thePair, theMap):
    theSourcePairList = theMap.find(thePair)
    theSeeds = []
    
    for pair in theSourcePairList:

        destStart = theMap.get(pair[0])
        destEnd = pair[1] - pair[0] + destStart
        theSeeds.append([destStart, destEnd])
    return theSeeds

def getValues(valuesPairList, theMap):
    theSeeds = []
    for value in valuesPairList:
        theSourcePairList = theMap.find([value[0], value[1]-value[0]+1])
        for pair in theSourcePairList:

            destStart = theMap.get(pair[0])
            destEnd = pair[1] - pair[0] + destStart
            theSeeds.append([destStart, destEnd])
    return theSeeds


    

def handle_map_input(theLine):

    map_input = re.findall("[0-9]*[0-9]", theLine)
    map_input = [int(x) for x in map_input]
    theMap = myMap.myMap(map_input)
    #print(theMap)
    return theMap


    
    
      
        

        

main()
