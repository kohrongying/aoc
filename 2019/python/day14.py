import math

f = open('../input/test.txt', 'r')
lines = f.readlines()
reactions = {}
"""
FUEL : {
  quantity: 1,
  ingredients: [ (AB, 2), (BC, 3)]
}
"""
for line in lines:
  ingredients, prod = line.strip().split("=>")
  pcount, product = prod.strip().split(" ")
  ingredients = ingredients.split(",")
  ilist = []
  for i in ingredients:
    icount, ingredient = i.strip().split(" ")
    ilist.append((ingredient, int(icount)))
  reactions[product] = {
    'quantity': int(pcount),
    'ingredients': ilist
  }

def solve(num_fuel):
  surplus = { }
  total_ore = 0
  deque = []
  starting_ingredients = [(key[0], key[1]*num_fuel) for key in reactions['FUEL']['ingredients']]
  deque.extend(starting_ingredients)
  while len(deque) != 0:
    chemical, quantity_needed = deque.pop(0)
    if chemical == 'ORE':
      total_ore += quantity_needed
    else:
      quantity_produced = reactions[chemical]['quantity']
      ingredients = reactions[chemical]['ingredients']
      if chemical in surplus:
        quantity_needed -= surplus[chemical]
        surplus[chemical] = 0
      multiple = math.ceil(quantity_needed / quantity_produced)
      surplus[chemical] = multiple * quantity_produced - quantity_needed
      for ingredient in ingredients:
        ingredient_name, ingredient_quantity = ingredient
        deque.append((ingredient_name, multiple * ingredient_quantity))
  return total_ore


def solve2():
  ore_per_fuel = solve(1)
  print('ore per fuel', ore_per_fuel)
  total_ore = 1000000000000
  total_fuel = math.floor(total_ore / ore_per_fuel) 
  mintry = total_fuel
  maxtry = total_fuel * 2
  guess = mintry

  while maxtry - mintry > 1:
    guess = (maxtry + mintry) // 2
    ore_needed = solve(guess)
    if ore_needed > total_ore:
      maxtry = guess
    else:
      mintry = guess
  check = solve(guess)
  if check > total_ore:
    return guess - 1
  return guess

print('fuel produced', solve2())