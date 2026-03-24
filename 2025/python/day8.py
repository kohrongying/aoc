from collections import Counter

def read_input(filename):
    input = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            a, b, c = line.split(",")
            input.append((int(a), int(b), int(c)))
    return input


def solve1(filename, num_closest_pairs=1000):
    input = read_input(filename)
    closest_pairs = get_closest_pairs(input)
    circuits = get_top_circuits(closest_pairs[:num_closest_pairs], 3)
    print(len(circuits[0]) * len(circuits[1]) * len(circuits[2]))
    return


def get_closest_pairs(input: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    def get_distance(p1, p2):
        return (
            (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2
        ) ** 0.5

    def get_unique_pairs(
        input: list[tuple[int, int, int]],
    ) -> list[tuple[tuple[int, int, int], tuple[int, int, int]]]:
        result = []
        for i in range(len(input)):
            for j in range(i + 1, len(input)):
                result.append((input[i], input[j]))
        assert len(result) == len(input) * (len(input) - 1) / 2
        return result

    res = []
    pairs = get_unique_pairs(input)
    for p in pairs:
        res.append((p[0], p[1], get_distance(p[0], p[1])))
    res = sorted(res, key=lambda x: x[2])
    return res


def get_top_circuits(
    input: list[tuple[tuple[int, int, int], tuple[int, int, int], int]], num=3
) -> list[list[tuple[int, int, int]]]:
    circuit_map = {}  # Map of point to circuit number
    counter = 0
    for p in input:
        p1, p2, _ = p
        if p1 in circuit_map and p2 in circuit_map:  # merge two existing circuits
            v1 = circuit_map[p1]
            v2 = circuit_map[p2]
            for k in circuit_map:
                if circuit_map[k] == v2:
                    circuit_map[k] = v1
        elif p1 in circuit_map:  # add to existing circuit
            circuit_map[p2] = circuit_map[p1]
        elif p2 in circuit_map:  # add to existing circuit
            circuit_map[p1] = circuit_map[p2]
        else:  # add to new circuit
            circuit_map[p1] = counter
            circuit_map[p2] = counter
            counter += 1
    top = []
    for val in set(circuit_map.values()):
        tmp = []
        for k in circuit_map:
            if circuit_map[k] == val:
                tmp.append(k)
        top.append(tmp)
    top = sorted(top, key=lambda x: len(x), reverse=True)
    return top[:num]


def solve1_withKruskal(filename, num_pairs):
    input = read_input(filename)

    closest_pairs = get_closest_pairs(input)
    dsu = DSU(len(input))
    for p in closest_pairs[:num_pairs]:
        p1, p2, _ = p
        dsu.union(input.index(p1), input.index(p2))

    counts = Counter(dsu.get_parent())
    sorted_counts = counts.most_common()
    print(sorted_counts[0][1] * sorted_counts[1][1] * sorted_counts[2][1])
    return


# Kruskal algorithm to find min spanning tree
def kruskal(filename):
    input = read_input(filename)

    # sort by distance first
    closest_pairs = get_closest_pairs(input)
    dsu = DSU(len(input))
    min_spanning_tree = []
    for p in closest_pairs:
        p1, p2, _ = p
        if dsu.union(input.index(p1), input.index(p2)):
            min_spanning_tree.append(p)  # append the edge to the tree
        # else, do nothing as p1 and p2 are already in the same set

        # check if min spanning tree contains n-1 edges, break if so
        if len(min_spanning_tree) == len(input) - 1:
            print("stop")
            print(p1[0] * p2[0])
            break
    return

# Disjoint Set Union - find and union functions are key to ensure
# Constant O(1) operation for find and union
# Data structure is using trees (not necessary BST, can be tree with alot of branches)
# https://cp-algorithms.com/data_structures/disjoint_set_union.html
class DSU:
    def __init__(self, n):  # n = number of nodes, each node is its own set
        # store parent of each node in parent array
        # Init as parent of 0 is 0, parent of 1 is 0 etc.
        self.parent = list(range(n))
        self.rank = [0] * n

    # only for part1, decompress path
    def get_parent(self):
        for i in range(len(self.parent)):
            self.parent[i] = self.find(self.parent[i])
        return self.parent

    # Find the root representation of the node, x
    def find(self, x):
        if self.parent[x] != x:
            # path decompression (eg. 7->4->1 => 7->1, 4->1)
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Returns False if x and y are connected
    # and True if not connected and to be unioned
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # x and y are of the same set

        # if x and y are different sets, merge them
        if self.rank[px] < self.rank[py]:
            px, py = py, px  # swap px and py
        # so that we always merge lower rank (py) to higher rank (px)
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

