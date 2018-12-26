with open ('day2-input.txt', 'r') as data:
  input = data.read().splitlines()
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