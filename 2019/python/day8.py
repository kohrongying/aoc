def construct_layers(inp, width, height):
  size = width * height
  data = str(inp)
  layers = []
  for i in range(0, len(data), size):
    digits = data[i:i+size]
    d = {}
    for digit in digits:
      if digit in d:
        d[digit] += 1
      else:
        d[digit] = 1
    layers.append(d)
  return layers

def solve():
  f = open('../input/day8.txt', 'r')
  layers = construct_layers(f.readlines()[0], 25, 6)
  min_layer = {}
  min_zeros = 1000000
  for layer in layers:
    if '0' in layer:
      count = layer['0']
      if count < min_zeros:
        min_layer = layer
        min_zeros = count
    else:
      min_layer = layer
      min_zeros = 0

  ones_count = min_layer['1']
  twos_count = min_layer['2']
  print(ones_count * twos_count)

def get_first_non_transparent(arr):
  for i in arr:
    if i != 2:
      return i
  return arr[0]

def construct_layers2(inp, width, height):
  size = width * height
  data = str(inp)
  layers = []
  for i in range(0, len(data), size):
    layers.append(data[i:i+size])
  return layers

def solve2(inp, width, height):
  layers = construct_layers2(inp, width, height)
  size = width * height
  pixels = []
  for pixel in range(size):
    pix_across_layers = [int(layer[pixel]) for layer in layers]
    final_pix = get_first_non_transparent(pix_across_layers)
    pixels.append(final_pix)

  for i in range(0, len(pixels), width):
    print(pixels[i:i+width])

# f = open('../input/day8.txt', 'r')
# inp = f.readlines()[0]