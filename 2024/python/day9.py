def read_inputs():
    with open('input/day9.txt', 'r') as f:
        return [int(i) for i in f.readline().strip()]


def solve1(line):
    expanded_idx, block_id, checksum = 0, 0, 0
    max_block_id = len(line) // 2

    end_of_disk_queue = []
    for n, idx in enumerate(range(len(line) - 1, -1, -2)):
        end_of_disk_queue += [max_block_id - n] * line[idx]

    while block_id < end_of_disk_queue[0]:
        for i in range(1, line[block_id * 2] + 1):
            checksum += block_id * expanded_idx
            expanded_idx += 1
        num_free_blocks = line[block_id * 2 + 1]
        if num_free_blocks != 0:
            for i in range(1, num_free_blocks + 1):
                val = end_of_disk_queue.pop(0)
                if val != block_id:
                    checksum += val * expanded_idx
                    expanded_idx += 1
                else:
                    break
        block_id += 1
    while block_id == end_of_disk_queue[0]:
        checksum += end_of_disk_queue.pop(0) * expanded_idx
        expanded_idx += 1
    print('Ans: ', checksum)


def solve2(line):
    expanded_idx, block_id, checksum = 0, 0, 0
    max_block_id = len(line) // 2

    # num of free spaces at each blockid index (incl last)
    free_spaces = [line[i + 1] for i in range(0, len(line) - 1, 2)] + [0]
    moved_nums = [[]] * len(free_spaces)  # list of new blockid at each blockid

    ignored_block_ids = []
    for n, idx in enumerate(range(len(line) - 1, 0, -2)):
        num_blocks = line[idx]
        moving_block_id = max_block_id - n
        if num_blocks > max(free_spaces[:-1 * n - 1]):
            continue
        for i, val in enumerate(free_spaces[:-1 * n - 1]):
            if val >= num_blocks:
                free_spaces[i] = val - num_blocks
                moved_nums[i] = moved_nums[i] + [moving_block_id] * num_blocks
                ignored_block_ids.append(moving_block_id)
                break

    for _ in range(0, len(line), 2):
        if block_id not in ignored_block_ids:
            for i in range(1, line[block_id * 2] + 1):
                checksum += block_id * expanded_idx
                expanded_idx += 1
        else:
            expanded_idx += line[block_id * 2]

        # then we add extra numbers at free spaces
        for j in moved_nums[block_id]:
            checksum += j * expanded_idx
            expanded_idx += 1

        # then increment expanded idx by free spaces
        expanded_idx += free_spaces[block_id]
        block_id += 1
    print('Ans: ', checksum)


if __name__ == "__main__":
    line = read_inputs()
    # solve1([1, 2, 3, 4, 5])
    # solve1([2, 3, 3, 3, 1, 3, 3, 1, 2, 1, 4, 1, 4, 1, 3, 1, 4, 0, 2])
    # solve1(line)
    # solve2([2, 3, 3, 3, 1, 3, 3, 1, 2, 1, 4, 1, 4, 1, 3, 1, 4, 0, 2])
    solve2(line)
