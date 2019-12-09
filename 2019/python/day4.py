from itertools import groupby

def has_adjacent(num):
  l = list(str(num))
  for i in range(len(l)-1):
    if l[i] == l[i+1]:
      return True
  return False

def is_increasing(num):
  l = list(str(num))
  return l == sorted(l)

# Compress 112233 into [2,2,2]
# Make use of groupby from itertools
def custom_rle(num):
  rle = []
  for k, i in groupby(str(num)):
    rle.append(len(list(i)))
  return rle

def solve():
  total = 0
  for i in range(256310, 732736+1):
    if is_increasing(i) and has_adjacent(i):
      total += 1
  print(total)

def solve2():
  total = 0
  for i in range(256310, 732736+1):
    if is_increasing(i) and 2 in custom_rle(i):
      total += 1
  print(total)