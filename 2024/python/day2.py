# a 2d array
levels = []


def read_inputs():
    with open('input/day2.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            arr = line.split(" ")
            levels.append([int(x) for x in arr])


def get_differences_within_level(level_arr):
    ret = []
    for i in range(1, len(level_arr)):
        ret.append(level_arr[i] - level_arr[i - 1])
    return ret


def is_all_increasing_or_decreasing(diff):
    all_increasing = all(x > 0 for x in diff)
    all_decreasing = all(x < 0 for x in diff)
    return all_increasing or all_decreasing


def is_more_than_zero_less_than_four(diff):
    return all(0 < abs(x) < 4 for x in diff)


def is_level_safe(level):
    diff_within_level = get_differences_within_level(level)
    return is_all_increasing_or_decreasing(diff_within_level) and is_more_than_zero_less_than_four(diff_within_level)


def solve1():
    safe_count = 0
    for level in levels:
        if is_level_safe(level):
            safe_count += 1
    print('Safe count is', safe_count)


import copy


def solve2():
    safe_count = 0
    for level in levels:
        if is_level_safe(level):
            safe_count += 1
        else:
            # brute force cos i can
            for i in range(len(level)):
                new_level = copy.deepcopy(level)
                new_level.pop(i)
                if is_level_safe(new_level):
                    safe_count += 1
                    break

    print('Safe count is', safe_count)


if __name__ == "__main__":
    read_inputs()
    # solve1()
    solve2()
