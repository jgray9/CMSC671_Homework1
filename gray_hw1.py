p = 10
s = 50
m = 200

class PriorityQueue():
    def __init__(self):
        self.items = []
    
    def add(self, key, value):
        self.items.append((key, value))
        self.items.sort(reverse=True)
    
    def pop(self):
        return self.items.pop()[1]
    
    def __len__(self):
        return len(self.items)

class StateSpace():
    def __init__(self, problem) -> None:
        self.n = len(problem)
        self.problem = problem
    
    def get_cost(self, tile):
        x, y = tile
        return self.problem[y][x]
    
    def __getitem__(self, index):
        return [self.get_cost(index, y) for y in range(self.n)]
    
    def __str__(self):
        s = ''
        for y in range(self.n):
            for x in range(self.n):
                s += f'{self.get_cost((x,y)):^5}'
            s += '\n'
        return s[:-1]

def h(tile, goal):
    return abs(goal[0] - tile[0]) + abs(goal[1] - tile[1])

# adapted from Artificial Intelligence: A Modern Approach 4th Edition pg. 73
def A_star(initial_state: tuple[int, int], goal_state: tuple[int, int], state_space: StateSpace):
    node = initial_state
    cost = 0
    path = ''
    frontier = PriorityQueue()
    frontier.add(0, (node, cost, path))

    def add_neighbor_to_frontier(neighbor, direction_letter):
        h_n = h(neighbor, goal_state)
        g_n = cost + state_space.get_cost(neighbor)
        neighbor_cost = h_n + g_n
        neighbor_path = path + direction_letter
        frontier.add(neighbor_cost, (neighbor, g_n, neighbor_path))

    while len(frontier) > 0:
        # pop best option
        node, cost, path = frontier.pop()
        # goal test
        if node == goal_state:
            return path
        # check neighbors
        # left
        if node[0] > 0:
            add_neighbor_to_frontier( (node[0] - 1, node[1]), 'W' )
        # up
        if node[1] > 0:
            add_neighbor_to_frontier( (node[0], node[1] - 1), 'N' )
        # right
        if node[0] < state_space.n - 1:
            add_neighbor_to_frontier( (node[0] + 1, node[1]), 'E' )
        # down
        if node[1] < state_space.n - 1:
            add_neighbor_to_frontier( (node[0], node[1] + 1), 'S' )
    return ''


def solve(initial_state, goal_state, problem, verborse=False):
    state_space = StateSpace(problem)
    if verborse:
        print(state_space)

    A_star(initial_state, goal_state, state_space)