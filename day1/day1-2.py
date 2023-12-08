# https://adventofcode.com/2023/day/1#part2

import re

digitPattern = '^[0-9]'
wordPattern = '(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)'
wordDigitPattern = '(?=(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(\d))'
wordToNumber = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}

def replaceWordToDigit(theString, thePattern):
    result = re.sub(thePattern, dictionary, theString) 
    if result == theString:
        return result
    else:
        return replaceWordToDigit(result, thePattern)

def dictionary(m):
    number = wordToNumber[m.group(0)]
    return str(number)

# Checks if the string is a digit and if not, turn it from a word to a string digit
# i.e 'one' to '1'
def helperWordToDigit(word):
    if word.isdigit():
        return word
    else:
        return wordToNumber[word]

try: 
    # Open file containing the words separated by a line
    theFile = open("day1/day1.txt")
    
except:
    print("NO FILE")

count = ""
totalCount = 0
finalNumber = ''
finalTwoDigit = ''

# For each line in the file
for line in theFile:
    # Reset variables to empty strings
    finalNumber = ''
    finalTwoDigit = ''

    # Look for digits or word digits such as 'one', 'two', etc.
    patternList = re.findall(wordDigitPattern, line)

    # For each character matched in regex,
    # if it's a character and not an empty '', append it finalNumber
    for array in patternList:
        for char in array:
            if char != '':
                finalNumber += helperWordToDigit(char)
    
    # Create a two digit number with the first and last number of the parsed line
    finalTwoDigit = finalNumber[0] + finalNumber[-1]
    
    # Add to the total count.
    totalCount += int(finalTwoDigit)
    
    print(finalNumber)
    print(finalTwoDigit, end='\n\n')

print("Total: ", totalCount)
    
