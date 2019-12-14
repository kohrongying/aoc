import copy

f = open('../input/day12.txt', 'r')
lines = f.readlines()
moons = []
for line in lines:
  coors = line.strip()[1:-1].split(', ')
  position = []
  for coor in coors:
    var, pos = coor.split('=')
    position.append(int(pos))
  moons.append({'position': position, 'velocity': [0,0,0]})

def update_velocity(curr_moon_index):
  curr_moon = moons[curr_moon_index]
  curr_moon_velocity = curr_moon['velocity']
  curr_moon_position = curr_moon['position']
  for i, moon in enumerate(moons):
    if i != curr_moon_index:
      for i in range(3):
        if curr_moon_position[i] > moon['position'][i]:
          curr_moon_velocity[i] -= 1
        elif curr_moon_position[i] < moon['position'][i]:
          curr_moon_velocity[i] += 1
  return copy.deepcopy(curr_moon['velocity'])

def update_position(curr_moon_index):
  curr_moon = moons[curr_moon_index]
  curr_moon_velocity = curr_moon['velocity']
  curr_moon_position = curr_moon['position']
  for i in range(3):
    curr_moon_position[i] += curr_moon_velocity[i]

def calc_kinetic_energy(velocity):
  return sum(abs(i) for i in velocity)

def calc_potential_energy(position):
  return sum(abs(i) for i in position)

def calc_total_energy():
  total_energy = 0
  for moon in moons:
    ke = calc_kinetic_energy(moon['velocity'])
    pe = calc_potential_energy(moon['position'])
    total_energy += ke * pe
  return total_energy

def find_moon_period():
  moon_periods = [0, 0 ,0, 0]
  velocities = [[], [], [], []]
  steps = 0
  TOTAL_STEPS = 1000000
  while steps != TOTAL_STEPS:
  # while 0 in moon_periods:
    for i in range(len(moons)):
      velocity = update_velocity(i)
      # if len(velocities[i]) > 0:
      #   if velocity == velocities[i][0] and moon_periods[i] == 0:
      #     print(i, velocity)
      #     moon_periods[i] = len(velocities[i])
      velocities[i].append(velocity)
    for i in range(len(moons)):
      update_position(i)
    steps += 1
  
  output = open('day12-output2.txt', 'w')
  for i in velocities[2]:
    output.write(str(i[2])+', ')
    
    # print(i)
  # print(moon_periods)


def solve():
  steps = 0
  TOTAL_STEPS = 1000

  while steps != TOTAL_STEPS:
    for i in range(len(moons)):
      update_velocity(i)
    for i in range(len(moons)):
      update_position(i)
    steps += 1

  print(calc_total_energy())

## TODO
def lcm(numbers):
  pass

## TODO
def cycle_detection(arr):
  pass

# def solve2():

f = open('../input/test.txt', 'r')
lines = f.readlines()[0].split(',')
print(len(lines))

# find_moon_period()
#  286332 96236 193052
# 332,477,126,821,644