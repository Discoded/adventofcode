import re
testString = '2tqbxgrrpmxqfglsqjkqthree6nhjvbxpflhr1eightwohr'

digitPattern = '^[0-9]'
wordPattern = '(?=(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(\d))'
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

def helperFunc(word):
    if word.isdigit():
        return word
    else:
        return wordToNumber[word]



test = re.findall(wordPattern, testString)
print(test)



finalNumber = ''
for x in test:
    for y in x:
        if y != '':
            finalNumber += helperFunc(y)
print(finalNumber)