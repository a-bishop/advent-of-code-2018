from string import ascii_lowercase
from collections import Counter

def solve1(polymers):
  newPolymers = []
  for letter in polymers:
    if letter.isupper():
      if len(newPolymers) == 0:
        newPolymers.append(letter)
      elif (letter.lower() != newPolymers[-1]):
        newPolymers.append(letter)
      else:
        newPolymers.pop()
    elif letter.islower():
      if len(newPolymers) == 0:
        newPolymers.append(letter)
      elif (letter.upper() != newPolymers[-1]):
        newPolymers.append(letter)
      else:
        newPolymers.pop()
  return len(newPolymers)

def solve2(polymers):
  lengthCount = Counter()
  for letter in ascii_lowercase:
    bufString = ''
    for polymer in polymers:
      if polymer.lower() != letter:
        bufString += polymer
    lengthCount[letter] = solve1(bufString)
  return lengthCount.most_common()[-1]

with open ('day5-input.txt', 'r') as f:
  mainPolymers = f.read().strip()
  print(solve1(mainPolymers))
  print(solve2(mainPolymers))