# steps = 1004, current_post = (x, y)
def left(steps, current_pos):
  coors = []
  x, y = current_pos
  for i in range(1, steps+1):
    coors.append((x-i,y))
  final_pos = (x-steps, y)
  return coors, final_pos

def right(steps, current_pos):
  coors = []
  x, y = current_pos
  for i in range(1, steps+1):
    coors.append((x+i,y))
  final_pos = (x+steps, y)
  return coors, final_pos

def up(steps, current_pos):
  coors = []
  x, y = current_pos
  for i in range(1, steps+1):
    coors.append((x,y+i))
  final_pos = (x, y+steps)
  return coors, final_pos

def down(steps, current_pos):
  coors = []
  x, y = current_pos
  for i in range(1, steps+1):
    coors.append((x,y-i))
  final_pos = (x, y-steps)
  return coors, final_pos

# Generator
def get_all_coors(path1):
  route = path1.split(",")
  x, y = (0,0)
  for i in route:
    direction = i[0]
    steps = int(i[1:])
    for j in range(steps):
      if direction == 'R':
        x += 1
      elif direction == 'L':
        x -= 1
      elif direction == 'U':
        y += 1
      elif direction == 'D':
        y -= 1
      else:
        return ValueError(f'invalid direction')
      yield x, y

def get_intersections(path1, path2):
  gen1 = get_all_coors(path1)
  gen2 = get_all_coors(path2)
  return set(gen1) & set(gen2) # only for sets - find interesection

def get_manhattan_distance(origin, coor):
  x1, y1 = origin
  x2, y2 = coor
  return abs(x2 - x1) + abs(y2 - y1)

def solve(path1, path2):
  intersects = get_intersections(path1, path2)
  origin = (0,0)
  return min(get_manhattan_distance(origin, coor) for coor in intersects)

def solve2(path1, path2):
  intersects = get_intersections(path1, path2)
  route1 = list(get_all_coors(path1))
  route2 = list(get_all_coors(path2))
  return min((route1.index(coor) + 2 + route2.index(coor)) for coor in intersects)
  
# path1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
# path2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'

# path1 = "R8,U5,L5,D3"
# path2 = "U7,R6,D4,L4"