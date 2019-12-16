from intcode import IntCode
import copy

def get_coor(move, curr_pos):
  x, y = curr_pos
  if move == 1:
    return (x, y+1)
  elif move == 2:
    return (x, y-1)
  elif move == 3:
    return (x-1, y)
  else:
    return (x+1, y)

# moves is a list of integers
def walk_curr_move(intcode, curr_move):
  x = 0
  y = 0
  for i in curr_move:
    out = intcode.get_output(i, 1)[0]
    if out == 0:
      return ValueError("Path should not contain wall")
    if i == 1:
      y += 1
    elif i == 2:
      y -= 1
    elif i == 3:
      x -= 1
    elif i == 4:
      x += 1
    else:
      return ValueError("Invalid move")
  return intcode, (x,y)
    
movement_commands = [1, 2, 3, 4]
walls = set()
# north=1 , south=2, west=3, east=4
opp = {
  1: 2,
  2: 1,
  3: 4,
  4: 3,
}
queue = []
seen = [(0,0)]

def initialise_queue():
  curr_pos = (0, 0)
  for m in movement_commands:
    comp = IntCode('../input/day15.txt')
    output = comp.get_output(m, 1)[0]
    if output == 2:
      new_pos = get_coor(m, curr_pos)
      found = new_pos
      print('found')
    elif output == 1:
      new_pos = get_coor(m, curr_pos)
      seen.append(new_pos)
      queue.append([m])

def solve():
  initialise_queue()
  while len(queue) > 0:
    curr_move = queue.pop(0)
    comp = IntCode('../input/day15.txt')

    comp, curr_pos = walk_curr_move(comp, curr_move)

    for m in movement_commands:
      output = comp.get_output(m, 1)[0]
      if output == 2:
        found = get_coor(m, curr_pos)
        print('num moves', len(curr_move) + 1)
        queue = []
        break
      elif output == 1:
        new_move = copy.deepcopy(curr_move)
        new_move.append(m)
        new_pos = get_coor(m, curr_pos)
        if new_pos not in seen:
          seen.append(new_pos)
          queue.append(new_move)
        comp.get_output(opp[m], 1)

def build_map():
  initialise_queue()
  while len(queue) > 0:
    curr_move = queue.pop(0)
    comp = IntCode('../input/day15.txt')
    comp, curr_pos = walk_curr_move(comp, curr_move)
    for m in movement_commands:
      output = comp.get_output(m, 1)[0]
      if output == 0:
        new_pos = get_coor(m, curr_pos)
        walls.add(new_pos)
      else:
        if output == 2:
          found = get_coor(m, curr_pos)
        new_move = copy.deepcopy(curr_move)
        new_move.append(m)
        new_pos = get_coor(m, curr_pos)
        if new_pos not in seen:
          seen.append(new_pos)
          queue.append(new_move)
        comp.get_output(opp[m], 1)
  print('found', found)

  f = open('day15-out2.txt', 'w')
  f.write(f'{found[0]} {found[1]} O\n')
  for i in walls:
    f.write(f'{i[0]} {i[0]} #\n')
  for j in seen:
    f.write(f'{i[0]} {i[0]} .\n')


def solve2():
  f = open('day15-out.txt', 'r')
  lines = f.readlines()
  walls = set()
  available = set()
  oxygen = set()

  for line in lines:
    x, y, c = line.strip().split(' ')
    x = int(x)
    y = int(y)
    if c == 'O':
      oxygen.add((x, y))
    elif c == '#':
      walls.add((x, y))
    else:
      available.add((x, y))

  def find_adjacent(pos):
    x, y = pos
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

  time = 0
  while True:
    adj_set = set()
    for tile in oxygen:
      adj_set.update(find_adjacent(tile))

    # remove infected from available set
    adj_set = adj_set - walls
    available = available - (adj_set)

    # add infected to oxygen set
    oxygen = oxygen.union(adj_set)
    time += 1
    if len(available) == 0:
      break
  print('time taken', time)