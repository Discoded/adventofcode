# [Advent of Code 2023](https://adventofcode.com/2023/)

# [Day 1](https://adventofcode.com/2023/day/1)

### Day 1 Part 1 
#### Input:
```
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
```
#### Output:
```
12
38
15
77
```
Final answer: **142** (sum total of each line output)

#### Solution:
```
Parse each character on each line and check if it's a digit
Return once you find the first digit,
Start from the end or reverse the string
Return once you find the first digit(last digit)
```
### Day 1 Part 2
#### Input:
```
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

```
#### Output:
```
29
93
13
24
42
14
76
```
Final answer: **281** (sum total of each line output)

#### Solution:

```
In each line, find strings: "one", "two", .... 'nine",
Replace each found string as '1', '2', '3', ... '9'
Run solution for Part 1
```

# [Day 2](https://adventofcode.com/2023/day/2)

The Elf would first like to know which games would have been possible if the bag contained only **12** red cubes, **13** green cubes, and **14** blue cubes?

#### Input:

```
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
```

#### Output:

```
Game 1: possible
Game 2: possible
Game 3: NOT possible
Game 4: NOT possible
Game 5: possible
```
Final answer: **8** (sum of game IDs that were possible (1+2+5=8))


#### Solution:

```
MAX_RED_NUMBER = 12
MAX_GREEN_NUMBER = 13
MAX_BLUE_NUMBER = 14

For each line
    store game_id
    Split: string by "n color",
        For each color:
            Check color:
                if max_color_number < current_number:
                    game_is_not_possible_ = true
            if game_is_not_possible:
                return
            else:
                game_id_sum += game_id
```

### Day 2 Part 2

As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

#### Input:

```
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
```
#### Output:

```
Game 1: 4*2*6 = 48
Game 2: 1*3*4 = 12
Game 3: 20*13*6 = 1560
Game 4: 14*3*2 = 630
Game 5: 6*3*2 = 36
```
Final answer: **2286** (Sum of the powers of each min color in each line(48+12+1560+630+36))

#### Solution:
```
For each line
    store game_id
    Split: string by "n color",
        For each color:
            Check color:
                if red:
                    if min_red < current_number:
                        min_red = current_number
                elif green:
                    if min_green < current_number:
                        min_green = current_number
                // blue
                else:
                    if min_blue < current_number:
                        min_blue = current_number
                if max_color_number < current_number:
                    game_is_not_possible_ = true
            if game_is_not_possible:
                return
            else:
                game_id_sum += game_id

```
# [Day 3](https://adventofcode.com/2023/day/3)

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can **add up all the part numbers** in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently **any number adjacent to a symbol**, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Input:
```
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
```

Output:

```
467, 35, 633, 617, 592, 755, 664, 598
```

Final answer: **4361** (Sum of the part numbers 467+35+633...+598)

#### Solution:

Two rare cases: 
    First line doesnt have a line above it
    Last line does not have a line below it
Another two cases where the number is directly on the edge, in which the slot directly left or right does not exist.
There are also cases where these two are combined.


```
Case 1 (First Line):
-----------------------
467. or .114.  or ..114
...*    .....     .....
-----------------------

Regular Case:
-----------------------
..*.    .....    .....    ....
.35. or .633. or 633.. or .633
....    .#...    #....    #...
-----------------------
Case 2 (Last Line):
-----------------------
...$.    .*...     ..*..
.664. or .598. or  ..598
------------------------
```

```
Handle first and last case.
Handling base case:
    For each line, find symbol:
        if symbol, check the 9 adjacent spots:
            If number found, find the whole number,
            Add to sum
            
```


# [Day 4](https://adventofcode.com/2023/day/4)

The Elf leads you over to the pile of colorful cards. There, you discover dozens of scratchcards, all with their opaque covering already scratched off. Picking one up, it looks like each card has two lists of numbers separated by a vertical bar (|): a list of **winning numbers** and then a list of **numbers you have**. You organize the information into a table (your puzzle input).

As far as the Elf has been able to figure out, you have to figure out which of the **numbers you have** appear in the list of **winning numbers**. The first match makes the card worth **one point** and each match after the first **doubles** the point value of that card.

#### Input:

```
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
```
#### Output:
```
Card 1: 41, 48, 83, 86 -> 2^(4-1) = 8
Card 2: 32, 61 -> 2^(2-1) = 2
Card 3: 1, 21 -> 2^(2-1) = 2
Card 4: 84 -> 2^0 = 1
Card 5: 0
Card 6: 0
```
Final answer: **13** (Sum total of points)

#### Solution: 
```
Split each line into winning_numbers and owned_numbers
for x in winning_numbers:
            for y in owned_numbers:
                if(x == y):
                    points += 1
    sum_of_points += 2^(points - 1)
```

## Day 4 Part 2

There's no such thing as "points". Instead, scratchcards only cause you to win more scratchcards equal to the number of winning numbers you have.

Specifically, you win copies of the scratchcards below the winning card equal to the number of matches. So, if card 10 were to have 5 matching numbers, you would win one copy each of cards 11, 12, 13, 14, and 15.

Copies of scratchcards are scored like normal scratchcards and have the same card number as the card they copied. So, if you win a copy of card 10 and it has 5 matching numbers, it would then win a copy of the same cards that the original card 10 won: cards 11, 12, 13, 14, and 15. This process repeats until none of the copies cause you to win any more cards. (Cards will never make you copy a card past the end of the table.)

```
Assuming you have:
    the list of points for each card: points_list
        where points_list[i] = total points on the ith card
    
Create a list where each card represent a copy of each card, the_duplicates = [0, 1, 1, ..., 1]
```
```py
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
                # Checks if the extra card is not past the end of the table
                # (Cards will never make you copy a card past the end of the table.)
                if not (i+x > len(points_list)-1):
                    the_duplicates[i+x] += 1
```

# [Day 5](https://adventofcode.com/2023/day/5) 

## Part 1

### Input:

```
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
```

### Output


Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location **82**.

Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location **43**.

Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location **86**.

Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location **35**.

Final answer: **35** (minimum location number)

### Solution
Simple solution: go through each map with the starting seed to get the location.

MapN(Map3(Map2(Map1(seed))))

#### Map Handling
```
Given a map (destination, source, range):
50 98 2
52 50 48

Map can be stored as
map: [[50, 98, 2], [52, 50, 48]]

def Map(key): value:
    for elem in map:
        if elem[1] + elem[2] - 1 >= key >=  elem[1]:
            return  key - elem[1] + elem[0]

```




## Part 2
- [ ] Find THE Map which Maps seed to location, (Merge maps)
- [x] Reduce Seeds instead of manually inputting each seed invidually
    

