# https://adventofcode.com/2023/day/7
import concurrent.futures
import copy
import logging
import logging
import math
import re
import threading
import time
import time
import typing

global theFile
def main():
    try: 
        # Open file containing the words separated by a line

        #theFile = open("./day8/day8.txt")
        theFile = open("./day8-practice.txt")
              
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
    #print(tree_dictionary)
    #print(l_r_instructions)
    #print(list(tree_dictionary))
    tree_keys = list(tree_dictionary)
    

    
    matches = [x for x in tree_keys if x[2] == 'A']
    print(matches)
    original_matches = copy.deepcopy(matches)
    # Assert that there are only 2 matches ending in 'A'
    #assert len(matches) == 2

    sentinels = [x for x in matches]
    sentinel_value = 'Z'
    counter = len(sentinels)
    # While all sentinels' last character do not equal 'Z'

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    while check_sentinels(sentinels):
        try:
            for instruction in l_r_instructions:
                with concurrent.futures.ThreadPoolExecutor(max_workers=len(matches)) as executor:
                        executor_out = executor.map(traverse_tree, range(len(matches)), matches)
                        
                    
                #print(sentinels)    
                counter += 1 
                matches = copy.deepcopy(sentinels)
                #print()
        except:
            print("Exception")
            break
    print("original: ", original_matches)
    print("final: ", sentinels)
    print("executor: ", executor_out)

    print("Steps: ", counter)

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

def traverse_tree(name, theTree: typing.Dict, instruction: str, theSentinel: str):
    logging.info("Thread %s: starting", name)
    assert len(theSentinel) == 3
    if instruction == 'L':
        print("L ", theSentinel + " -> " + theTree[theSentinel][0])
        logging.info("Thread %s: finishing", name)
        return theTree[theSentinel][0]
    elif instruction == 'R':
        print("L ", theSentinel + " -> " + theTree[theSentinel][1])
        logging.info("Thread %s: finishing", name)
        return theTree[theSentinel][1]
    else:
        raise Exception("Else statement reached. Should not be possible.")
    
        
    
main()
