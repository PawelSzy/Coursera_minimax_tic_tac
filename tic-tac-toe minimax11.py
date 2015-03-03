"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided
import random

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
   
#    print "player", player
#    print "check_win", board.check_win(),
#    print "\n", board, "\n"
    
    winner = board.check_win()
    #print "winner!!!\n", player
    if winner!=None: 
        return (SCORES[winner], (-1, -1))

    empty_squares = board.get_empty_squares()
    
    is_draw = False
    scores=[]
    for square in empty_squares:
        new_board=board.clone()
        row, col = square[0], square[1]
        new_board.move(row, col, player)
        move = mm_move(new_board, provided.switch_player(player))
        #print "square, move", square, move
        if move[0]*SCORES[player] > 0:
            return (SCORES[player], square)
        if move[0]==SCORES[provided.DRAW]:
            is_draw =True
            draw_move = (0, square)
        scores.append((SCORES[player], square))
#      
        #print "scores ", scores

        if is_draw == True:
            #print"draw: ", draw_move
            return draw_move
        else:
            return random.choice(scores)
            
    return 0, (-1, -1)

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]


def run_test():
    
    y_win_board = provided.TTTBoard(3)

    #board.move(row, col, provided.PLAYERX)
    y_win_board.move(0, 0, provided.PLAYERO)
    y_win_board.move(0, 1, provided.PLAYERX)
    y_win_board.move(0, 2, provided.PLAYERO)
    y_win_board.move(1, 0, provided.PLAYERO)
    y_win_board.move(1, 1, provided.PLAYERX)
    y_win_board.move(2, 0, provided.PLAYERO)
    y_win_board.move(2, 1, provided.PLAYERO)
    y_win_board.move(2, 2, provided.PLAYERX)
    y_win_board.move(1, 2, provided.PLAYERX)
    
    x_win_board = provided.TTTBoard(3)

    #board.move(row, col, provided.PLAYERX)
    x_win_board.move(0, 0, provided.PLAYERX)
    x_win_board.move(0, 1, provided.PLAYERX)
    x_win_board.move(0, 2, provided.PLAYERO)
    x_win_board.move(1, 0, provided.PLAYERO)
    x_win_board.move(1, 1, provided.PLAYERX)
    x_win_board.move(2, 0, provided.PLAYERO)
    x_win_board.move(2, 1, provided.PLAYERO)
    x_win_board.move(2, 2, provided.PLAYERX)
    x_win_board.move(1, 2, provided.PLAYERX)   
    
    
    one_to_x = provided.TTTBoard(3)
    
    #one_to_x.move(0, 0, provided.PLAYERX)
    one_to_x.move(0, 1, provided.PLAYERX)
    one_to_x.move(0, 2, provided.PLAYERO)
    one_to_x.move(1, 0, provided.PLAYERO)
    one_to_x.move(1, 1, provided.PLAYERX)
    one_to_x.move(2, 0, provided.PLAYERO)
    one_to_x.move(2, 1, provided.PLAYERO)
    one_to_x.move(2, 2, provided.PLAYERX)
    one_to_x.move(1, 2, provided.PLAYERX)
   
    
    
    one_to_y = provided.TTTBoard(3)
    
    #one_to_x.move(0, 0, provided.PLAYERX)
    one_to_y.move(0, 1, provided.PLAYERX)
    one_to_y.move(0, 2, provided.PLAYERO)
    one_to_y.move(1, 0, provided.PLAYERO)
    one_to_y.move(1, 1, provided.PLAYERX)
    one_to_y.move(2, 0, provided.PLAYERO)
    one_to_y.move(2, 1, provided.PLAYERO)
    one_to_y.move(2, 2, provided.PLAYERX)
    one_to_y.move(1, 2, provided.PLAYERX)

    two_to_x = provided.TTTBoard(3)
    
    #one_to_x.move(0, 0, provided.PLAYERX)
    two_to_x.move(0, 1, provided.PLAYERX)
    two_to_x.move(0, 2, provided.PLAYERO)
    #two_to_x.move(1, 0, provided.PLAYERO)
    two_to_x.move(1, 1, provided.PLAYERX)
    two_to_x.move(2, 0, provided.PLAYERO)
    two_to_x.move(2, 1, provided.PLAYERO)
    two_to_x.move(2, 2, provided.PLAYERX)
    two_to_x.move(1, 2, provided.PLAYERX)
    
    draw_move =provided.TTTBoard(3) 
    
    draw_move.move(0, 0, provided.PLAYERX)
    #draw_move.move(0, 1, provided.PLAYERX)
    draw_move.move(0, 2, provided.PLAYERO)
    draw_move.move(1, 0, provided.PLAYERO)
    draw_move.move(1, 1, provided.PLAYERO)
    draw_move.move(2, 0, provided.PLAYERX)
    draw_move.move(2, 1, provided.PLAYERO)
    draw_move.move(2, 2, provided.PLAYERX)
    draw_move.move(1, 2, provided.PLAYERX)
    
    draw_to_x = provided.TTTBoard(3)
    
    #one_to_x.move(0, 0, provided.PLAYERX)
    draw_to_x.move(0, 1, provided.PLAYERX)
    draw_to_x.move(0, 2, provided.PLAYERO)
    #draw_to_x.move(1, 0, provided.PLAYERO)
    #draw_to_x.move(1, 1, provided.PLAYERX)
    draw_to_x.move(2, 0, provided.PLAYERO)
    draw_to_x.move(2, 1, provided.PLAYERO)
    draw_to_x.move(2, 2, provided.PLAYERX)
    draw_to_x.move(1, 2, provided.PLAYERX)
    
#    bord_list = [y_win_board,x_win_board,one_to_x,two_to_x,draw_to_x]
    #bord_list = [draw_move,draw_to_x]
    bord_list = [draw_move]
    for board in bord_list:
        print "start_board"
        print board
    
        move = mm_move(board, provided.PLAYERX)
        print "\n----------------"
        print board
    
        print "move to do", move

#    board = one_to_y     
#    print "\none move to y"    
#    print "start_board"
#    print board
#    
#    move = mm_move(board, provided.PLAYERO)
#    print "\n----------------"
#    print board
#    print "move to do", move
#run_test()



# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

#provided.play_game(move_wrapper, 1, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
