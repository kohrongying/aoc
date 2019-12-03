
def get_coordinates(line):
  x, y = line.strip().split(', ')
  return int(x), int(y) 

def parse_file(file):
  f = open(file, 'r')
  coors = []
  largest_x = 0
  largest_y = 0 
  for line in f.readlines():
    x, y = get_coordinates(line)
    if x > largest_x: 
      largest_x = x 
    if y > largest_y:
      largest_y = y
    coors.append((x,y))
  return coors

def manhattan_distance(x1, y1, x2, y2):
  return abs(x1-x2) + abs(y1-y2)

def get_closest_coor(x, y, coors):
  shortest_distance = 100000
  closest_coor = 0
  for i, val in enumerate(coors): 
    x_i = val[0]
    y_i = val[1]
    dist = manhattan_distance(x,y, x_i, y_i)
    if dist < shortest_distance:
      shortest_distance = dist
      closest_coor = i
    elif dist == shortest_distance: 
      closest_coor = '.'
  return closest_coor

def parse_grid():
  coors = parse_file('day6.txt')
  length = len(coors)
  points = [0 for i in range(length)]
  bounded_points = find_bounded_points(coors)
  min_x, min_y, max_x, max_y = get_bounded_coors(coors)
  for i in range(min_x, max_x+1):
    for j in range(min_y, max_y+1):
      point = get_closest_coor(i, j, coors)
      if check_edge(i, j, min_x, min_y, max_x, max_y):
        if point in bounded_points:
          bounded_points.remove(point)
      if point != '.':
        points[point] +=1  
  temp = [points[i] for i in bounded_points]
  return max(temp)

def check_edge(x, y, min_x, min_y, max_x, max_y):
  if x == min_x or x == max_x or y == min_y or y == max_y:
    return True
  return False

def find_bounded_points(coors):
  temp = []
  min_x, min_y, max_x, max_y = get_bounded_coors(coors)
  for i, val in enumerate(coors):
    if val[0] > min_x and val[0] < max_x and val[1] > min_y and val[1] < max_y:
      temp.append(i)
  return temp

def get_bounded_coors(coors):
  min_x = min(coors, key = lambda t: t[0])[0]
  min_y = min(coors, key = lambda t: t[1])[1]
  max_x = max(coors, key = lambda t: t[0])[0]
  max_y = max(coors, key = lambda t: t[1])[1]
  return min_x, min_y, max_x, max_y

def get_region():
  coors = parse_file('day6.txt')
  min_x, min_y, max_x, max_y = get_bounded_coors(coors)
  region_size = 0
  for i in range(min_x, max_x+1):
    for j in range(min_y, max_y+1):
      # print(get_manhantan_sum(i, j, coors))
      if get_manhantan_sum(i, j, coors) < 10000:
        region_size += 1
  return region_size

def get_manhantan_sum(x, y, coors):
  total = 0
  for i in coors:
    total += manhattan_distance(x, y, i[0], i[1]) 
  return total
