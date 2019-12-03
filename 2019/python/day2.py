import copy

f = open('../input/day2.txt', 'r')
lines = f.readlines()
new_codes = lines[0].split(",")
codes_copy = []
for i in new_codes:
  codes_copy.append(int(i))

def get_output(codes):
  pointer = 0
  while codes[pointer] != 99:
    
    arg1 = codes[codes[pointer + 1]]
    arg2 = codes[codes[pointer + 2]]
    store = codes[pointer + 3]

    if codes[pointer] == 1:
      val = arg1 + arg2
    elif codes[pointer] == 2:
      val = arg1 * arg2
    else:
      break
    codes[store] = val
    pointer += 4

  return codes[0]

def solve2():
  for i in range(157):
    for j in range(157):
      codes = copy.deepcopy(codes_copy)
      codes[1] = i
      codes[2] = j
      if get_output(codes) == 19690720:
        print(i, 'i')
        print(j, 'j')
