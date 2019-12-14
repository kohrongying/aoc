from intcode import IntCode

def get_new_position(curr_pos, curr_dir, turn):
  x, y = curr_pos
  if turn: # Turn Right
    new_dir = curr_dir + 1 if curr_dir != 4 else 1
  else: # Turn Left
    new_dir = curr_dir - 1 if curr_dir != 1 else 4
  if new_dir == 1:
    new_pos = (x, y+1)
    return new_dir, new_pos
  elif new_dir == 2:
    new_pos = (x+1, y)
    return new_dir, new_pos
  elif new_dir == 3:
    new_pos = (x, y-1)
    return new_dir, new_pos
  elif new_dir == 4:
    new_pos = (x-1, y)
    return new_dir, new_pos
  else:
    return ValueError("Invalid direction")
    
panels = {}
comp = IntCode('../input/day11.txt')
curr_position = (0,0)
curr_color = 1
curr_direction = 1

while True:
  outputs = comp.get_output(curr_color, 2)
  if len(outputs) != 2:
    break
  color, turn = outputs
  panels[curr_position] = color
  curr_direction, curr_position = get_new_position(curr_position, curr_direction, turn)
  if curr_position in panels:
    curr_color = panels[curr_position]
  else:
    curr_color = 0

# PART 1
print(len(panels))

# PART 2
for k in panels:
  if panels[k] == 1:
    print(k)