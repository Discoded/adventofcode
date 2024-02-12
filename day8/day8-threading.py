# https://adventofcode.com/2023/day/7
import concurrent.futures
import copy
import logging
import math
import re
import threading
import time
import typing

def main():
    try: 
        # Open file containing the words separated by a line

        theFile = open("./day8/day8.txt")
        #theFile = open("./day8.txt")
        #theFile = open("./day8-practice.txt")
              
    except:
        print("NO FILE")

    iterable = iter(theFile)

    # Left and right instructions
    line = next(iterable)
    global l_r_instructions
    l_r_instructions = re.findall('\\w', line)
    
    next(iterable)
    global tree_dictionary
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
    

    global matches
    matches = [x for x in tree_keys if x[2] == 'A']
    print("Starting Nodes: ", matches)
    original_matches = copy.deepcopy(matches)
    # Assert that there are only 2 matches ending in 'A'
    #assert len(matches) == 2

    sentinels = [x for x in matches]
    counter = len(sentinels)

    exceptionCounter = 0
    steps = []
    steps_counter = [0 for x in range(len(matches))]
    thread_names = range(0, len(matches))
    start = time.time()


    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(matches)) as executor:
            results = executor.map(traverse_tree_threaded, thread_names, matches)
        for x in results:
            steps.append(x)
    except Exception as e:
        print(e.message, e.args)
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

def traverse_tree(theInstruction: str, theSentinel: str):
    global tree_dictionary
    assert len(theSentinel) == 3

    if theInstruction == 'L':
        #print("L ", elem + " -> " + tree_dictionary[elem][0])
        return tree_dictionary[theSentinel][0]
    elif theInstruction == 'R':
        #print("L ", elem + " -> " + tree_dictionary[elem][1])
        return tree_dictionary[theSentinel][1]
    else:
        raise Exception("Else statement reached. Should not be possible.")

def traverse_tree_threaded(theThreadName:int, theMatch):
    global l_r_instructions
    startingMatch = theMatch
    theSteps = 0
    print("Thread:", theThreadName, l_r_instructions[0], startingMatch, theSteps)
    while True:
        try:
            for instruction in l_r_instructions:
            
                startingMatch = traverse_tree(instruction, startingMatch)
                theSteps += 1
                
                if startingMatch[2] == 'Z':
                    print("Thread:", theThreadName, instruction, startingMatch, theSteps)
                    return theSteps
        
        except:
            break
    
        
    
main()
