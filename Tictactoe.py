# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 13:16:40 2017

@author: tranw
"""


class ttt(object):
    def __init__(self):
        pass
    
    def reset_board(self):
        self.board = [' ']*10
        self.game_state = True
        
    def display_board(self):
        print '\t{}|{}|{}\n\t-----\n\t{}|{}|{}\n\t-----\n\t{}|{}|{}'.format(self.board[7], self.board[8], self.board[9], self.board[4], self.board[5], self.board[6], self.board[1], self.board[2], self.board[3])

    def check_win(self):
        lines = ((1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7))
        for line in lines:
            check = 0
            for i in line:
                check += (self.board[i] == self.current_player)
            if check == 3:
                self.game_state = False
                self.win()

    def move(self):
        self.display_board()
        if self.current_player == 'X':
            self.current_player = 'O'
        elif self.current_player == 'O':
            self.current_player = 'X'
            
        if self.current_player == 'X':
            self.player = 1
        else:
            self.player = 2
    
        while True:
            try:
                mark = int(raw_input('Player {}, pick a spot between 1 and 9\n'.format(self.player)))
            except ValueError:
                print 'Sorry, please pick a number between 1 and 9\n'
                continue
            
            if mark not in (range(10)):
                print 'Sorry, please pick a number between 1 and 9\n'
                continue
            
            if self.board[mark] == ' ':
                self.board[mark] = self.current_player
                self.check_win()
                break
            else:
                print 'That spot is taken!'
                continue
        
    def start_game(self):
        self.current_player = 'O'
        self.reset_board()
        
        turn = 0
        while self.game_state == True:
            self.move()

            turn +=1
            if turn == 10:
                self.tie()
        
        while True:
            re = raw_input('Play again?\n(0): No\t(1) Yes')
            if re == 1:
                self.start_game()
                break
            elif re == 0:
                break
            else:
                continue 
            

    def win(self):
        self.display_board()
        print 'Player {} wins!'.format(self.player)
        self.game_state = False
        
    def tie(self):
        self.display_board()
        print 'Game ends in tie!'
        self.game_state = False
        