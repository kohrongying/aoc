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
def solve():
  surplus = { }
  total_ore = 0
  deque = []
  deque.extend(reactions['FUEL']['ingredients'])
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
  # print('ore needed', total_ore)
  return total_ore, surplus
