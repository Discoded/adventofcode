# https://adventofcode.com/2023/day/7
import re
import math

global theFile
def main():
    try: 
        # Open file containing the words separated by a line

        theFile = open("./day8/day8.txt")
        theFile = open("./day8/day8-practice.txt")
              
    except:
        print("NO FILE")

    iterable = iter(theFile)

    # Left and right instructions
    line = next(iterable)
    l_r_instructions = re.findall('\\w', line)
    next(iterable)

    tree_dictionary = dict()

    line = next(iterable)
    node = re.findall("(\\w\\w\\w)", line)
    tree_dictionary[node[0]] = [node[1], node[2]]
    while True:
        try:
            line = next(iterable)
            node = re.findall("(\\w\\w\\w)", line)
            print(node)
            #tree_dictionary.append(node[0])
            tree_dictionary[node[0]] = [node[1], node[2]]
        except StopIteration:
            print("StopIteration Exception")
            break
    print(tree_dictionary)
    print(l_r_instructions)

    sentinel = "AAA"
    sentinel_val = "ZZZ"
    counter = 0
    while sentinel != sentinel_val:
        try:
            for instruction in l_r_instructions:
                if instruction == 'L':
                    print("L ", sentinel + " -> "+ tree_dictionary[sentinel][0])
                    sentinel =  tree_dictionary[sentinel][0]
                elif instruction == 'R':
                    print("R ", sentinel + " -> "+ tree_dictionary[sentinel][1])
                    sentinel = tree_dictionary[sentinel][1]
                counter += 1
        except:
            print("Exception")
            break
    
    print("Steps: ", counter)
    
main()
