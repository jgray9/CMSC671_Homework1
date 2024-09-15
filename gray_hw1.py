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

def solve(initial_state, goal_state, problem):
    state_space = StateSpace(problem)

    print(f'Agent: {initial_state}')
    print(f'Goal State: {goal_state}')
    print(f'State Space:\n{state_space}')

    print('Heuristics:')
    for x in range(state_space.n):
        for y in range(state_space.n):
            dist = h(x, y, goal_state[0], goal_state[1])
            print(f'{dist:^5}', end='')
        print('')
    
    print('Neighbors of Agent (1,0):')
    neighbors = state_space.get_neighbors(1, 0)
    for n in neighbors:
        print(n)

solve((1,0), (1,2), [[p,p,p], [p,m,p], [s,s,s]])

q = PriorityQueue()
q.add(1, 'tac')
print(q.items)
q.add(0, 'tic')
print(q.items)
q.add(2, 'toe')
print(q.items)

print(q.pop())
print(q.pop())
print(q.pop())