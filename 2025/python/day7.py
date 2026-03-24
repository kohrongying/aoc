def solve1(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    pos_s = 0
    for i in range(len(lines[0])):
        if lines[0][i] == 'S':
            pos_s = i
            break
    beams = set([pos_s])
    manifold_len = len(lines[0])
    counter = 0
    for i in range(1, len(lines)):
        newbeams = set()
        for beam in beams:
            if lines[i][beam] == '^':
                if beam - 1 >= 0:
                    newbeams.add(beam-1)
                if beam + 1 < manifold_len:
                    newbeams.add(beam+1)
                counter += 1
            else:
                newbeams.add(beam)
        beams = newbeams
        # print(beams)
    print(counter)
    return counter

# Stack does not work as the array grows in size fast
# Using memo / sort also does not help 
# Hence use dict to with [beam_no] = frequency
def solve2(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    stack = {}
    for i in range(len(lines[0])):
        if lines[0][i] == 'S':
            stack[i] = 1
            break
    manifold_len = len(lines[0])
    for i in range(1, len(lines)):
        if i % 2 != 0:
            continue
        level_stack: dict[int, int] = {}
        for beam in stack:
            if lines[i][beam] == '^':
                if beam - 1 >= 0:
                    level_stack[beam-1] = level_stack.get(beam-1,0) + stack[beam]
                if beam + 1 < manifold_len:
                    level_stack[beam+1] = level_stack.get(beam+1,0) + stack[beam]
            else:
                level_stack[beam] = level_stack.get(beam,0) + stack[beam]
        stack = level_stack
    counter = 0
    for k in stack:
        counter += stack[k]
    print(counter)
    return counter
