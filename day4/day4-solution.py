import re
import time
from datetime import datetime
from collections import Counter

def most_mins_asleep():
  guardSleep = Counter()
  for line in sortedIn:
    if '#' in line:
      currGuard = guardNum.search(line)[1]
    elif 'asleep' in line:
      startAsleep = datetime.strptime(line[1:17], "%Y-%m-%d %H:%M")
    elif 'wakes' in line:
      endSleep = datetime.strptime(line[1:17], "%Y-%m-%d %H:%M")
      guardSleep[currGuard] += int((endSleep - startAsleep).seconds/60)
  for k,v in guardSleep.most_common(1):
    return k

def solve1():
  minCounter = Counter()
  guardAsleepMost = most_mins_asleep()
  countingMins = False
  for line in sortedIn:
    if guardAsleepMost in line:
      countingMins = True
    if(countingMins):
      if 'asleep' in line:
        startMins = int(mins.search(line)[1])
      elif 'wakes' in line:
        endMins = int(mins.search(line)[1])
        for i in range(startMins, endMins):
          minCounter[i] += 1
      elif ('#' in line) & (guardAsleepMost not in line):
        countingMins = False
  for k,v in minCounter.most_common(1):
    mostMins = int(k)
  return mostMins * int(guardAsleepMost)

def solve2():
  guardMinCounter = Counter()
  for line in sortedIn:
    if '#' in line:
      currGuard = guardNum.search(line)[1]
    elif 'asleep' in line:
      startMins = int(mins.search(line)[1])
    elif 'wakes' in line:
      endMins = int(mins.search(line)[1])
      for i in range(startMins, endMins):
        # the key for the counter is now a list, containing the guard's number and the minute asleep 
        guardMinCounter[currGuard, i] += 1
  for k,v in guardMinCounter.most_common(1):
    return int(k[0]) * int(k[1])

with open ('day4-input.txt', 'r') as data:
  myInput = data.read().splitlines()
  sortedIn = sorted(myInput, key=lambda dt: (time.strptime(dt[6:17], "%m-%d %H:%M")))
  guardNum = re.compile(r'#(\d+)')
  mins = re.compile(r':(\d+)')
  print(solve1())
  print(solve2())
