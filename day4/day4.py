# https://adventofcode.com/2023/day/4
from itertools import repeat
import math
import re
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(1500)
"""Main function that calls other functions

"""

points_list = []

def main():
    try: 
        # Open file containing the words separated by a line
        theFile = open("./day4.txt")
        #theFile = open("./day4-practice.txt")
    
    except:
        print("NO FILE")

    

    global points_list
    points_list = find_winners(theFile)
    duplicates = [0] + list(repeat(1, len(points_list)-1))
    total_number_of_cards = find_duplicates_iteratively(duplicates)
    #total_number_of_cards = find_duplicates_recursively(duplicates, 0)
    print("total_number_of_cards: ", total_number_of_cards)
    
"""Return a list of integers, each elements describes how many winning numbers are in that card
Example: list[1] is the number of winning numbers in Card 1, list[2] is for Card 2 and so on

Keyword arguments:
theFile -- The file to perform operations on
"""
def find_winners(theFile):
    points = 0
    total_points = 0
    card_points_list = [0]

    # For each line in the file
    for line in theFile:

        print(line, end="")
        m = re.match("(Card *)+(?P<card_id>[0-9]*[0-9]*[0-9])+: ", line)
        card_id = int(m.group("card_id"))
        trimmed_line = line[m.span()[1]:].split("|")
        winning_numbers= sorted([int(x) for x in re.findall("\d*\d", trimmed_line[0])])
        owned_numbers = sorted([int(x) for x in re.findall("\d*\d", trimmed_line[1])])

        #print(winning_numbers)
        #print(owned_numbers)

        for x in winning_numbers:
            for y in owned_numbers:
                if(x == y):
                    points += 1
        
        card_points = math.floor(pow(2, points-1))
        print("Card points: ", card_points, end="\n\n")
        total_points += card_points
        
        card_points_list.append(points)

        points = 0


    print("Total points: ", total_points)
    print("List of points: ", card_points_list)
    return card_points_list

"""Recursively find the number of cards

"""
def find_duplicates_recursion(the_duplicates, the_card_count):
    print(the_duplicates)
    print("total: ", the_card_count)
    card_count = the_card_count

    for i, elem in enumerate(the_duplicates):
        if elem == 0:
            pass
        else:
            # Subtract 1 Card from list of duplicates
            the_duplicates[i] -= 1
            # Add 1 Card to total number of cards
            card_count += 1
            if the_duplicates[i] == 0:
                list_range = i
            else:
                list_range = 0

            print("Card {}, points: {}".format(i, points_list[i]))
            points = points_list[i]

            for x in range(1, points+1):
               
                print("extra card: ", i+x)
                if not (i+x > len(points_list)-1):
                    the_duplicates[i+x] += 1
               
            find_duplicates_iteratively(the_duplicates, card_count)
    
    return card_count
            
def find_duplicates_iteratively(the_duplicates):

    print(the_duplicates)
    card_count = 0
    for i, elem in enumerate(the_duplicates):
        
        while the_duplicates[i] != 0:

            # Subtract 1 Card from list of duplicates
            the_duplicates[i] -= 1
            # Add 1 Card to total number of cards
            card_count += 1

            print("Card {}, points: {}".format(i, points_list[i]))
            points = points_list[i]

            for x in range(1, points+1):
               
                print("extra card: ", i+x)
                if not (i+x > len(points_list)-1):
                    the_duplicates[i+x] += 1
    
    return card_count
            



main()