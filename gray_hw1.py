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
    x, y = tile
    # move up
    if y > goal[1]:
        return h((x, y - 1), goal) + 1
    # move right
    if x < goal[0]:
        return h((x + 1, y), goal) + 1
    # move down
    if y < goal[1]:
        return h((x, y + 1), goal) + 1
    # move left
    if x > goal[0]:
        return h((x - 1, y), goal) + 1
    return 0

# adapted from Artificial Intelligence: A Modern Approach 4th Edition pg. 73
def A_star(initial_state: tuple[int, int], goal_state: tuple[int, int], state_space: StateSpace):
    node = initial_state
    frontier = PriorityQueue()
    frontier.add(0, node)
    costs = {node: 0}
    paths = {node: ''}

    def add_neighbor_to_frontier(neighbor, direction_letter):
        h_n = h(neighbor, goal_state)
        g_n = costs[node] + state_space.get_cost(neighbor)
        neighbor_cost = h_n + g_n
        neighbor_path = paths[node] + direction_letter
        if neighbor not in costs or neighbor_cost < costs[neighbor]:
            costs[neighbor] = neighbor_cost
            paths[neighbor] = neighbor_path
            frontier.add(neighbor_cost, neighbor)

    while len(frontier) > 0:
        # pop best option
        node = frontier.pop()
        # goal test
        if node == goal_state:
            return paths[node]
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


def solve(initial_state, goal_state, problem):
    state_space = StateSpace(problem)
    print(state_space)

    print( A_star(initial_state, goal_state, state_space) )


solve((1,0), (3,3), [
    [m,p,m,m,m],
    [p,p,p,p,p],
    [p,m,m,m,m],
    [p,p,p,p,p]
    ])