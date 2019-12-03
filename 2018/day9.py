game_state = ([0], 0)

def add_marble(arr, current_marble_index, x):
  if len(arr) < current_marble_index + 2:
    if len(arr) == 0:
      index_to_insert = 0
    else:
      index_to_insert = current_marble_index + 2 - len(arr)
  else:
    index_to_insert = current_marble_index + 2
  arr.insert(index_to_insert, x)
  return arr, index_to_insert

def remove_marble(arr, current_marble_index):
  new_marble_index = current_marble_index - 7
  if new_marble_index < 0:
    new_marble_index = len(arr) - 7 + current_marble_index

  removed_marble = arr.pop(new_marble_index)
  return (arr, new_marble_index), removed_marble

def make_list(s):
  a = s.split(' ')
  temp = []
  index = 0 
  curr = 0
  for i in a:
    if i!='':
      if len(i)>2:
        first, back = i.split('(')
        temp.append(int(first))
        index+=1
        mid, end = back.split(')')
        temp.append(int(mid))
        curr = index
        index+=1
        if end!='':
          temp.append(int(end))
          index+=1
        
      else:
        temp.append(int(i))
      index += 1

  print(temp)
  print(curr)

def get_new_player(num_players, current_player_index):
  if current_player_index == num_players-1:
    return 0
  return current_player_index + 1

def get_highest_score(scores):
  return max(i for i in scores)

def build_game(num_players, last_marble):
  # game_state = ([0], 0) #array and curr marble index
  player_scores = [0 for i in range(num_players)] #score
  current_player_index = 0
  for i in range(1,last_marble+1):
    if i%23==0:
      game_state, score = remove_marble(game_state[0], game_state[1])
      player_scores[current_player_index] += i + score
    else:
      game_state = add_marble(game_state[0], game_state[1], i)

    if current_player_index < (num_players -1):
      current_player_index += 1 
    else:
      current_player_index = 0    
  return player_scores

class Node:
  def __init__(self, data, leftNode=None, rightNode=None ):
    self.data = data 
    self.left = leftNode
    self.right = rightNode
  def __repr__(self):
    return repr(self.data)

def add_node(i, currNode): 
  thatNode = currNode.right.right 
  newNode = Node(i, currNode.right, thatNode)
  thatNode.left = newNode
  currNode.right.right = newNode
  return newNode
  
def remove_node(currNode):
  toDel = currNode.left.left.left.left.left.left.left
  newCurrNode = toDel.right
  toDel.left.right = newCurrNode
  newCurrNode.left = toDel.left
  return newCurrNode, toDel.data

def doubly_linked_list():
  num_players = 429
  last_marble = 70901
  player_scores = [0 for i in range(num_players)] #score
  current_player_index = 0

  n0 = Node(0)
  n1 = Node(1, n0, n0)
  n0.right = n1
  n0.left = n1 
  currNode = n1
  for i in range(2,last_marble+1):
    if i%23==0:
      currNode, score = remove_node(currNode)
      player_scores[current_player_index] += i + score
    else:
      currNode = add_node(i, currNode)
    current_player_index = get_new_player(num_players, current_player_index)
  print(get_highest_score(player_scores))

doubly_linked_list()