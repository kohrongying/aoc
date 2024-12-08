# 1 leader dict (key: leader, value: [followers]
leaders = {}
updates = []


def read_inputs():
    with open('input/day5.txt', 'r') as f:
        for line in f.readlines():
            if '|' in line:
                x, y = line.strip().split('|')
                leaders[x] = leaders.get(x, []) + [y]
            elif ',' in line:
                updates.append(line.strip().split(','))


def solve1():
    right_updates = 0
    correct_order = True
    for line in updates:
        seen_pages = []
        for i, page in enumerate(line):
            page_followers = leaders.get(page, [])
            # current page cannot allow followers in front.
            correct_order = set(page_followers).isdisjoint(set(seen_pages))
            if not correct_order:
                break
            seen_pages.append(page)
        if correct_order:
            right_updates += get_mid(line)
    print('Ans is:', right_updates)


def get_mid(lst) -> int:
    return int(lst[len(lst) // 2])


def solve2():
    fixed_updates = 0
    for line in updates:
        seen_pages = []
        for i, page in enumerate(line):
            page_followers = leaders.get(page, [])
            # current page cannot allow followers in front.
            correct_order = set(page_followers).isdisjoint(set(seen_pages))
            if not correct_order:
                fixed_line = recursive_fix([], line)
                fixed_updates += get_mid(fixed_line)
                break
            seen_pages.append(page)
    print('Ans is:', fixed_updates)


def recursive_fix(seen: list[str], updates_left: list[str]) -> list[str]:
    if len(updates_left) == 0:
        return seen

    while True:
        if len(updates_left) == 0:
            break
        curr_page = updates_left.pop(0)
        page_followers = leaders.get(curr_page, [])
        correct_order = set(page_followers).isdisjoint(set(seen))
        seen.append(curr_page)
        if not correct_order:
            seen[-1], seen[-2] = seen[-2], seen[-1]
            seen = recursive_fix([], seen)
    return seen


if __name__ == "__main__":
    read_inputs()
    solve1()
    print(recursive_fix([], ['75', '97', '47', '61', '53']))
    print(recursive_fix([], ['61', '13', '29']))
    print(recursive_fix([], ['97', '13', '75', '29', '47']))
    solve2()
