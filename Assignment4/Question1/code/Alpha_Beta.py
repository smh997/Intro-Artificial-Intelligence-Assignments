from utils import Game, State

def min_value(game, state, alpha, beta):
    print(f'Ply: {state.ply}, MIN: node: {state.name}')
    if game.is_terminal(state):
        print(f'Ply: {state.ply}, MIN: node: {state.name} is terminal')
        return (game.utility(state, 1), None)
    inf = float('inf')
    v = inf
    for a in game.actions(state):
        print(f'Ply: {state.ply}, MIN: node: {state.name}, tried action {a}')
        v2, a2 = max_value(game, game.result(state, a), alpha, beta)
        print(f'Ply: {state.ply}, MIN: node: {state.name}, tried action {a} and the result value is {v2}')
        if v2 < v:
            v, move = v2, a
            beta = min(beta, v)
        if v <= alpha:
            print(f'PRUNE!: Ply: {state.ply}, MIN: node: {state.name} is done as v = {v} is less than or equal alpha = {alpha}')
            return (v, move)
    print(f'Ply: {state.ply}, MIN: node: {state.name} is done')
    return (v, move)

def max_value(game, state, alpha, beta):
    print(f'Ply: {state.ply}, MAX: node: {state.name}')
    if game.is_terminal(state):
        print(f'Ply: {state.ply}, MAX: node: {state.name} is terminal')
        return (game.utility(state, 0), None)
    m_inf = float('-inf')
    v = m_inf
    for a in game.actions(state):
        print(f'Ply: {state.ply}, MAX: node: {state.name}, tried action {a}')
        v2, a2 = min_value(game, game.result(state, a), alpha, beta)
        print(f'Ply: {state.ply}, MAX: node: {state.name}, tried action {a} and the result value is {v2}')
        if v2 > v:
            v, move = v2, a
            alpha = max(alpha, v)
        if v >= beta:
            print(f'PRUNE!: Ply: {state.ply}, MAX: node: {state.name} is done as v = {v} is greater than or equal beta = {beta}')
            return (v, move)
    print(f'Ply: {state.ply}, MAX: node: {state.name} is done')
    return (v, move)

def alpha_beta_search(game, state):
    player = game.to_move(state)
    m_inf, inf = float('-inf'), float('inf')
    value, move = max_value(game, state, m_inf, inf)
    return (move, value)


first_state = State('A')
two_ply_game = Game(2, first_state)
four_ply_game1 = Game(4, first_state, 0)
four_ply_game2 = Game(4, first_state, 1)
four_ply_game3 = Game(4, first_state, 2)


game = two_ply_game
print('Best acrion for MAX with the final utility value:', alpha_beta_search(game, first_state))

print()

game = four_ply_game1
print('Best acrion for MAX with the final utility value:', alpha_beta_search(game, first_state))

print()

game = four_ply_game2
print('Best acrion for MAX with the final utility value:', alpha_beta_search(game, first_state))

print()

game = four_ply_game3
print('Best acrion for MAX with the final utility value:', alpha_beta_search(game, first_state))