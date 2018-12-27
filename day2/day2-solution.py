def solve1(input):
  totalCount2 = 0
  totalCount3 = 0
  for string in input:
    myDict = {}
    count2 = False
    count3 = False
    for letter in string:
      if letter in myDict:
        myDict[letter] += 1
      else:
        myDict[letter] = 1
    for item in myDict:
      if (myDict[item] == 2):
        count2 = True
      elif (myDict[item] == 3):
        count3 = True
    if count2 == True:
      totalCount2 += 1
    if count3 == True:
      totalCount3 += 1
  print(totalCount2 * totalCount3)

def solve2(input):
  startingIndex = 1
  i = 0
  for string in input:
    letters = list(string)
    for index, secondString in enumerate(input, start=startingIndex):
      error = 0
      secondLetters = list(secondString)
      for letter, secondLetter in zip(letters, secondLetters):
        if (letter != secondLetter):
          errorIndex = string.index(letter)
          error += 1
          if error > 1:
            break
      if error == 1:
        letters.pop(errorIndex)
        print(''.join(letters))
    startingIndex += 1

with open ('day2-input.txt', 'r') as data:
  input = data.read().splitlines()
  solve1(input)
  solve2(input)
  