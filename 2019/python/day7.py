def valid_sequnce(seq):
  if len(set(seq)) != 5:
    return False
  if '5' in seq or '6' in seq or '7' in seq or '8' in seq or '9' in seq:
    return False
  return True

def valid_sequnce2(seq):
  if len(set(seq)) != 5:
    return False
  if '1' in seq or '2' in seq or '3' in seq or '4' in seq or '0' in seq:
    return False
  return True

def solve():
  max_signal = 0
  for i in range(1234, 43210):
    seq = list(str(i).zfill(5))
    if valid_sequnce(seq):
      thrusters = init_thrusters(5)
      phase_sequence = [int(x) for x in seq]
      input_signal = 0
      for i, phase_setting in enumerate(phase_sequence):
        comp = thrusters[i]
        input_signal = comp.get_output(phase_setting, input_signal, 1)[0]
      if input_signal is not None and input_signal > max_signal:
        max_signal = input_signal
  print(max_signal)

class IntCode:
  def __init__(self, filename):
    f = open(filename, 'r')
    lines = f.readlines()
    icodes = lines[0].split(",")
    self.curr_pointer = 0
    self.codes = [int(i) for i in icodes]
    self.length = len(self.codes)
    self.curr_pointer = 0
    self.input_flag = 0
  
  def get_output(self, phase_setting, input, num_outputs):
    outputs = []
    while len(outputs) < num_outputs and self.codes[self.curr_pointer] != 99:
      code = str(self.codes[self.curr_pointer]).zfill(5)
      opcode = int(code[4])
      val1 = self.get_value1(self.curr_pointer, int(code[2]))

      if opcode == 4:
        outputs.append(val1)
        self.curr_pointer += 2

      elif opcode == 3:
        store = self.get_write_address(self.curr_pointer, opcode, int(code[2]))
        if self.input_flag:
          input_val = input
        else:
          input_val = phase_setting
          self.input_flag = 1
        self.write_to_address(store, input_val)
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
      return self.codes[param1]
    elif mode == 1:
      return param1
    else:
      print(f"Invalid mode for param 1 at {pointer}")
      return ValueError(f"Invalid mode for param 1 at {pointer}" )

  def get_value2(self, pointer, mode):
    param2 = self.codes[pointer + 2]
    if mode == 0:
      return self.codes[param2]
    elif mode == 1:
      return param2
    else:
      print(f"Invalid mode for param 2 at {pointer}")
      return ValueError(f"Invalid mode for param 2 at {pointer}" )

  def get_write_address(self, pointer, opcode, mode):
    if mode == 0:
      if opcode == 3:
        return self.codes[pointer + 1]
      elif opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
        return self.codes[pointer + 3]
    else:
      print(f"Invalid mode for param 3 at {pointer}")
      return ValueError(f"Invalid mode for param 3 at {pointer}" )

  def write_to_address(self, index, val):
    self.codes[index] = val

def init_thrusters(num):
  thrusters = []
  for i in range(num):
    comp = IntCode('../input/day7.txt')
    thrusters.append(comp)
  return thrusters

def solve2():
  max_signal = 0
  for i in range(56789, 98766):
    seq = list(str(i).zfill(5))
    if valid_sequnce2(seq):
      output_signals = [0,0,0,0,0]
      thrusters = init_thrusters(5)
      phase_sequence = [int(x) for x in seq]
      input_signal = 0
      thruster_index = 0
      while True:
        comp = thrusters[thruster_index]
        phase_setting = phase_sequence[thruster_index]
        out = comp.get_output(phase_setting, input_signal, 1)
        if len(out) < 1:
          break
        input_signal = out[0]
        output_signals[thruster_index] = input_signal
        thruster_index = (thruster_index + 1) % 5
      
      # Find max thruster signal
      if output_signals[4] > max_signal:
        max_signal = output_signals[4]
  print(max_signal)