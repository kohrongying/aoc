def solve1(filename):
    m = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            n = []
            for c in line.strip():
                if c != '\n':
                    n.append(c)
            m.append(n)
    
    counter = 0
    num_changes = 0
    iteration = 1
    while num_changes != 0 or counter == 0:
        print()
        num_changes = 0
        for i, row in enumerate(m):
            for j, col in enumerate(row):
                if m[i][j] == '@' and is_accessible(m, i, j):
                    counter += 1
                    num_changes += 1
                    m[i][j] = '.'
        iteration += 1
        print(f'Iteration {iteration}: {counter}')
                    
    print(counter)
    return counter
    
def is_accessible(m, i, j):
    rolls = get_adjacent_values(m, i, j)
    counter = 0
    for r in rolls:
        if r == '@':
            counter += 1 
    return counter < 4

def get_adjacent_values(m, i, j):
    return [
        get_value_at(m, i-1, j-1),
        get_value_at(m, i-1, j),
        get_value_at(m, i-1, j+1),
        get_value_at(m, i, j-1),
        get_value_at(m, i, j+1),
        get_value_at(m, i+1, j-1),
        get_value_at(m, i+1, j),
        get_value_at(m, i+1, j+1),
    ]

def get_value_at(m, i, j):
    if i < 0 or i >= len(m) or j < 0 or j >= len(m[0]):
        return '.'
    return m[i][j]

