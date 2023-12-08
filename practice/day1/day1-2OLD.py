# https://adventofcode.com/2023/day/1#part2

import re

digitPattern = '^[0-9]'
wordPattern = '(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)'
wordDigitPattern = '(?=(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(\d))'
wordToNumber = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
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

def helperWordToDigit(word):
    if word.isdigit():
        return word
    else:
        return wordToNumber[word]

try: 
    # Open file containing the words separated by a line
    theFile = open("day1/day1-2.txt")
    
except:
    print("NO FILE")

count = ""
totalCount = 0

for line in theFile:
    processedLine = replaceWordToDigit(line, wordPattern)
    print("Original     : ", line, end="")
    print("processedLine: ", processedLine)

    for char in processedLine:
        # If it's a digit, append it as a character to variable count
        if re.match(digitPattern, char):
            count += char
    print(count)

    # Take the first and last digit and combine them
    finalDigit = count[0] + count[-1]

    # Add the two-digit number to the total
    totalCount += int(finalDigit)
    print(finalDigit + '\n')

    # Reset temporary variables
    count = ""
    finalDigit = ""

print(totalCount)







# FInd each word number
# Turn them into digit
# Then do day1.py on it