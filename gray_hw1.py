p = 10
s = 50
m = 200

def solve(initial_state, goal_state, problem):
    n = len(problem)
    state_space = [[] for _ in range(n)]

    print(f'Agent: {initial_state}')
    print(f'Goal State: {goal_state}')
    for row in problem:
        for cost in row:
            print(f'{cost:^5}', end='')
        print('')

solve((1,0), (1,2), [[p,p,p], [p,m,p], [s,s,s]])