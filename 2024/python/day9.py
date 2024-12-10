def read_inputs():
    with open('input/day9.txt', 'r') as f:
        return [int(i) for i in f.readline().strip()]


def solve1(line):
    left = 0
    expanded_idx = 0
    max_block_id = len(line) // 2
    block_id = 0
    checksum = 0

    end_of_disk_queue = []
    for n, idx in enumerate(range(len(line) - 1, -1, -2)):
        end_of_disk_queue += [max_block_id - n] * line[idx]

    while block_id < end_of_disk_queue[0]:
        for i in range(1, line[left] + 1):
            checksum += block_id * expanded_idx
            expanded_idx += 1
        num_free_blocks = line[left + 1]
        if num_free_blocks != 0:
            for i in range(1, num_free_blocks + 1):
                val = end_of_disk_queue.pop(0)
                if val != block_id:
                    checksum += val * expanded_idx
                    expanded_idx += 1
                else:
                    break
        block_id += 1
        left += 2
    while block_id == end_of_disk_queue[0]:
        checksum += end_of_disk_queue.pop(0) * expanded_idx
        expanded_idx += 1
    print('Ans: ', checksum)


if __name__ == "__main__":
    line = read_inputs()
    # solve1([1, 2, 3, 4, 5])
    # solve1([2, 3, 3, 3, 1, 3, 3, 1, 2, 1, 4, 1, 4, 1, 3, 1, 4, 0, 2])
    solve1(line)