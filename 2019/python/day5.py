
def solve(input):
  f = open('../input/day5.txt', 'r')
  lines = f.readlines()
  icodes = lines[0].split(",")
  pointer = 0
  codes = []
  for i in icodes:
    codes.append(int(i))
  output = 0
  while codes[pointer] != 99:
    code = str(codes[pointer])
    code = code.zfill(5)
    opcode = int(code[4])
    
    mode1 = int(code[2])
    param1 = codes[pointer + 1]
    val1 = param1 if mode1 else codes[param1]

    if opcode == 2:
      mode2 = int(code[1])
      param2 = codes[pointer + 2]
      val2 = param2 if mode2 else codes[param2]
      store = codes[pointer + 3]

      val = val1 * val2
      codes[store] = val
      pointer += 4
    elif opcode == 1:
      mode2 = int(code[1])
      param2 = codes[pointer + 2]
      val2 = param2 if mode2 else codes[param2]
      store = codes[pointer + 3]

      val = val1 + val2
      codes[store] = val
      pointer += 4
    elif opcode == 4:
      if val1 != 0:
        print(val1)
        return ValueError(f'Output not zero!')
      else:
        output = val1
      pointer += 2
    elif opcode == 3: 
      val = input
      store = codes[pointer + 1]
      codes[store] = val
      pointer += 2
    else:
      return ValueError(f'invalid opcode {codes[pointer]}')
    # print(f'code: {code}, val1: {val1}, val: {val}, pointer: {pointer},')

def solve2(input):
  f = open('../input/day5.txt', 'r')
  lines = f.readlines()
  icodes = lines[0].split(",")
  pointer = 0
  codes = []
  for i in icodes:
    codes.append(int(i))

  while codes[pointer] != 99:
    code = str(codes[pointer])
    code = code.zfill(5)
    opcode = int(code[4])
    
    mode1 = int(code[2])
    param1 = codes[pointer + 1]
    val1 = param1 if mode1 else codes[param1]

    if opcode == 4:
      if val1 != 0:
        print(val1)
        return ValueError(f'Output not zero!')
      else:
        output = val1
      pointer += 2
    elif opcode == 3: 
      val = input
      store = codes[pointer + 1]
      codes[store] = val
      pointer += 2
    else:
      mode2 = int(code[1])
      param2 = codes[pointer + 2]
      val2 = param2 if mode2 else codes[param2]

      if opcode == 5:
        if val1 != 0:
          pointer = val2
        else:
          pointer += 3
      elif opcode == 6:
        if val1 == 0:
          pointer = val2
        else:
          pointer += 3
      else:
        store = codes[pointer + 3]
        if opcode == 2:
          val = val1 * val2
          codes[store] = val
          pointer += 4
        elif opcode == 1:
          val = val1 + val2
          codes[store] = val
          pointer += 4
        elif opcode == 7:
          codes[store] = 1 if val1 < val2 else 0
          pointer += 4
        elif opcode == 8:
          codes[store] = 1 if val1 == val2 else 0
          pointer += 4
        else:
          return ValueError(f'invalid opcode {codes[pointer]}')