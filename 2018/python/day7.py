import copy

def parse_line(line):
  a, b = line.strip().split(" must be finished before step ")
  return a[-1], b[0]

def parse_file(file):
  f = open(file, 'r')
  temp = []
  for line in f.readlines():
    temp.append(parse_line(line))
  return temp

def get_all_elements(arr):
  s = set()
  for i in arr:
    for j in i:
      s.add(j)
  return list(s)

def get_dependent_elements(arr):
  s = set()
  for i in arr:
    s.add(i[1])
  return list(s)

def get_independent_elements(arr, dep):
  set1 = set(arr)
  set2 = set(dep)
  a = list(set1-set2)
  a.sort()
  return a

def find_indep_steps(arr, indep):
  temp = []
  for i in arr:
    if i[0] == indep:
      temp.append(i)
  return temp

def sort_steps(arr):
  arr.sort(key=lambda x : x[1].lower())
  return arr

def remove_indep_steps(arr, indep):
  temp = []
  for i in arr:
    if i[0] != indep:
      temp.append(i)
  return temp

def get_order(file):
  arr = parse_file(file)
  order = ""
  all_elements = get_all_elements(arr)
  total_elements = all_elements
  dep_elements = get_dependent_elements(arr)
  stack = get_independent_elements(all_elements, dep_elements)
  # print(stack)
  while stack != []:
    letter = stack.pop(0)
    # print(letter+' is popped')
    order += letter
    arr = remove_indep_steps(arr, letter)
    dep_elements = get_dependent_elements(arr)
    all_elements = get_all_elements(arr)
    stack = set(stack)
    stack.update(get_independent_elements(all_elements, dep_elements))
    stack = sorted(stack)
    # print(stack)
    # print('curr ordr '+order)
  
  e = get_last_element(total_elements, order)
  order += e
  return order

def get_time(file):
  arr = parse_file(file)
  order = ""
  all_elements = get_all_elements(arr)
  total_elements = all_elements
  dep_elements = get_dependent_elements(arr)
  stack = get_independent_elements(all_elements, dep_elements)
  workers = []
  curr_time = 0
  order = ""
  needed_workers = min(5, len(stack))
  for i in range(needed_workers):
    letter = stack[i]
    workers.append((letter, curr_time + ord(letter)-4))
  
  stack = stack[5:]

  while len(order) < 25:
    workers.sort(key=lambda x : x[1])
    letter, t = workers.pop(0)
    # print('{} is popped'.format(letter))
    # print('time is now {}'.format(curr_time))
    order += letter
    curr_time = t

    arr = remove_indep_steps(arr, letter)
    dep_elements = get_dependent_elements(arr)
    all_elements = get_all_elements(arr)
    stack = set(stack)
    stack.update(get_independent_elements(all_elements, dep_elements))
    stack = remove_workers_from_stack(workers,list(stack))
    # print(stack)
    avail_workers = min(len(stack), (5 - len(workers)))
    for i in range(avail_workers):
      letter = stack.pop(0)
      if check_workers(letter,workers):
        workers.append((letter, curr_time + ord(letter)-4))
    # print(order)
    # print(workers)
  
  e = get_last_element(total_elements, order)
  curr_time += ord(e)-4
    
  return curr_time

def remove_workers_from_stack(workers, stack):
  temp = copy.deepcopy(stack)
  for i in stack:
    for j in workers:
      if i == j[0]:
        temp.remove(i)
  temp.sort()
  return temp


def check_workers(letter, workers):
  for i in workers:
    if letter == i[0]:
      return False
  return True

def get_last_element(arr, s):
  for i in arr: 
    if i not in s:
      return i

print(get_time('day7.txt'))