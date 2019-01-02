
def solve1():
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

with open ('day5-input.txt', 'r') as f:
  polymers = f.read().strip()
  newPolymers = []
  print(solve1())
