p = 10
s = 50
m = 200

class StateSpace():
    def __init__(self, problem) -> None:
        self.n = len(problem)
        self.problem = problem
    
    def __getitem__(self, index):
        x_col = []
        for y in range(self.n):
            x_col.append( self.problem[y][index] )
        return x_col
    
    def __str__(self):
        s = ''
        for y in range(self.n):
            for x in range(self.n):
                s += f'{self[x][y]:^5}'
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

solve((1,0), (1,2), [[p,p,p], [p,m,p], [s,s,s]])