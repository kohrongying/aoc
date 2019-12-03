def parse_line(line):
  return line.strip().split(' => ')[0]
  
def build_patterns_list(file):
  f = open(file, 'r')
  patterns = []
  for line in f.readlines():
    patterns.append(parse_line(line))
  return patterns

def get_pattern(i, state):
  if i == 0: 
    return ".."+state[0:3]
  elif i == 1:
    return "."+state[0:4]
  elif i == len(state)-1:
    return state[-3:]+".."
  elif i == len(state)-2:
    return state[-4:]+"."
  else:
    return state[i-2:i+3]

def match_pattern(pattern, patterns):
  if pattern in patterns:
    return True
  return False 


patterns = build_patterns_list('day12-test.txt')

# initial_state = "#.#.#....##...##...##...#.##.#.###...#.##...#....#.#...#.##.........#.#...#..##.#.....#..#.###"
initial_state = "#..#.#..##......###...###"
for i in range(20):
  new_state=""
  for j in range(len(initial_state)):
    pattern = get_pattern(j, initial_state)
    # print(pattern)
    if match_pattern(pattern, patterns):
      new_state+="#"
    else:
      new_state+="."
  initial_state = new_state
  print(initial_state)
