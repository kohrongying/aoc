

def generate_multiplier(position, pattern, length):
  pat = []
  while True:
    for p in pattern:
      for i in range(position):
        pat.append(p)
        if len(pat) > length:
          return pat[1:]

def get_ones_digit(num):
  return int(str(num)[-1])

def dot_product(a, b):
  return sum([i*j for (i, j) in zip(a, b)])

def solve(input_signal, num_phases):
  pattern = [0, 1, 0, -1]
  input_signal = [int(j) for j in list(str(input_signal))]
  input_length = len(input_signal)
  for i in range(num_phases):
    new_list = [0]*input_length
    for i in range(input_length):
      k_list = generate_multiplier(i+1, pattern, input_length)
      total_sum = dot_product(k_list, input_signal)
      new_list[i] = get_ones_digit(total_sum)
    input_signal = new_list

  return new_list[:8]

def solve2():
  # TODO