# https://adventofcode.com/2023/day/7
import re
import math
import typing
import copy
import time

global theFile
def main():
    try: 
        # Open file containing the words separated by a line

        theFile = open("./day8/day8.txt")
        #theFile = open("./day8.txt")
        #theFile = open("./day8/day8-practice.txt")
              
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
            tree_dictionary[node[0]] = [node[1], node[2]]
        except StopIteration:
            print("StopIteration Exception")
            break
    tree_keys = list(tree_dictionary)
    

    
    matches = [x for x in tree_keys if x[2] == 'A']
    print("Starting Nodes: ", matches)
    original_matches = copy.deepcopy(matches)
    # Assert that there are only 2 matches ending in 'A'
    #assert len(matches) == 2

    sentinels = [x for x in matches]
    counter = len(sentinels)

    exceptionCounter = 0
    steps = [0 for x in range(len(matches))]
    steps_counter = [0 for x in range(len(matches))]
    start = time.time()


    while True:
        try:
            for i, instruction in enumerate(l_r_instructions):
                
                for i, elem in enumerate(matches):
                    
                    sentinels[i] = traverse_tree(tree_dictionary, instruction, elem)
                    steps_counter[i] += 1
                    if sentinels[i][2] == 'Z':
                        steps[i] = steps_counter[i]
                        steps_counter[i] = 0
                
                    counter += 1 
                matches = copy.deepcopy(sentinels)

            for x in steps:
                if x != 0:
                    exceptionCounter += 1

            if exceptionCounter >= len(matches):
                
                raise(Exception)
            else: 
                exceptionCounter = 0
                
        except BaseException as e:
            print("Exception: ", e)
            break
        
    end = time.time()

    print("original: ", original_matches)
    print("Total Steps: ", counter)
    print("Steps For each Node before repeat: ", steps)
    # Calculate LCM
    step0 = steps[0]
    for step in steps:
        step0 = math.lcm(step0, step)
    
    print("Traversal Time: ", end - start)
    print("Lowest Common Multiple: ", step0)

    

def check_sentinels(theSentinels: typing.List[str]) -> bool:
    """Return true is all element in the given array ends with 'Z' character

    Keyword arguments:
    theSentinels -- List of strings to check the last or 3rd character. Each element string must have a length of 3
    """
    for elem in theSentinels:
        ## If a sentinel[2] is not equal to 'Z' return True
        assert len(elem) == 3
        if elem[2] != 'Z':
            return True
    return False

def traverse_tree(theTree: typing.Dict, instruction: str, theSentinel: str):
    assert len(theSentinel) == 3
    if instruction == 'L':
        #print("L ", elem + " -> " + tree_dictionary[elem][0])
        return theTree[theSentinel][0]
    elif instruction == 'R':
        #print("L ", elem + " -> " + tree_dictionary[elem][1])
        return theTree[theSentinel][1]
    else:
        raise Exception("Else statement reached. Should not be possible.")
    
        
    
main()
