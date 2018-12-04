# Development of checkers game.
print('Making checkers')

from checkers import game
g = game()
g.make_move((0,0),(1,1)) #W1
g.make_move((9,1),(8,0)) # B1
g.make_move((1,1),(2,0)) #W2



