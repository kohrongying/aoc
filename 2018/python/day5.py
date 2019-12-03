import string 
def check_polarity(a, b):
  if a.islower() and a.upper()==b:
    return True
  else: 
    if a.isupper() and a.lower()==b:
      return True 
  return False

def react_polymer(polymer):
  temp = ""
  to_remove = []
  for i in range(len(polymer)):
    if i != len(polymer)-1:
      if check_polarity(polymer[i], polymer[i+1]):
        if i not in to_remove:
          to_remove.append(i)
          to_remove.append(i+1)
  
  temp = removeUnits(polymer, to_remove)
  if len(temp)==len(polymer):
    return polymer
  else:
    return react_polymer(temp)

def react_polymer2(polymer):
  temp = polymer
  length = 0
  while length != len(temp):
    length = len(temp)
    to_remove = []
    for i in range(len(temp)):
      if i != len(temp)-1:
        if check_polarity(temp[i], temp[i+1]):
          if i not in to_remove:
            to_remove.append(i)
            to_remove.append(i+1)
    
    temp = removeUnits(temp, to_remove)
  return temp

def removeUnits(polymer, ind):
  temp = ""
  for i in range(len(polymer)):
    if i not in ind:
      temp += polymer[i]
  return temp

def remove_letter_from_polymer(polymer, letters):
  return polymer.translate(None, ''.join(letters))
  # temp = ""
  # for i in polymer: 
  #   if i.lower()!=letter:
  #     temp += i 
  # return temp

def part2():
  alphabet = list(string.ascii_lowercase)
  # alphabet = ['x']
  polymer = open('day5_short.txt', 'r').readline()
  shortest_polymer_length = 11724
  for letter in alphabet: 
    new_polymer = remove_letter_from_polymer(polymer, [letter, letter.upper()])
    reacted_polymer = react_polymer(new_polymer)
    length = len(reacted_polymer)
    if length < shortest_polymer_length:
      shortest_polymer_length = length
    print("{} has length of {}".format(letter, length))
  return shortest_polymer_length

# part2()
print(len(react_polymer2(open('day5_noX.txt', 'r').readline())))
# print(len(open('day5_noX.txt', 'r').readline()))
