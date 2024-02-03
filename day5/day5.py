# https://adventofcode.com/2023/day/5

import re
try: 
    # Open file containing the words separated by a line
    theFile = open("./day2.txt")
    #theFile = open("./message.txt")
    #theFile = open("./day2-practice.txt")
    
except:
    print("NO FILE")

def main():
    load_data()

def load_data():
    
    for line in theFile:
        m = re.match("(seeds: )+(?P<game_id>[0-9]*[0-9])", line)

main()
