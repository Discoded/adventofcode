# https://adventofcode.com/2023/day/1
import re
try: 
    # Open file containing the words separated by a line
    theFile = open("day1/day1.txt")
    
except:
    print("NO FILE")


count = ""
digitPattern = '^[0-9]'
totalCount = 0

# For each line in the file
for line in theFile:
    print(line, end='')
    # For each character in the string, check if it's a digit (regex '^[0-9]')
    for char in line:
        # If it's a digit, append it as a character to variable count
        if re.match(digitPattern, char):
            count += char
    print(count)

    # Take the first and last digit and combine them
    finalDigit = count[0] + count[-1]

    # Add the two-digit number to the total
    totalCount += int(finalDigit)

    print(count)
    print(finalDigit + '\n')

    # Reset temporary variables
    count = ""
    finalDigit = ""
print("Total: ", totalCount)

    
    