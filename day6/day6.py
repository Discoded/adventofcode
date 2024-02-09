# https://adventofcode.com/2023/day/7
import re
import math

global theFile
def main():
    try: 
        # Open file containing the words separated by a line

        # Part 1
        #theFile = open("./day6.txt")

        # Part 2
        theFile = open("./day6-2.txt")
        #theFile = open("./day6-practice.txt")
              
    except:
        print("NO FILE")

    iterable = iter(theFile)


    times = []
    distances = []
    for line in theFile:
        if(re.match("Time: ", line)):
            times = re.findall("[0-9]*[0-9]", line)
            print("times: ", times)
        else:
            distances = re.findall("[0-9]*[0-9]", line)
            print("distances: ", distances)
    
    times = [int(time) for time in times]
    distances = [int(distance) for distance in distances]
    hold_time = []
    ways_to_win_list = []
    for i, time in enumerate(times):
        record_time = time
        record_distance = distances[i]

        print("\nrecord_time: {}\nrecord_distance: {}".format(record_time, record_distance))
        
        #print("hold_time is between 0 and ", record_time)
        print("h^2 + {}*h - {}".format(record_time, record_distance))
        
        hold_time = find_quadratic_roots(-1, record_time, -1*record_distance)
        
        ways_to_win = hold_time[1] - hold_time[0] + 1
        print("ways_to_win: ", ways_to_win)
        ways_to_win_list.append(ways_to_win)

    print("ways_to_win_list: ", ways_to_win_list)
    print("ways_to_win_list product:", math.prod(ways_to_win_list))

def find_quadratic_roots(a: int, b: int, c: int):

    root_0 = 0
    root_1 = 0

    print("a:{}, b:{}, c:{}".format(a, b, c))
    root_0 = ((-1*b)+math.sqrt(math.pow(b, 2) - 4*a*c ))/(2*a)
    root_1 = ((-1*b)- math.sqrt(math.pow(b, 2) - 4*a*c ))/(2*a)

    print(root_0, root_1)
    print(math.floor(root_0)+1, math.ceil(root_1)-1)
    
    floor_root_0 = math.floor(root_0)+1
    ceil_root_1 = math.ceil(root_1)-1

    return [floor_root_0, ceil_root_1]

    
main()