import re

def solve1():
  grid1 = [[0 for z in range(1500)] for k in range(1500)]
  result = 0
  for claim in claims:
    for x in range(claim[1], claim[1] + claim[3]):
      for y in range(claim[2], claim[2] + claim[4]):
        grid1[x][y] += 1
  for col in grid1:
    for rowItem in col:
      if rowItem > 1:
        result += 1
  return(result)

def solve2():
  grid2 = [[0 for z in range(1500)] for k in range(1500)]
  not_overlapping = set()
  for claim in claims:
    not_overlapping.add(claim[0])
  for claim in claims:
    for x in range(claim[1], claim[1] + claim[3]):
      for y in range(claim[2], claim[2] + claim[4]):
        if grid2[x][y] != 0:
          if claim[0] in not_overlapping:
            not_overlapping.remove(claim[0])
          if grid2[x][y] in not_overlapping:
            not_overlapping.remove(grid2[x][y])
        else:
          grid2[x][y] = claim[0]
  return list(not_overlapping)
    
with open ('day3-input.txt', 'r') as data:
  input = data.read().splitlines()
  claims = []
  for string in input:
    split = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', string)
    [claimID, startX, startY, width, height] = map(int, [split[1], split[2], split[3], split[4], split[5]])
    claims.append([claimID, startX, startY, width, height])
  print(solve1())
  print(solve2())