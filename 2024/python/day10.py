from typing import Tuple

inp = []
num_cols, num_rows = 0, 0


def read_inputs(filename):
    with open(f'input/{filename}', 'r') as f:
        for line in f.readlines():
            inp.append([int(x) for x in line.strip()])
    global num_rows, num_cols
    num_rows = len(inp)
    num_cols = len(inp[0])


def solve1():
    total_score = 0
    for i, row in enumerate(inp):
        for j, col in enumerate(row):
            total_score += len(get_trailhead_score(-1, (i, j), set()))
    print('Ans: ', total_score)


def is_valid_coordinate(t):
    return 0 <= t[0] < num_cols and 0 <= t[1] < num_rows


def get_trailhead_score(prev_height: int, curr_pos: Tuple[int, int], summits: set[Tuple[int, int]]) -> set[
    Tuple[int, int]]:
    if not is_valid_coordinate(curr_pos):
        return set()
    curr_height = inp[curr_pos[0]][curr_pos[1]]
    if curr_height - prev_height != 1:
        return set()
    if curr_height == 9:
        summits.add(curr_pos)
        return summits

    up = (curr_pos[0] - 1, curr_pos[1])
    right = (curr_pos[0], curr_pos[1] + 1)
    down = (curr_pos[0] + 1, curr_pos[1])
    left = (curr_pos[0], curr_pos[1] - 1)
    return get_trailhead_score(curr_height, up, summits) | \
        get_trailhead_score(curr_height, right, summits) | \
        get_trailhead_score(curr_height, down, summits) | \
        get_trailhead_score(curr_height, left, summits)


def get_trailhead_score2(prev_height: int, curr_pos: Tuple[int, int]) -> int:
    if not is_valid_coordinate(curr_pos):
        return 0
    curr_height = inp[curr_pos[0]][curr_pos[1]]
    if curr_height - prev_height != 1:
        return 0
    if curr_height == 9:
        return 1

    up = (curr_pos[0] - 1, curr_pos[1])
    right = (curr_pos[0], curr_pos[1] + 1)
    down = (curr_pos[0] + 1, curr_pos[1])
    left = (curr_pos[0], curr_pos[1] - 1)
    return get_trailhead_score2(curr_height, up) + \
        get_trailhead_score2(curr_height, right) + \
        get_trailhead_score2(curr_height, down) + \
        get_trailhead_score2(curr_height, left)


def solve2():
    total_score = 0
    for i, row in enumerate(inp):
        for j, col in enumerate(row):
            total_score += get_trailhead_score2(-1, (i, j))
    print('Ans: ', total_score)


if __name__ == "__main__":
    line = read_inputs('day10.txt')
    solve1()
    solve2()
    # print(get_trailhead_score(-1, (0, 0), set()))
