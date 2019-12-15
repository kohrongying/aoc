from intcode import IntCode

def solve():
  # Change memory address 0 to 1
  comp = IntCode('../input/day13.txt')
  outputs = comp.get_output(0, -1)
  num_tiles = 0
  for i in range(0, len(outputs)-3, 3):
    x, y, tile_id = outputs[i:i+3]
    if tile_id == 2:
      num_tiles += 1
  print(num_tiles)

def solve2():
  comp = IntCode('../input/day13.txt')
  paddle = (None, None)
  ball = (None, None)
  score = 0
  joystick = 0
  while True:
    outputs = comp.get_output(joystick, 3)
    if len(outputs) != 3:
      break
    x, y, tile_id = outputs
    if x == -1 and y == 0:
      score = tile_id
    if tile_id == 3:
      paddle = (x, y)
    elif tile_id == 4:
      ball = (x, y)
      
    if ball[0] is not None and paddle[0] is not None: 
      if ball[0] < paddle[0]:
        joystick = -1
      elif ball[0] > paddle[0]:
        joystick = 1
      else:
        joystick = 0
    else:
      joystick = 0

  print('score', score)