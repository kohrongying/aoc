from enum import Enum
from functools import reduce
import re

inp = []


def read_inputs():
    with open('input/day3.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            inp.append(line)


class State(Enum):
    CORRUPT = 2
    NOTCORRUPT = 3
    NOTCORRUPTOPEN = 4
    NOTCORRUPTX = 5
    NOTCORRUPTCOMMA = 6
    NOTCORRUPTY = 7
    NOTCORRUPTEND = 8
    DO = 9
    DONT = 10


# Rudimentary state machine sigh
def solve_line(line):
    pointer = 0
    x = y = ''
    stack = []
    state = State.CORRUPT

    def match_target(character, ind):
        target = 'mul('
        return character == target[ind]

    def is_digit(character):
        return character in ('0123456789')

    def corrupt_reset():
        # return state, pointer, x, y
        return State.CORRUPT, 0, '', ''

    for ch in line:
        if state == State.CORRUPT:
            if match_target(ch, 0):
                state = State.NOTCORRUPT
                pointer += 1
        elif state == State.NOTCORRUPT:
            if match_target(ch, pointer):
                pointer += 1
                if pointer == 4:
                    state = State.NOTCORRUPTOPEN
                    pointer = 0
            else:
                state, pointer, x, y = corrupt_reset()
        elif state == State.NOTCORRUPTOPEN:
            if is_digit(ch):
                pointer += 1
                state = State.NOTCORRUPTX
                x += ch
            else:
                state, pointer, x, y = corrupt_reset()
        elif state == State.NOTCORRUPTX:
            if is_digit(ch) and pointer <= 3:
                pointer += 1
                x += ch
            elif ch == ',':
                state = State.NOTCORRUPTCOMMA
                pointer = 0
            else:
                state, pointer, x, y = corrupt_reset()
        elif state == State.NOTCORRUPTCOMMA:
            if is_digit(ch):
                pointer += 1
                state = State.NOTCORRUPTY
                y += ch
            else:
                state, pointer, x, y = corrupt_reset()
        elif state == State.NOTCORRUPTY:
            if is_digit(ch) and pointer <= 3:
                pointer += 1
                y += ch
            elif ch == ')':
                stack.append((int(x), int(y)))
                state, pointer, x, y = corrupt_reset()
            else:
                state, pointer, x, y = corrupt_reset()
    return stack


def solve2v2():
    enabled = True
    newlines = []
    for line in inp:
        new_line = '' # Rebuild the line by removing donts
        donts = [m.start() for m in re.finditer("don't\(\)", line)]
        dos = [m.start() for m in re.finditer("do\(\)", line)]
        curr_index = 0
        while True:
            if enabled:
                try:
                    idx = min([i for i in donts if i > curr_index])
                    new_line += line[curr_index:idx]
                    curr_index = idx
                    enabled = False
                except:
                    new_line += line[curr_index:]
                    break
            else:
                try:
                    idx = min([i for i in dos if i > curr_index])
                    curr_index = idx
                    enabled = True
                except:
                    break
        newlines.append(new_line)
    return newlines


def calc_multiplications(l):
    ans = reduce(lambda a, b: a + b, [tup[0] * tup[1] for tup in l])
    print(ans)


def solve1():
    stack = []
    for line in inp:
        stack = stack + solve_line(line)
    print(stack)
    calc_multiplications(stack)


def solve1v2(lines):
    muls = []
    pattern = 'mul\(\d{1,3},\d{1,3}\)'
    for line in lines:
        muls = muls + re.findall(pattern, line)
    stack = []
    for m in muls:
        cg = 'mul\((\d{1,3}),(\d{1,3})\)'
        x = re.search(cg, m)
        stack.append((int(x.group(1)), int(x.group(2))))
    print(stack)
    calc_multiplications(stack)


if __name__ == "__main__":
    read_inputs()
    # calc_multiplications(solve_line('xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'))
    # solve_line('mul(4*, mul(6,9!, ?(12,34)')
    # solve_line('mul ( 2 , 4 )')
    # solve1()
    # solve1v2()
    # calc_multiplications(solve_line2("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"))
    clean_lines = solve2v2()
    solve1v2(clean_lines)
