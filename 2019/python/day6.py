f = open('../input/day6.txt', 'r')
lines = f.readlines()
d = {}

def print_dict(d):
  for key in d:
    print(f'{key}: {d[key]}')

# Build a tree of key [orbiter]: value [parent]
# Each planet has exactly ONE parent
def build_tree():
  for line in lines:
    station, orbiter = line.strip().split(")")
    if station not in d:
      d[station] = None
    d[orbiter] = station

# Build a tree of key [orbiter]: 
# {
#   parent: value
#   children: [value]
# }
def build_tree_with_children():
  for line in lines:
    station, orbiter = line.strip().split(")")
    if station not in d:
      d[station] = {
        'parent': None,
        'children': [orbiter]
      }
    else:
      d[station]['children'].append(orbiter)
    if orbiter not in d:
      d[orbiter] = {
        'parent': station,
        'children': []
      }
    else:
      d[orbiter]['parent'] = station

# recursion to find path to origin (COM)
def walk_tree(station, path_length=0):
  if d[station] is None:
    return path_length
  else:
    path_length += 1
    station = d[station]
    return walk_tree(station, path_length)

def solve():
  build_tree()
  print(sum(walk_tree(station) for station in d))

def solve2():
  build_tree_with_children()
  origin = d['YOU']['parent']
  dest = d['SAN']['parent']
  # Initialise a queue for visiting planets
  seen = [origin]
  # Keep a dictionary of path lengths from origin
  dists = { origin: 0 }

  while len(seen) != 0:
    current_station = seen.pop(0)
    count = dists[current_station] + 1
    neighbours = []
    if d[current_station]['parent'] is not None:
      neighbours.append(d[current_station]['parent'])
      neighbours.extend(d[current_station]['children'])
      for n in neighbours:
        if n != dest:
          if n not in dists:
            seen.append(n)
            dists[n] = count
        else:
          print(count)
          break

solve2()