import re
testString = '2tqbxgrrpmxqfglsqjkqthree6nhjvbxpflhr1eightwohr'

digitPattern = '^[0-9]'
wordPattern = '(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)'
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

def dictionary(m):
    number = wordToNumber[m.group(0)]
    return str(number)
print(testString)
print(re.sub(wordPattern, dictionary, testString))