f = open('../input/day9.txt', 'r')
lines = f.readlines()
icodes = lines[0].split(",")
curr_pointer = 0
codes = [int(i) for i in icodes]
length = len(codes)
relative_base = 0
memory = {}


def get_value1(pointer, mode):
  param1 = codes[pointer + 1]
  if mode == 0:
    if param1 < length:
      return codes[param1]
    return memory[param1] if param1 in memory else 0
  elif mode == 1:
    return param1
  elif mode == 2:
    if relative_base + param1 < length:
      return codes[relative_base + param1]
    return memory[relative_base + param1] if relative_base + param1 in memory else 0
  else:
    return ValueError(f"Invalid mode for param 1 at {pointer}" )

def get_value2(pointer, mode):
  param2 = codes[pointer + 2]
  if mode == 0:
    if param2 < length:
      return codes[param2]
    return memory[param2] if param2 in memory else 0
  elif mode == 1:
    return param2
  elif mode == 2:
    if relative_base + param2 < length:
      return codes[relative_base + param2]
    return memory[relative_base + param2] if relative_base + param2 in memory else 0
  else:
    return ValueError(f"Invalid mode for param 2 at {pointer}" )

def get_write_address(pointer, opcode, mode):
  if mode == 0:
    if opcode == 3:
      return codes[pointer + 1]
    elif opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
      return codes[pointer + 3]

  elif mode == 2:
    if opcode == 3:
      return relative_base + codes[pointer + 1]
    elif opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
      return relative_base + codes[pointer + 3]
  else:
    return ValueError(f"Invalid mode for param 3 at {pointer}" )

def write_to_address(index, val):
  if index < length:
    codes[index] = val
  else:
    memory[index] = val

input = 2
while codes[curr_pointer] != 99:
  code = str(codes[curr_pointer]).zfill(5)
  opcode = int(code[4])
  # print('pointer', curr_pointer)
  val1 = get_value1(curr_pointer, int(code[2]))

  if opcode == 4:
    print(val1)
    curr_pointer += 2

  elif opcode == 3:
    store = get_write_address(curr_pointer, opcode, int(code[2]))
    write_to_address(store, input)
    curr_pointer += 2

  elif opcode == 9:
    relative_base += val1
    curr_pointer += 2

  elif opcode == 1:
    val2 = get_value2(curr_pointer, int(code[1]))
    store = get_write_address(curr_pointer, opcode, int(code[0]))
    val = val1 + val2
    write_to_address(store, val)
    curr_pointer += 4

  elif opcode == 2:
    val2 = get_value2(curr_pointer, int(code[1]))
    store = get_write_address(curr_pointer, opcode, int(code[0]))
    val = val1 * val2
    write_to_address(store, val)
    curr_pointer += 4
  
  elif opcode == 5:
    val2 = get_value2(curr_pointer, int(code[1]))
    if val1 != 0:
      curr_pointer = val2
    else:
      curr_pointer += 3

  elif opcode == 6:
    val2 = get_value2(curr_pointer, int(code[1]))
    if val1 == 0:
      curr_pointer = val2
    else:
      curr_pointer += 3

  elif opcode == 7:
    val2 = get_value2(curr_pointer, int(code[1]))
    store = get_write_address(curr_pointer, opcode, int(code[0]))
    if val1 < val2:
      write_to_address(store, 1)
    else:
      write_to_address(store, 0)
    curr_pointer += 4

  elif opcode == 8:
    val2 = get_value2(curr_pointer, int(code[1]))
    store = get_write_address(curr_pointer, opcode, int(code[0]))
    if val1 == val2:
      write_to_address(store, 1)
    else:
      write_to_address(store, 0)
    curr_pointer += 4

  else:
    print(ValueError(f'invalid opcode {codes[pointer]}'))
