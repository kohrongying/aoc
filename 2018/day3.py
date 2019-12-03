claims = {}

def create_2d_matrix(row, col):
  temp = []
  for i in range(row):
    row_array = []
    for j in range(col):
      row_array.append([])
    temp.append(row_array)
  return temp

def print_matrix(mat):
  for i in mat:
    print(i)

def parse_file(file):
  f = open(file, 'r')

  fabric = create_2d_matrix(1000,1000)
  for line in f.readlines():
    index, remainder = line.split("@")
    num = index.strip()[1:]
    coor, grid = remainder.strip().split(":")
    x, y = coor.split(",")
    x = int(x)
    y = int(y)
    dx, dy = grid.strip().split('x')
    claims[num] = int(dx) * int(dy)
    for i in range(int(dx)):
      for j in range(int(dy)):
        fabric[y+j][x+i].append(num)
  return fabric

def createDict(num):
  d = {}
  for i in range(1, num+1):
    d[str(i)]=0
  return d

def get_num_overlap(mat):
  total = 0
  for row in mat:
    for col in row:
      if len(col) >= 2:
        total+=1
  return total

def get_non_overlap(mat):
  d = createDict(1411)
  singles = {}
  for row in mat:
    for col in row:
      if len(col)==1:
        if col[0] in singles:
          singles[col[0]]+=1
        else:
          singles[col[0]]=1
  for k in singles: 
    if singles[k] == claims[k]:
      return k
  return None

# print_matrix(parse_file('day3.txt'))
print(get_num_overlap(parse_file('test.txt')))
# print(get_non_overlap(parse_file('day3.txt')))