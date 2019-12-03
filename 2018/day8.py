
def parse_line(line):
  input = [int(i) for i in line.split(' ')]
  entries_sum = 0
  num_child = input.pop(0)
  num_entries = input.pop(0)
  children = [[num_child,num_entries]]

  while input != []:
    children[-1][0] = children[-1][0]-1
    num_child = input.pop(0)
    num_entries = input.pop(0)
    if num_child == 0:
      for i in range(num_entries):
        entries_sum += input.pop(0)
    else:
      children.append([num_child, num_entries])
    
    no_child = children[-1][0]
    while no_child == 0:
      for i in range(children[-1][1]):
        entries_sum += input.pop(0)
      children.pop()
      if len(children)>=1:
        no_child = children[-1][0]
      else:
        break
  return entries_sum

# print(parse_line("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"))

def build_tree(line):
  input = [int(i) for i in line.split(' ')]
  num_child = input.pop(0)
  num_entries = input.pop(0)
  children = [[num_child,num_entries]]
  nodes = [{'children':[], 'entries':[], 'num_child': num_child, 'num_entries': num_entries, "value": 0}]

  while input != []:
    parentNode = nodes[-1]
    
    num_child = input.pop(0)
    num_entries = input.pop(0)
    currentNode = {'children':[], 'entries':[], 'num_child': num_child, 'num_entries': num_entries, 'value':0}

    parentNode['num_child'] -= 1
    if num_child == 0:
      val = 0
      for i in range(num_entries):
        val += input.pop(0)
      currentNode['value'] = val
      parentNode['children'].append(currentNode)
    else: 
      nodes.append(currentNode)

    lastNode = nodes[-1]
    
    while lastNode['num_child'] == 0 and len(nodes) >=1:
      for i in range(lastNode['num_entries']):
        lastNode['entries'].append(input.pop(0))
       
      if len(nodes) >1:
        currentParentNode = nodes.pop()
        lastNode = nodes[-1]
        lastNode['children'].append(currentParentNode)
      else:
        break
  return nodes[0]

def get_value(node):
  if node['children']==[]:
    return node['value']
  else:
    total = 0
    entries_list = node['entries']
    for i in entries_list:
      if i <= len(node['children']):
        total += get_value(node['children'][i-1])
    node['value'] = total
  return node['value']


node = build_tree(open('day8.txt','r').readline())
# get_value()
# print(build_tree("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"))
