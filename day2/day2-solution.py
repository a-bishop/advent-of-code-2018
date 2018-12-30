from collections import Counter

def solve1(input):
  totalCount2, totalCount3 = 0, 0
  for string in input:
    twoUncounted, threeUncounted = True, True
    c = Counter(string)
    for k, v in c.items():
      if (v == 2) & twoUncounted:
        totalCount2 += 1
        twoUncounted = False
      if (v == 3) & threeUncounted:
        totalCount3 += 1
        threeUncounted = False
  print(totalCount2 * totalCount3)

def solve2(input):
  startingIndex = 1
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
  