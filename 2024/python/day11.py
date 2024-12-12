def solve1(inp, blink_count):
    line = [int(x) for x in inp.strip().split(' ')]
    count = 0
    while count < blink_count:
        num_stones = len(line)
        curr_stone_idx = 0
        while curr_stone_idx < num_stones:
            num = line[curr_stone_idx]
            if num == 0:
                line[curr_stone_idx] = 1
            elif len(str(num)) % 2 == 0:
                line[curr_stone_idx] = int(str(num)[:len(str(num)) // 2])
                line.append(int(str(num)[len(str(num)) // 2:]))
            else:
                line[curr_stone_idx] = num * 2024
            curr_stone_idx += 1
        count += 1
    print('Ans', len(line))


def recurse(num: int, num_blink: int, d={}) -> int:
    if num_blink == 1:
        return 2 if len(str(num)) % 2 == 0 else 1

    key = f'{num}:{num_blink}'
    if key in d:
        return d[key]

    if len(str(num)) % 2 == 0:
        half_1, half_2 = int(str(num)[:len(str(num)) // 2]), int(str(num)[len(str(num)) // 2:])
        key_1 = f'{half_1}:{num_blink - 1}'
        key_2 = f'{half_2}:{num_blink - 1}'
        d[key_1] = recurse(half_1, num_blink - 1, d)
        d[key_2] = recurse(half_2, num_blink - 1, d)
        return d[key_1] + d[key_2]
    elif num == 0:
        key = f'1:{num_blink - 1}'
        d[key] = recurse(1, num_blink - 1, d)
        return d[key]
    key = f'{num * 2024}:{num_blink - 1}'
    d[key] = recurse(num * 2024, num_blink - 1, d)
    return d[key]


if __name__ == "__main__":
    puzzle_inp = '6571 0 5851763 526746 23 69822 9 989'
    # solve1(puzzle_inp, 75)
    line = [int(x) for x in puzzle_inp.strip().split(' ')]
    t = 0
    for x in line:
        t += recurse(x, 1000)
    print('Ans', t)
