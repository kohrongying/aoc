class IntCode:
  def __init__(self, filename):
    # self.file = file
    f = open(filename, 'r')
    lines = f.readlines()
    icodes = lines[0].split(",")
    self.curr_pointer = 0
    self.codes = [int(i) for i in icodes]
    self.length = len(self.codes)
    self.relative_base = 0
    self.memory = {}
    self.curr_pointer = 0
  
  def get_output(self, input, num_outputs):
    outputs = []
    while len(outputs) < num_outputs and self.codes[self.curr_pointer] != 99:
      code = str(self.codes[self.curr_pointer]).zfill(5)
      opcode = int(code[4])
      val1 = self.get_value1(self.curr_pointer, int(code[2]))

      if opcode == 4:
        outputs.append(val1)
        # print('hi', len(outputs))

        self.curr_pointer += 2

      elif opcode == 3:
        store = self.get_write_address(self.curr_pointer, opcode, int(code[2]))
        self.write_to_address(store, input)
        self.curr_pointer += 2

      elif opcode == 9:
        self.relative_base += val1
        self.curr_pointer += 2

      elif opcode == 1:
        val2 = self.get_value2(self.curr_pointer, int(code[1]))
        store = self.get_write_address(self.curr_pointer, opcode, int(code[0]))
        val = val1 + val2
        self.write_to_address(store, val)
        self.curr_pointer += 4

      elif opcode == 2:
        val2 = self.get_value2(self.curr_pointer, int(code[1]))
        store = self.get_write_address(self.curr_pointer, opcode, int(code[0]))
        val = val1 * val2
        self.write_to_address(store, val)
        self.curr_pointer += 4
      
      elif opcode == 5:
        val2 = self.get_value2(self.curr_pointer, int(code[1]))
        if val1 != 0:
          self.curr_pointer = val2
        else:
          self.curr_pointer += 3

      elif opcode == 6:
        val2 = self.get_value2(self.curr_pointer, int(code[1]))
        if val1 == 0:
          self.curr_pointer = val2
        else:
          self.curr_pointer += 3

      elif opcode == 7:
        val2 = self.get_value2(self.curr_pointer, int(code[1]))
        store = self.get_write_address(self.curr_pointer, opcode, int(code[0]))
        if val1 < val2:
          self.write_to_address(store, 1)
        else:
          self.write_to_address(store, 0)
        self.curr_pointer += 4

      elif opcode == 8:
        val2 = self.get_value2(self.curr_pointer, int(code[1]))
        store = self.get_write_address(self.curr_pointer, opcode, int(code[0]))
        if val1 == val2:
          self.write_to_address(store, 1)
        else:
          self.write_to_address(store, 0)
        self.curr_pointer += 4

      else:
        pass
        # print(ValueError(f'invalid opcode {self.codes[pointer]}'))
    return outputs

  def get_value1(self, pointer, mode):
    param1 = self.codes[pointer + 1]
    if mode == 0:
      if param1 < self.length:
        return self.codes[param1]
      return self.memory[param1] if param1 in self.memory else 0
    elif mode == 1:
      return param1
    elif mode == 2:
      if self.relative_base + param1 < self.length:
        return self.codes[self.relative_base + param1]
      return self.memory[self.relative_base + param1] if self.relative_base + param1 in self.memory else 0
    else:
      print(f"Invalid mode for param 1 at {pointer}")
      return ValueError(f"Invalid mode for param 1 at {pointer}" )

  def get_value2(self, pointer, mode):
    param2 = self.codes[pointer + 2]
    if mode == 0:
      if param2 < self.length:
        return self.codes[param2]
      return self.memory[param2] if param2 in self.memory else 0
    elif mode == 1:
      return param2
    elif mode == 2:
      if self.relative_base + param2 < self.length:
        return self.codes[self.relative_base + param2]
      return self.memory[self.relative_base + param2] if self.relative_base + param2 in self.memory else 0
    else:
      print(f"Invalid mode for param 2 at {pointer}")
      return ValueError(f"Invalid mode for param 2 at {pointer}" )

  def get_write_address(self, pointer, opcode, mode):
    if mode == 0:
      if opcode == 3:
        return self.codes[pointer + 1]
      elif opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
        return self.codes[pointer + 3]

    elif mode == 2:
      if opcode == 3:
        return self.relative_base + self.codes[pointer + 1]
      elif opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
        return self.relative_base + self.codes[pointer + 3]
    else:
      print(f"Invalid mode for param 3 at {pointer}")
      return ValueError(f"Invalid mode for param 3 at {pointer}" )

  def write_to_address(self, index, val):
    if index < self.length:
      self.codes[index] = val
    else:
      self.memory[index] = val