def get_power_level(x, y, sn):
  rack_id = x + 10
  power_level = rack_id * y
  power_level += sn 
  power_level = power_level * rack_id
  if power_level>99:
    digit = int(list(str(power_level))[-3])
  else: 
    digit = 0
  return digit - 5 

def build_cells(sn):
  cells = []
  for i in range(300):
    temp = []
    for j in range(300):
      power = get_power_level(i, j, sn)
      temp.append(power)
    cells.append(temp)
  return cells

def get_three_by_three(x, y, cells):
  total = 0
  for j in range(y, y+3):
    for i in range(x, x+3):
      total += cells[j][i]
  return total

def get_largest_power(sn):
  cells = build_cells(sn)
  table = get_summed_area_table(cells)
  largest = 0
  coor = []
  for i in range(0,298):
    for j in range(0,298):
      num = get_three_by_three(i,j, cells)
      if num > largest:
        largest = num
        coor = [i, j]
  return coor[1], coor[0]

def get_summed_area_table(cells):
  new = []
  for j in range(len(cells)):
    temp = []
    for i in range(len(cells)):
      if i ==0 and j ==0:
        prev = cells[j][i]
        temp.append(prev)
      elif i!=0 and j ==0:
        prev += cells[j][i]
        temp.append(prev)
      elif i==0 and j !=0:
        prev = cells[j][i]
        temp.append(new[-1][i] + prev)
      else:
        prev += cells[j][i]
        temp.append(new[-1][i] + prev)
    new.append(temp)
    # print(temp)
  return new

# table = get_summed_area_table([[31,2,4,33,5,36],[12,26,9,10,29,25],[13,17,21,22,20,18],[24,23,15,16,14,19],[30,8,28,27,11,7],[1,35,34,3,32,6]])

def get_largest_power_square(sn):
  cells = build_cells(sn)
  table = get_summed_area_table(cells)
  largest = 0
  coor = []
  for k in range(1,301):
    for i in range(0,300-k+1):
      for j in range(0,300-k+1):
        num = get_square(j, i, k, table)
        if num > largest:
          largest = num
          coor = [j,i,k]
  return coor[1], coor[0], coor[2]

def get_square(x,y,k,cells):
  d = cells[y+k-1][x+k-1]
  x_small = max(0, x-1)
  y_small = max(0, y-1)
  a = cells[y_small][x_small]
  b = cells[y_small][x+k-1]
  c = cells[y+k-1][x_small]
  # print("{} {} {} {}".format(a,b,c,d))
  return d+a-b-c

# print(get_square(2,3,3,table))