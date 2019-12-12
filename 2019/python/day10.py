import math

def build_asteroid():
  f = open('../input/day10.txt', 'r')
  lines = f.readlines()
  asteroids = []
  for index, line in enumerate(lines):
    col_index = index
    row = list(line)
    for row_index, char in enumerate(row):
      if char == '#':
        asteroids.append((row_index, col_index))
  return asteroids

# Contains both a gradient and a direction
def calc_vector(point1, point2):
  return (calc_gradient(point1, point2), calc_direction(point1, point2))

def calc_direction(point1, point2):
  x1, y1 = point1
  x2, y2 = point2
  if x2 > x1:
    return 'R'
  elif x2 == x1:
    if y2 > y1:
      return 'U'
    return 'D'
  return 'L'

def calc_gradient(point1, point2):
  x1, y1 = point1
  x2, y2 = point2
  if x2-x1 == 0:
    return 'inf'
  if y2-y1 == 0:
    return 0
  return (y2-y1)/(x2-x1)

def calc_magnitude(point1, point2):
  x1, y1 = point1
  x2, y2 = point2
  return ((y2-y1)**2 + (x2-x1)**2)**0.5

def find_quadrant(point1, point2):
  x1, y1 = point1
  x2, y2 = point2
  if x2 == x1 and y2 < y1:
    return 1
  elif x2 > x1 and y2 < y1:
    return 2
  elif x2 > x1 and y2 == y1:
    return 3
  elif x2 > x1 and y2 > y1:
    return 4
  elif x2 == x1 and y2 > y1:
    return 5
  elif x2 < x1 and y2 > y1:
    return 6
  elif x2 < x1 and y2 == y1:
    return 7
  else:
    return 8

def calc_angle(point1, point2):
  x1, y1 = point1
  x2, y2 = point2
  quad = find_quadrant(point1, point2)
  if quad == 1:
    return 0
  elif quad == 3: 
    return 90
  elif quad == 5:
    return 180
  elif quad == 7: 
    return 270
  elif quad == 2:
    angle = math.degrees(math.atan(abs(y2-y1)/ abs(x2-x1)))
    return 90 - angle
  elif quad == 4:
    angle = math.degrees(math.atan(abs(y2-y1)/ abs(x2-x1)))
    return 90 + angle
  elif quad == 6:
    angle = math.degrees(math.atan(abs(y2-y1)/ abs(x2-x1)))
    return 270 - angle
  else:
    angle = math.degrees(math.atan(abs(y2-y1)/ abs(x2-x1)))
    return 270 + angle

def calc_vector2(point1, point2):
  return calc_angle(point1, point2), calc_magnitude(point1, point2)

def solve(asteroids):
  d = {}
  for asteroid in asteroids:
    for ast in asteroids:
      if asteroid != ast:
        gradient = calc_vector(asteroid, ast)
        if asteroid not in d:
          d[asteroid] = set([gradient])
        else:
          d[asteroid].add(gradient)

  best_position = max(d, key=lambda x: len(d[x]))
  max_asteroids = max(len(d[key]) for key in d)
  
  print(best_position)
  print(max_asteroids)

def solve2(asteroids):
  base = (14, 17)
  positions = {}
  for asteroid in asteroids:
    if asteroid != base:
      angle, magnitude = calc_vector2(base, asteroid)
      if angle in positions:
        positions[angle].append((magnitude, asteroid))
      else:
        positions[angle] = [(magnitude, asteroid)]
  
  # sort all key values by order of magnitude
  for angle in positions:
    positions[angle] = sorted(positions[angle], key=lambda k: (k[0]))

  # sort keys by angle (smallest angle first)
  order = sorted(positions.keys())
  order_index = 200 % len(order) - 1
  asteroid_index = math.floor(200 / len(order))

  # Answer
  print(positions[order[order_index]][asteroid_index])


# asteroids = build_asteroid()
# solve2(asteroids)