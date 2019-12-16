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
  return comp, (x,y)
    
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

