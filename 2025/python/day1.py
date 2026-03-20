def solve1(filename):
    with open(filename) as f:
        lines = f.readlines()
    pt = 50
    counter = 0
    for line in lines:
        line = line.strip()
        if line[0] != 'L' and line[0] != 'R':
            raise Exception(f'invalid input {line}')
        dir = 1 if line[0] == 'R' else -1
        val = int(line[1:])
        pt += dir * (val%100)
        if pt > 99:
            pt = pt - 100
        elif pt < 0:
            pt = 100 - abs(pt)
        if pt == 0:
            counter += 1
        # print(pt, val, counter)
    print(counter)
    return counter

def solve2(filename):
    with open(filename) as f:
        lines = f.readlines()
    pt = 50
    counter = 0
    for line in lines:
        line = line.strip()
        pt, c = spin(pt, line)
        counter += c
    print(f'final counter is {counter}')
    return counter
        
def spin(pt, line):
    orig = pt
    # counter = 0
    dir = 1 if line[0] == 'R' else -1
    dist = int(line[1:])
    counter = dist // 100 # handle quotient of cycles first
    pt += dir * (dist % 100)
    if pt > 99:
        pt = pt - 100
        # counter += 1
    elif pt < 0:
        pt = 100 - abs(pt)
        # if orig != 0:
        #     counter += 1
    # elif pt == 0 and orig != 0:
    #     counter += 1
    
    # handle the remainder
    if dist % 100 != 0:
        if pt == 0: # from 50 move L50
            counter += 1
            
        # from +ve cross to -ve
        elif orig != 0 and (orig + dir * (dist % 100)) * pt < 0: # crossed 0
            counter += 1
        
        # from -ve cross to +ve
        elif (orig + dir * (dist % 100)) > 99:
            counter += 1 

    # print(pt, counter)
    return pt, counter
    
assert spin(0, 'L5') == (95, 0)
assert spin(0, 'L100') == (0, 1)
assert spin(50, 'L50') == (0, 1)
assert spin(50, 'L68') == (82, 1)
assert spin(95, 'R60') == (55, 1)
