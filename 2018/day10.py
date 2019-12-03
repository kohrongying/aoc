from matplotlib import pylab
from pylab import * 

def parse_line(line):
  line=line.strip()
  x, y = line[10:24].split(',')
  v_x, v_y = line[-7:-1].split(',')
  return ([int(x), int(y)], [int(v_x), int(v_y)])

def update_position(x, y, v_x, v_y, seconds):
  new_x = x + seconds * v_x
  new_y = y + seconds * v_y
  return [new_x, new_y]

def parse_file(file):
  f = open(file, 'r')
  initial_positions = []
  velocities = []
  for line in f.readlines():
    initial, velocity = parse_line(line)
    initial_positions.append(initial)
    velocities.append(velocity)
  return initial_positions, velocities

def build_new_positions(seconds):
  initial_positions, velocities = parse_file('day10.txt')
  new_positions = []
  for i in range(len(velocities)):
    new_positions.append(update_position(initial_positions[i][0], initial_positions[i][1], velocities[i][0], velocities[i][1], seconds))
  return new_positions

def manhattan_distance(x1, y1, x2, y2):
  return abs(x1-x2) + abs(y1-y2)

def get_manhantan_sum(x, y, coors):
  total = 0
  for i in coors:
    total += manhattan_distance(x, y, i[0], i[1]) 
  return total

def get_closest_sum():
  minSum = 1000000000000
  second = 0
  for i in range(10054,20000):
    positions = build_new_positions(i)
    total = 0
    for j in positions: 
      total += get_manhantan_sum(j[0], j[1], positions)
    if total < minSum:
      minSum = total
      second = i
      print("After {} second, closest is {}".format(i, total))

get_closest_sum()
def print_message(positions):
  x= []
  y =[]
  for i in positions:
    x.append(i[0])
    y.append(i[1])

  scatter(x,y, s=100, marker='o')
  show()

# positions = build_new_positions(10054)
# print_message(positions)