import re

def solve1(input):
  grid = [['o' for z in range(1500)] for k in range(1500)]
  overlapped = 0
  for claim in input:
    split = re.match(r'#\d+ @ (\d+),(\d+): (\d+)x(\d+)', claim)
    startX, startY, width, height = map(int, [split[1], split[2], split[3], split[4]])
    # print('claim: %s X: %s Y: %s width: %s height: %s' % (claimID, startX, startY, width, height))
    for x in range(startX, (startX + width)):
      for y in range(startY, (startY + height)):
        if grid[x][y] == 'o':
          grid[x][y] = 'x'
        elif grid[x][y] == 'x':
          grid[x][y] = '-'
          overlapped += 1
  print(overlapped)
    
with open ('day3-input.txt', 'r') as data:
  input = data.read().splitlines()
  solve1(input)