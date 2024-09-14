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
        for x in range(self.n):
            for y in range(self.n):
                s += f'{self[x][y]:^5}'
            s += '\n'
        return s[:-1]
        

def solve(initial_state, goal_state, problem):
    state_space = StateSpace(problem)

    print(f'Agent: {initial_state}')
    print(f'Goal State: {goal_state}')
    print(f'State Space:\n{state_space}')

solve((1,0), (1,2), [[p,p,p], [p,m,p], [s,s,s]])