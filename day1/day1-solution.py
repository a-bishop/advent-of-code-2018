
def solve1(input):
  print(sum(list(map(int, input))))

def solve2(input):
  sum = 0
  mySet = {sum}
  freqs = list(map(int, input))
  while True:
    for freq in freqs:
      sum += freq
      if sum in mySet:
        print(sum)
        return
      mySet.add(sum)

with open ('day1-input.txt', 'r') as data:
  input = data.read().splitlines()
  solve1(input)
  solve2(input)