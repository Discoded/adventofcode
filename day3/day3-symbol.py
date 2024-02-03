# https://adventofcode.com/2023/day/3
import re
try: 
    # Open file containing the words separated by a line
    #theFile = open("./day3.txt")
    theFile = open("./day3-practice.txt")
    
except:
    print("NO FILE")



after_line = ""


# O(n)..?
fileContents = theFile.read().split('\n')

#print(fileContents)

is_part_number = False
part_number_sum = 0
part_numbers = set()
#regex = "[^.\d]"
regex = "@|#|\$|%|&|\*|\+|=|-|/"

# Take off 1st line
global previous_line 
previous_line = fileContents.pop(0)

# For each line in the file
for i, line in enumerate(fileContents):
    print(i, line, end="\n\n")

    # Find numbers
    # If number:  
    m = re.finditer(regex, line)  

    # ..35.633.
    # (2, 4], (6, 9]
    # @, #, $, %, &, *,

    for x in m:
        print("\nspan: ",x.span())
        print("Symbol: ", x.group(), end="\n")
        pos = x.span()
        beg = pos[0] + -1
        end = pos[1] + 1
        print("beg end",beg, end)
        numbers = re.finditer("\d*\d*\d", previous_line[beg:end])

        for y in numbers:
            print("y.span(): ",y.span())
            print("NUMBER: ", previous_line[x.span()[0]:])

            if(y.span() == (0, 1)):
                # Check if left or right edge
                if(x.span()[0] > 2 and x.span()[1] < previous_line.__len__):   
                    print("(0, 1) NUMBER: ", previous_line[x.span()[0]-3:x.span()[0]])
                # If left or right edge..
                else:
                    print("left or right edge")
            


            elif(y.span() == (1, 3)):
                print("(1, 3) NUMBER: ", previous_line[x.span()[0]:x.span()[0]+y.span()[1]])

    previous_line = line

        
# Check if the number is a part number
#def check_match():
