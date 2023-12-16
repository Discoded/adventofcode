# https://adventofcode.com/2023/day/3
import re
try: 
    # Open file containing the words separated by a line
    theFile = open("./day3.txt")
    #theFile = open("./day3-practice.txt")
    
except:
    print("NO FILE")


previous_line = ""
after_line = ""

print(previous_line)

# O(n)..?
fileContents = theFile.read().split('\n')

#print(fileContents)

is_part_number = False
part_number_sum = 0
part_numbers = set()
regex = "[^.\d]"
#regex = "@|#|\$|%|&|\*|\+|=|-|/"


# For each line in the file
for i, line in enumerate(fileContents):
    print(i, line, end="\n\n")

    # Find numbers
    # If number:  
    m = re.finditer("\d*\d*\d", line)  

    # ..35.633.
    # (2, 4], (6, 9]
    # @, #, $, %, &, *,

    for x in m:
        print("\nspan: ",x.span())
        print("Potential Part #: ", x.group(), end="\n")

        # If line is the first line, a higher line doesn't exist, so only check bottom line and middle(same) line
        if i == 0:
            # If number is left most, only need to check 3digit: 5/12, 2digit: 4/10
            if x.span()[0] == 0:
                
                print("Top: ")
                # Check right, 
                match = re.search(regex, fileContents[i][x.span()[0]:x.span()[1]+1])
                print("Mid: ", fileContents[i][x.span()[1]:x.span()[1]+1])
                if match:
                    is_part_number = True

                # Check bottom
                match = re.search(regex, fileContents[i+1][i:x.span()[1]+1])
                print("Bot: ", fileContents[i+1][i:x.span()[1]+1])
                if match:
                    is_part_number = True

            # If the potential part number is on the edge
            # Then check 3digit: 5/12, 2digit: 4/10
            elif x.span()[1] == len(line):

                #print("NUMBER IS RIGHT MOST")
                match = re.search(regex, fileContents[i][x.span()[0]-1:x.span()[1]])
                print("Left: ", fileContents[i][x.span()[0]-1:x.span()[1]])
                if match:
                    is_part_number = True
                match = re.search(regex, fileContents[i+1][x.span()[0]-1:x.span()[1]])
                if match:
                    is_part_number = True
                print("Bot: ", fileContents[i+1][x.span()[0]-1:x.span()[1]])

            # If the potential part number is neither left most or right most:
            # Then check 3digit: 7/12, 2digit: 6/10
            else:
                # Check middle left and right:
                match = re.search(regex, fileContents[i][x.span()[0]-1:x.span()[1]+1])
                print("Mid: ",fileContents[i][x.span()[0]-1:x.span()[1]+1])
                if match:
                    is_part_number = True
                # Check bottom 5:
                match = re.search(regex, fileContents[i+1][x.span()[0]-1:x.span()[1]+1])
                if match:
                    is_part_number = True
                print("Bot: ", fileContents[i+1][x.span()[0]-1:x.span()[1]+1])

        # Check if the line is not the last line
        elif i != (len(fileContents) - 1):
            # Check if number is left most
            # Check 3digit: 4 top, 1 mid, 4 bottom, 2digit: 3 top, 1 mid, 3 bottom
            if x.span()[0] == 0:
                # Top 4
                match = re.search(regex, fileContents[i-1][x.span()[0]:x.span()[1]+1])
                if match:
                    is_part_number = True
                # Right
                match = re.search(regex, fileContents[i][x.span()[0]:x.span()[1]+1])
                if match:
                    is_part_number = True
                # Bottom
                match = re.search(regex, fileContents[i+1][x.span()[0]:x.span()[1]+1])
                if match:
                    is_part_number = True
            
            # Check if number is right most
            # 3digit: 9/12, 2digit: 7/12
            elif x.span()[1] == len(line):
                # Top 4
                match = re.search(regex, fileContents[i-1][x.span()[0]-1:x.span()[1]])
                print("Top: ", fileContents[i-1][x.span()[0]-1:x.span()[1]])
                if match:
                    is_part_number = True
                
                # Mid 
                match = re.search(regex, fileContents[i][x.span()[0]-1:x.span()[1]])
                print("Mid: ", fileContents[i][x.span()[0]-1:x.span()[1]])
                if match:
                    is_part_number = True

                # Bot
                match = re.search(regex, fileContents[i+1][x.span()[0]-1:x.span()[1]])
                print("Bot: ", fileContents[i+1][x.span()[0]-1:x.span()[1]])
                if match:
                    is_part_number = True
                
                print("NUMBER IS RIGHT MOST")
            # If in the middle, must check all 12 spots if 3 digit: 5 top, 2 mid, 5 bottom and 10 spots if 2 digit: 4 top, 2 mid, 4 bottom
            else:
                # Check top 5 spots
                match = re.search(regex, fileContents[i-1][x.span()[0]-1:x.span()[1]+1])
                print("Top: ", fileContents[i-1][x.span()[0]-1:x.span()[1]+1])
                if match:
                    is_part_number = True
                    
                # Check middle 2 spots (left and right)
                match = re.search(regex, fileContents[i][x.span()[0]-1:x.span()[1]+1])
                print("Mid: ", fileContents[i][x.span()[0]-1:x.span()[1]+1])
                if match:
                    is_part_number = True

                # Check bottom 5 spots
                match = re.search(regex, fileContents[i+1][x.span()[0]-1:x.span()[1]+1])
                print("Bot: ", fileContents[i+1][x.span()[0]-1:x.span()[1]+1])
                if match:
                    is_part_number = True
        
        # For the last line
        else: 
            # If number is left most, only need to check 3digit: 5/12, 2digit: 4/10
            if x.span()[0] == 0:
                print("Top: ", fileContents[i-1][i:x.span()[1]+1])
                # Check right, 
                match = re.search(regex, fileContents[i][x.span()[1]:x.span()[1]+1])
                print("Right match: ", match)
                if match:
                    is_part_number = True
                # Check top
                match = re.search(regex, fileContents[i-1][i:x.span()[1]+1])
                if match:
                    is_part_number = True

            # If the potential part number is on the right edge
            # Then check 3digit: 5/12, 2digit: 4/10
            elif x.span()[1] == len(line):

                # Top
                match = re.search(regex, fileContents[i-1][x.span()[0]-1:x.span()[1]])
                print("Top: ", fileContents[i-1][x.span()[0]-1:x.span()[1]])
                if match:
                    is_part_number = True
                # Mid
                match = re.search(regex, fileContents[i][x.span()[0]-1:x.span()[1]])
                print("Mid: ", fileContents[i][x.span()[0]-1:x.span()[1]])
                if match:
                    is_part_number = True

            # If the potential part number is neither left most or right most:
            # Then check 3digit: 7/12, 2digit: 6/10
            else:
                # Check middle left and right:
                match = re.search(regex, fileContents[i][x.span()[0]-1:x.span()[1]+1])
                if match:
                    is_part_number = True
                # Check top 5:
                match = re.search(regex, fileContents[i-1][x.span()[0]-1:x.span()[1]+1])
                print("Top: ", fileContents[i-1][x.span()[0]-1:x.span()[1]+1])
                if match:
                    is_part_number = True
        
        if(is_part_number):
            print("\n{} is a part number".format(x.group()))
            part_number = int(x.group())
            part_number_sum += part_number
            part_numbers.add(part_number)
        else:
            print("\n{} is NOT a part number".format(x.group()))
        is_part_number = False

    unique_total = 0
    for x in part_numbers:
        unique_total += x

    print("Part number sum: ", part_number_sum)
    print("Part number unique sum: ", unique_total)
# Check if the number is a part number
#def check_match():
