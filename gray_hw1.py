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
    
    def get_cost(self, x, y):
        return self.problem[y][x]
    
    def get_neighbors(self, x, y):
        neighbors = []
        if x > 0:
            neighbors.append((x - 1, y))
        if y > 0:
            neighbors.append((x, y - 1))
        if x < self.n - 1:
            neighbors.append((x + 1, y))
        if y < self.n - 1:
            neighbors.append((x, y + 1))
        return neighbors
    
    def __getitem__(self, index):
        return [self.get_cost(index, y) for y in range(self.n)]
    
    def __str__(self):
        s = ''
        for y in range(self.n):
            for x in range(self.n):
                s += f'{self.get_cost(x,y):^5}'
            s += '\n'
        return s[:-1]

def h(x, y, goal_x, goal_y):
    # move up
    if y > goal_y:
        return h(x, y - 1, goal_x, goal_y) + 1
    # move right
    if x < goal_x:
        return h(x + 1, y, goal_x, goal_y) + 1
    # move down
    if y < goal_y:
        return h(x, y + 1, goal_x, goal_y) + 1
    # move left
    if x > goal_x:
        return h(x - 1, y, goal_x, goal_y) + 1
    return 0

def print_reached(state_space, reached):
    for y in range(state_space.n):
        for x in range(state_space.n):
            if (x,y) in reached:
                print(f'{reached[(x,y)]:^5}', end='')
            else:
                print(f'     ', end='')
        print('')

# adapted from Artificial Intelligence: A Modern Approach 4th Edition pg. 73
def uniform_cost(initial_state, goal_state, state_space: StateSpace):
    node = initial_state
    frontier = PriorityQueue()
    frontier.add(0, (node,[]))
    reached = {node: 0}

    def add_neighbor_to_frontier(neighbor, direction_letter):
        neighbor_cost = reached[node] + state_space.get_cost(neighbor[0], neighbor[1])
        neighbor_path = path + [direction_letter]
        if neighbor not in reached or neighbor_cost < reached[neighbor]:
            reached[neighbor] = neighbor_cost
            frontier.add(neighbor_cost, (neighbor,neighbor_path))

    while len(frontier) > 0:
        print('reached:')
        print_reached(state_space, reached)
        # pop best option
        node, path = frontier.pop()
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



def solve(initial_state, goal_state, problem):
    state_space = StateSpace(problem)
    print(state_space)

    print( uniform_cost(initial_state, goal_state, state_space) )


solve((1,0), (1,2), [[p,p,p], [p,m,p], [s,s,s]])