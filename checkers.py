import numpy as np

class game:
    def __init__(self):
        self.check = check()
        #### set dep
        self.turn = 1 # set white to have turn at
        self.Wpiece = [] # list of white pieces
        self.Bpiece = []
        
        #### setup board
        self.board = self.newboard()
        self.greeting()

    def greeting(self):
        print('starting game.........')
        self._display_board()
        return

    def status(self):
        print('GAME STATUS')
        print('White: ',str(len(self.Wpiece)))
        print('Black: ',str(len(self.Bpiece)))
        self._display_board()
        return
    
    def _display_board(self):
        "display board, at present only prints."
        print(self.board)        
        if self.turn == 1: turn_status = "WHITE'S TURN"
        else: turn_status = "BLACK'S TURN"
        print(turn_status)
        print()
        return

    def newboard(self):
        "create new board with pieces"
        board = np.zeros([100]) # clean board


        # white  pieces
        for i in np.arange(0,10,2):
            p = piece(i,'W') # create piece
            self.Wpiece.append(p) # add to list of pieces
            board[i:i+1] = 1 #add_to_board

        # black pieces
        for i in np.arange(91,100,2):
            p = piece(i,'B') # create piece
            self.Bpiece.append(p) # add to list of pieces
            board[i:i+1] = 2 # add_to_board

        # reshape board
        board = board.reshape(10,10)
        return(board)

    def make_move(self,start,end):
        "take input, checks that it is a legal move, and moves piece to location"
        #### check if new position is valid
        #calc_2_positons
        #(if off board remove option of move)
        #check all white piece positons, if one is in position of movement change the movement to new possible postition (check not off board)
        # check position request to move in list, if yes move, if no return message not possible.
        #
        self.check.piece_exists(start)
        # make movement on board and update position in pieces.
        self._move_piece(start,end)
        # if there was a jump remove other piece.
        # display board 
        self._display_board()
        return
    
    
    def _move_piece(self,start,end):
        "move piece position of board"
        self.board[start] = 0 # reset start position
        self.board[end] = self.turn
        
        if self.turn == 1:
            self.turn += 1
        else: self.turn -= 1
        return


class piece:
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color
        return
    
class check(game):
    def __init__(self):
        print(self.board)
        print('check_init')
        pass
    def piece_exists(self,start):
        print('check_piece_exists_used')
        if self.board[start] == self.turn: prob=False
        else: prob = True
        return(prob)
    def piece_correct_color(self):
        return
    def square_empty(self,end):
        if self.board[end] == 0: prob = False
        else: prob = True
        return(check)