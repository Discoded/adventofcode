# https://adventofcode.com/2023/day/2
import re
try: 
    # Open file containing the words separated by a line
    theFile = open("./day2.txt")
    #theFile = open("./message.txt")
    #theFile = open("./day2-practice.txt")
    
except:
    print("NO FILE")

def calculate_power_sum(red, green, blue):
    power = red*green*blue
    return power


def main():
    RED_LIMIT = 12
    GREEN_LIMIT = 13
    BLUE_LIMIT = 14

    highest_red = 0
    highest_green = 0
    highest_blue = 0

    total_id = 0
    power_sum = 0

    for line in theFile:
        print(line, end='')
        m = re.match("(Game )+(?P<game_id>[0-9]*[0-9])", line)
        game_id = m.group("game_id")
        print("game_id: ", game_id)
        m = re.findall("\d*\d red|\d*\d green|\d*\d blue", line)
        print(m)

        isPossible = True
        
        for x in m:
            # ['3', 'red'] or ['1', 'green'] or ['6', 'blue']
            roll = x.split(" ")
            cube_value = int(roll[0])
            if (roll[1] == 'red'):
                if (cube_value > highest_red):
                    highest_red = cube_value
                if (cube_value > RED_LIMIT):
                    print("RED COUNT NOT POSSIBLE")
                    isPossible = False
            elif (roll[1] == 'green'):
                if (cube_value > highest_green):
                    highest_green = cube_value
                if (int(cube_value) > GREEN_LIMIT):
                    print("GREEN COUNT NOT POSSIBLE")
                    isPossible = False
            elif (roll[1] == 'blue'):
                if (cube_value > highest_blue):
                    highest_blue = cube_value
                if (int(cube_value) > BLUE_LIMIT):
                    print("BLUE COUNT NOT POSSIBLE")
                    isPossible = False

        if isPossible:
            #print("NOT POSSIBLE")
            total_id += int(game_id)
        
        isPossible = True

        print("Highest value of red: ", highest_red)
        print("Highest value of green: ", highest_green)
        print("Highest value of blue: ", highest_blue)

        power = calculate_power_sum(highest_red, highest_green, highest_blue)
        

        power_sum += power

        print("Power: ", power)
        print("Power sum: ", power_sum)

        highest_red = 0
        highest_green = 0
        highest_blue = 0
    print("total_id: ", total_id)

main()

    # For each character in the string, check if it's a digit (regex '^[0-9]')
    # for char in line:
    #     # If it's a digit, append it as a character to variable count
    #     if re.match(digitPattern, char):
    #         count += char
    # print(count)

    # # Take the first and last digit and combine them
    # finalDigit = count[0] + count[-1]

    # # Add the two-digit number to the total
    # totalCount += int(finalDigit)

    # print(count)
    # print(finalDigit + '\n')

    # # Reset temporary variables
    # count = ""
    # finalDigit = ""