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

for line in theFile:
    finalNumber = ''
    finalTwoDigit = ''
    patternList = re.findall(wordDigitPattern, line)

    for array in patternList:
        for char in array:
            if char != '':
                finalNumber += helperWordToDigit(char)
    
    finalTwoDigit = finalNumber[0] + finalNumber[-1]
    totalCount += int(finalTwoDigit)
    print(finalNumber)
    print(finalTwoDigit, end='\n\n')

print("Total: ", totalCount)
    
