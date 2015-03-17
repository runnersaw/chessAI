# -*- coding: utf-8 -*-
"""
Created on Mon May  5 20:23:59 2014

@author: sawyer
"""

import pygame
from pygame.locals import *
import sys
import time
import copy

size = (600, 600)

all_spaces = []
for i in range(1,9):
    for j in range(1,9):
        all_spaces.append((i,j))

class Piece():
    def __init__(self, pos, team):
        self.pos = pos
        self.team = team
        self.alive = True
        self.moved = False
        
    def move(self, end_pos):
        self.pos = end_pos
        self.moved = True
        
    def check_valid_moves(self, moves):
        valid_moves = []
        for move in moves:
            if move[0] in range(1,9) and move[1] in range(1,9):
                valid_moves.append(move)
        return valid_moves

class Pawn(Piece):
    def __init__(self, pos, team):
        Piece.__init__(self, pos, team)
        self.score = 1
        
    def valid_moves(self, pieces):
        moves = []
        if self.team == 'Black':
            if (self.pos[0]+1, self.pos[1]) not in pieces.get_black_spaces():
                if (self.pos[0]+1, self.pos[1]) not in pieces.get_white_spaces():
                    moves.append((self.pos[0]+1, self.pos[1]))
                    if self.pos[0] == 2:
                        if (self.pos[0]+1, self.pos[1]) not in pieces.get_white_spaces():
                            if (self.pos[0]+2, self.pos[1]) not in pieces.get_black_spaces():
                                if (self.pos[0]+2, self.pos[1]) not in pieces.get_white_spaces():
                                    moves.append((self.pos[0]+2, self.pos[1]))
            if (self.pos[0]+1, self.pos[1]+1) in pieces.get_white_spaces():
                moves.append((self.pos[0]+1, self.pos[1]+1))
            if (self.pos[0]+1, self.pos[1]-1) in pieces.get_white_spaces():
                moves.append((self.pos[0]+1, self.pos[1]-1))
            self.check_valid_moves(moves)
            return moves
        if self.team == 'White':
            if (self.pos[0]-1, self.pos[1]) not in pieces.get_black_spaces():
                if (self.pos[0]-1, self.pos[1]) not in pieces.get_white_spaces():
                    moves.append((self.pos[0]-1, self.pos[1]))
                    if self.pos[0] == 7:
                        if (self.pos[0]-1, self.pos[1]) not in pieces.get_black_spaces():
                            if (self.pos[0]-2, self.pos[1]) not in pieces.get_white_spaces():
                                if (self.pos[0]-2, self.pos[1]) not in pieces.get_black_spaces():
                                    moves.append((self.pos[0]-2, self.pos[1]))
            if (self.pos[0]-1, self.pos[1]+1) in pieces.get_black_spaces():
                moves.append((self.pos[0]-1, self.pos[1]+1))
            if (self.pos[0]-1, self.pos[1]-1) in pieces.get_black_spaces():
                moves.append((self.pos[0]-1, self.pos[1]-1))
            moves = self.check_valid_moves(moves)
            return moves
    
class Rook(Piece):
    def __init__(self, pos, team):
        Piece.__init__(self, pos, team)
        self.score = 5
        
    def valid_moves(self, pieces):
        moves = []
        directions = ['right', 'left', 'up', 'down']
        for direction in directions:
            if direction == 'right':
                run = True
                count = 0
                while run:
                    count+=1
                    if count>8:
                        run = False
                    if self.team == 'White':
                        if (self.pos[0], self.pos[1]+count) not in pieces.get_white_spaces():
                            moves.append((self.pos[0], self.pos[1]+count))
                            if (self.pos[0], self.pos[1]+count) in pieces.get_black_spaces():
                                run = False
                        else: 
                            run = False
                    if self.team == 'Black':
                        if (self.pos[0], self.pos[1]+count) not in pieces.get_black_spaces():
                            moves.append((self.pos[0], self.pos[1]+count))
                            if (self.pos[0], self.pos[1]+count) in pieces.get_white_spaces():
                                run = False
                        else: 
                            run = False
            if direction == 'left':
                run = True
                count = 0
                while run:
                    count+=1
                    if count>8:
                        run = False
                    if self.team == 'White':
                        if (self.pos[0], self.pos[1]-count) not in pieces.get_white_spaces():
                            moves.append((self.pos[0], self.pos[1]-count))
                            if (self.pos[0], self.pos[1]-count) in pieces.get_black_spaces():
                                run = False
                        else: 
                            run = False
                    if self.team == 'Black':
                        if (self.pos[0], self.pos[1]-count) not in pieces.get_black_spaces():
                            moves.append((self.pos[0], self.pos[1]-count))
                            if (self.pos[0], self.pos[1]-count) in pieces.get_white_spaces():
                                run = False
                        else: 
                            run = False
            if direction == 'up':
                run = True
                count = 0
                while run:
                    count+=1
                    if count>8:
                        run = False
                    if self.team == 'White':
                        if (self.pos[0]-count, self.pos[1]) not in pieces.get_white_spaces():
                            moves.append((self.pos[0]-count, self.pos[1]))
                            if (self.pos[0]-count, self.pos[1]) in pieces.get_black_spaces():
                                run = False
                        else: 
                            run = False
                    if self.team == 'Black':
                        if (self.pos[0]-count, self.pos[1]) not in pieces.get_black_spaces():
                            moves.append((self.pos[0]-count, self.pos[1]))
                            if (self.pos[0]-count, self.pos[1]) in pieces.get_white_spaces():
                                run = False
                        else: 
                            run = False
            if direction == 'down':
                run = True
                count = 0
                while run:
                    count+=1
                    if count>8:
                        run = False
                    if self.team == 'White':
                        if (self.pos[0]+count, self.pos[1]) not in pieces.get_white_spaces():
                            moves.append((self.pos[0]+count, self.pos[1]))
                            if (self.pos[0]+count, self.pos[1]) in pieces.get_black_spaces():
                                run = False
                        else: 
                            run = False
                    if self.team == 'Black':
                        if (self.pos[0]+count, self.pos[1]) not in pieces.get_black_spaces():
                            moves.append((self.pos[0]+count, self.pos[1]))
                            if (self.pos[0]+count, self.pos[1]) in pieces.get_white_spaces():
                                run = False
                        else: 
                            run = False
        moves = self.check_valid_moves(moves)
        return moves
                            
class Bishop(Piece):
    def __init__(self, pos, team):
        Piece.__init__(self, pos, team)
        self.score = 3
        
    def valid_moves(self, pieces):
        moves = []
        directions = ['right', 'left', 'up', 'down']
        for direction in directions:
            if direction == 'right':
                run = True
                count = 0
                while run:
                    count+=1
                    if count>8:
                        run = False
                    if self.team == 'White':
                        if (self.pos[0]+count, self.pos[1]+count) not in pieces.get_white_spaces():
                            moves.append((self.pos[0]+count, self.pos[1]+count))
                            if (self.pos[0]+count, self.pos[1]+count) in pieces.get_black_spaces():
                                run = False
                        else: 
                            run = False
                    if self.team == 'Black':
                        if (self.pos[0]+count, self.pos[1]+count) not in pieces.get_black_spaces():
                            moves.append((self.pos[0]+count, self.pos[1]+count))
                            if (self.pos[0]+count, self.pos[1]+count) in pieces.get_white_spaces():
                                run = False
                        else: 
                            run = False
            if direction == 'left':
                run = True
                count = 0
                while run:
                    count+=1
                    if count>8:
                        run = False
                    if self.team == 'White':
                        if (self.pos[0]+count, self.pos[1]-count) not in pieces.get_white_spaces():
                            moves.append((self.pos[0]+count, self.pos[1]-count))
                            if (self.pos[0]+count, self.pos[1]-count) in pieces.get_black_spaces():
                                run = False
                        else: 
                            run = False
                    if self.team == 'Black':
                        if (self.pos[0]+count, self.pos[1]-count) not in pieces.get_black_spaces():
                            moves.append((self.pos[0]+count, self.pos[1]-count))
                            if (self.pos[0]+count, self.pos[1]-count) in pieces.get_white_spaces():
                                run = False
                        else: 
                            run = False
            if direction == 'up':
                run = True
                count = 0
                while run:
                    count+=1
                    if count>8:
                        run = False
                    if self.team == 'White':
                        if (self.pos[0]-count, self.pos[1]+count) not in pieces.get_white_spaces():
                            moves.append((self.pos[0]-count, self.pos[1]+count))
                            if (self.pos[0]-count, self.pos[1]+count) in pieces.get_black_spaces():
                                run = False
                        else: 
                            run = False
                    if self.team == 'Black':
                        if (self.pos[0]-count, self.pos[1]+count) not in pieces.get_black_spaces():
                            moves.append((self.pos[0]-count, self.pos[1]+count))
                            if (self.pos[0]-count, self.pos[1]+count) in pieces.get_white_spaces():
                                run = False
                        else: 
                            run = False
            if direction == 'down':
                run = True
                count = 0
                while run:
                    count+=1
                    if count>8:
                        run = False
                    if self.team == 'White':
                        if (self.pos[0]-count, self.pos[1]-count) not in pieces.get_white_spaces():
                            moves.append((self.pos[0]-count, self.pos[1]-count))
                            if (self.pos[0]-count, self.pos[1]-count) in pieces.get_black_spaces():
                                run = False
                        else: 
                            run = False
                    if self.team == 'Black':
                        if (self.pos[0]-count, self.pos[1]-count) not in pieces.get_black_spaces():
                            moves.append((self.pos[0]-count, self.pos[1]-count))
                            if (self.pos[0]-count, self.pos[1]-count) in pieces.get_white_spaces():
                                run = False
                        else: 
                            run = False
        moves = self.check_valid_moves(moves)
        return moves
    
class Knight(Piece):
    def __init__(self, pos, team):
        Piece.__init__(self, pos, team)
        self.score = 3
        
    def valid_moves(self, pieces):
        moves = []
        if self.team == 'White':
            if (self.pos[0]-2, self.pos[1]-1) not in pieces.get_white_spaces():
                moves.append((self.pos[0]-2, self.pos[1]-1))
        if self.team == 'White':
            if (self.pos[0]-2, self.pos[1]+1) not in pieces.get_white_spaces():
                moves.append((self.pos[0]-2, self.pos[1]+1))
        if self.team == 'White':
            if (self.pos[0]-1, self.pos[1]-2) not in pieces.get_white_spaces():
                moves.append((self.pos[0]-1, self.pos[1]-2))
        if self.team == 'White':
            if (self.pos[0]-1, self.pos[1]+2) not in pieces.get_white_spaces():
                moves.append((self.pos[0]-1, self.pos[1]+2))
        if self.team == 'White':
            if (self.pos[0]+1, self.pos[1]-2) not in pieces.get_white_spaces():
                moves.append((self.pos[0]+1, self.pos[1]-2))
        if self.team == 'White':
            if (self.pos[0]+1, self.pos[1]+2) not in pieces.get_white_spaces():
                moves.append((self.pos[0]+1, self.pos[1]+2))
        if self.team == 'White':
            if (self.pos[0]+2, self.pos[1]-1) not in pieces.get_white_spaces():
                moves.append((self.pos[0]+2, self.pos[1]-1))
        if self.team == 'White':
            if (self.pos[0]+2, self.pos[1]+1) not in pieces.get_white_spaces():
                moves.append((self.pos[0]+2, self.pos[1]+1))
        if self.team == 'Black':
            if (self.pos[0]-2, self.pos[1]-1) not in pieces.get_black_spaces():
                moves.append((self.pos[0]-2, self.pos[1]-1))
        if self.team == 'Black':
            if (self.pos[0]-2, self.pos[1]+1) not in pieces.get_black_spaces():
                moves.append((self.pos[0]-2, self.pos[1]+1))
        if self.team == 'Black':
            if (self.pos[0]-1, self.pos[1]-2) not in pieces.get_black_spaces():
                moves.append((self.pos[0]-1, self.pos[1]-2))
        if self.team == 'Black':
            if (self.pos[0]-1, self.pos[1]+2) not in pieces.get_black_spaces():
                moves.append((self.pos[0]-1, self.pos[1]+2))
        if self.team == 'Black':
            if (self.pos[0]+1, self.pos[1]-2) not in pieces.get_black_spaces():
                moves.append((self.pos[0]+1, self.pos[1]-2))
        if self.team == 'Black':
            if (self.pos[0]+1, self.pos[1]+2) not in pieces.get_black_spaces():
                moves.append((self.pos[0]+1, self.pos[1]+2))
        if self.team == 'Black':
            if (self.pos[0]+2, self.pos[1]-1) not in pieces.get_black_spaces():
                moves.append((self.pos[0]+2, self.pos[1]-1))
        if self.team == 'Black':
            if (self.pos[0]+2, self.pos[1]+1) not in pieces.get_black_spaces():
                moves.append((self.pos[0]+2, self.pos[1]+1))
        moves = self.check_valid_moves(moves)
        return moves
    
class King(Piece):
    def __init__(self, pos, team):
        Piece.__init__(self, pos, team)
        self.score = 0

    def valid_moves(self, pieces):
        moves = []
        space = (self.pos[0]+1, self.pos[1]+1)
        if self.team == 'White':
            if space not in pieces.get_threatened_by_black() and space not in pieces.get_white_spaces():
                moves.append(space)
        if self.team == 'Black':
            if space not in pieces.get_threatened_by_white() and space not in pieces.get_black_spaces():
                moves.append(space)
        space = (self.pos[0]+1, self.pos[1])
        if self.team == 'White':
            if space not in pieces.get_threatened_by_black() and space not in pieces.get_white_spaces():
                moves.append(space)
        if self.team == 'Black':
            if space not in pieces.get_threatened_by_white() and space not in pieces.get_black_spaces():
                moves.append(space)
        space = (self.pos[0]+1, self.pos[1]-1)
        if self.team == 'White':
            if space not in pieces.get_threatened_by_black() and space not in pieces.get_white_spaces():
                moves.append(space)
        if self.team == 'Black':
            if space not in pieces.get_threatened_by_white() and space not in pieces.get_black_spaces():
                moves.append(space)
        space = (self.pos[0], self.pos[1]+1)
        if self.team == 'White':
            if space not in pieces.get_threatened_by_black() and space not in pieces.get_white_spaces():
                moves.append(space)
        if self.team == 'Black':
            if space not in pieces.get_threatened_by_white() and space not in pieces.get_black_spaces():
                moves.append(space)
        space = (self.pos[0], self.pos[1]-1)
        if self.team == 'White':
            if space not in pieces.get_threatened_by_black() and space not in pieces.get_white_spaces():
                moves.append(space)
        if self.team == 'Black':
            if space not in pieces.get_threatened_by_white() and space not in pieces.get_black_spaces():
                moves.append(space)
        space = (self.pos[0]-1, self.pos[1]+1)
        if self.team == 'White':
            if space not in pieces.get_threatened_by_black() and space not in pieces.get_white_spaces():
                moves.append(space)
        if self.team == 'Black':
            if space not in pieces.get_threatened_by_white() and space not in pieces.get_black_spaces():
                moves.append(space)
        space = (self.pos[0]-1, self.pos[1])
        if self.team == 'White':
            if space not in pieces.get_threatened_by_black() and space not in pieces.get_white_spaces():
                moves.append(space)
        if self.team == 'Black':
            if space not in pieces.get_threatened_by_white() and space not in pieces.get_black_spaces():
                moves.append(space)
        space = (self.pos[0]-1, self.pos[1]-1)
        if self.team == 'White':
            if space not in pieces.get_threatened_by_black() and space not in pieces.get_white_spaces():
                moves.append(space)
        if self.team == 'Black':
            if space not in pieces.get_threatened_by_white() and space not in pieces.get_black_spaces():
                moves.append(space)
        moves = self.check_valid_moves(moves)
        return moves
    
class Queen(Piece):
    def __init__(self, pos, team):
        Piece.__init__(self, pos, team)
        self.score = 9

    def valid_moves(self, pieces):
        moves = []
        directions = ['right', 'left', 'up', 'down']
        for direction in directions:
            if direction == 'right':
                run = True
                count = 0
                while run:
                    count+=1
                    if count>8:
                        run = False
                    if self.team == 'White':
                        if (self.pos[0]+count, self.pos[1]+count) not in pieces.get_white_spaces():
                            moves.append((self.pos[0]+count, self.pos[1]+count))
                            if (self.pos[0]+count, self.pos[1]+count) in pieces.get_black_spaces():
                                run = False
                        else: 
                            run = False
                    if self.team == 'Black':
                        if (self.pos[0]+count, self.pos[1]+count) not in pieces.get_black_spaces():
                            moves.append((self.pos[0]+count, self.pos[1]+count))
                            if (self.pos[0]+count, self.pos[1]+count) in pieces.get_white_spaces():
                                run = False
                        else: 
                            run = False
            if direction == 'left':
                run = True
                count = 0
                while run:
                    count+=1
                    if count>8:
                        run = False
                    if self.team == 'White':
                        if (self.pos[0]+count, self.pos[1]-count) not in pieces.get_white_spaces():
                            moves.append((self.pos[0]+count, self.pos[1]-count))
                            if (self.pos[0]+count, self.pos[1]-count) in pieces.get_black_spaces():
                                run = False
                        else: 
                            run = False
                    if self.team == 'Black':
                        if (self.pos[0]+count, self.pos[1]-count) not in pieces.get_black_spaces():
                            moves.append((self.pos[0]+count, self.pos[1]-count))
                            if (self.pos[0]+count, self.pos[1]-count) in pieces.get_white_spaces():
                                run = False
                        else: 
                            run = False
            if direction == 'up':
                run = True
                count = 0
                while run:
                    count+=1
                    if count>8:
                        run = False
                    if self.team == 'White':
                        if (self.pos[0]-count, self.pos[1]+count) not in pieces.get_white_spaces():
                            moves.append((self.pos[0]-count, self.pos[1]+count))
                            if (self.pos[0]-count, self.pos[1]+count) in pieces.get_black_spaces():
                                run = False
                        else: 
                            run = False
                    if self.team == 'Black':
                        if (self.pos[0]-count, self.pos[1]+count) not in pieces.get_black_spaces():
                            moves.append((self.pos[0]-count, self.pos[1]+count))
                            if (self.pos[0]-count, self.pos[1]+count) in pieces.get_white_spaces():
                                run = False
                        else: 
                            run = False
            if direction == 'down':
                run = True
                count = 0
                while run:
                    count+=1
                    if count>8:
                        run = False
                    if self.team == 'White':
                        if (self.pos[0]-count, self.pos[1]-count) not in pieces.get_white_spaces():
                            moves.append((self.pos[0]-count, self.pos[1]-count))
                            if (self.pos[0]-count, self.pos[1]-count) in pieces.get_black_spaces():
                                run = False
                        else: 
                            run = False
                    if self.team == 'Black':
                        if (self.pos[0]-count, self.pos[1]-count) not in pieces.get_black_spaces():
                            moves.append((self.pos[0]-count, self.pos[1]-count))
                            if (self.pos[0]-count, self.pos[1]-count) in pieces.get_white_spaces():
                                run = False
                        else: 
                            run = False
        directions = ['right', 'left', 'up', 'down']
        for direction in directions:
            if direction == 'right':
                run = True
                count = 0
                while run:
                    count+=1
                    if count>8:
                        run = False
                    if self.team == 'White':
                        if (self.pos[0], self.pos[1]+count) not in pieces.get_white_spaces():
                            moves.append((self.pos[0], self.pos[1]+count))
                            if (self.pos[0], self.pos[1]+count) in pieces.get_black_spaces():
                                run = False
                        else: 
                            run = False
                    if self.team == 'Black':
                        if (self.pos[0], self.pos[1]+count) not in pieces.get_black_spaces():
                            moves.append((self.pos[0], self.pos[1]+count))
                            if (self.pos[0], self.pos[1]+count) in pieces.get_white_spaces():
                                run = False
                        else: 
                            run = False
            if direction == 'left':
                run = True
                count = 0
                while run:
                    count+=1
                    if count>8:
                        run = False
                    if self.team == 'White':
                        if (self.pos[0], self.pos[1]-count) not in pieces.get_white_spaces():
                            moves.append((self.pos[0], self.pos[1]-count))
                            if (self.pos[0], self.pos[1]-count) in pieces.get_black_spaces():
                                run = False
                        else: 
                            run = False
                    if self.team == 'Black':
                        if (self.pos[0], self.pos[1]-count) not in pieces.get_black_spaces():
                            moves.append((self.pos[0], self.pos[1]-count))
                            if (self.pos[0], self.pos[1]-count) in pieces.get_white_spaces():
                                run = False
                        else: 
                            run = False
            if direction == 'up':
                run = True
                count = 0
                while run:
                    count+=1
                    if count>8:
                        run = False
                    if self.team == 'White':
                        if (self.pos[0]-count, self.pos[1]) not in pieces.get_white_spaces():
                            moves.append((self.pos[0]-count, self.pos[1]))
                            if (self.pos[0]-count, self.pos[1]) in pieces.get_black_spaces():
                                run = False
                        else: 
                            run = False
                    if self.team == 'Black':
                        if (self.pos[0]-count, self.pos[1]) not in pieces.get_black_spaces():
                            moves.append((self.pos[0]-count, self.pos[1]))
                            if (self.pos[0]-count, self.pos[1]) in pieces.get_white_spaces():
                                run = False
                        else: 
                            run = False
            if direction == 'down':
                run = True
                count = 0
                while run:
                    count+=1
                    if count>8:
                        run = False
                    if self.team == 'White':
                        if (self.pos[0]+count, self.pos[1]) not in pieces.get_white_spaces():
                            moves.append((self.pos[0]+count, self.pos[1]))
                            if (self.pos[0]+count, self.pos[1]) in pieces.get_black_spaces():
                                run = False
                        else: 
                            run = False
                    if self.team == 'Black':
                        if (self.pos[0]+count, self.pos[1]) not in pieces.get_black_spaces():
                            moves.append((self.pos[0]+count, self.pos[1]))
                            if (self.pos[0]+count, self.pos[1]) in pieces.get_white_spaces():
                                run = False
                        else: 
                            run = False
        moves = self.check_valid_moves(moves)
        return moves
        
class Pieces:
    def __init__(self):
        self.wp1 = Pawn((7,1), 'White')
        self.wp2 = Pawn((7,2), 'White')
        self.wp3 = Pawn((7,3), 'White')
        self.wp4 = Pawn((7,4), 'White')
        self.wp5 = Pawn((7,5), 'White')
        self.wp6 = Pawn((7,6), 'White')
        self.wp7 = Pawn((7,7), 'White')
        self.wp8 = Pawn((7,8), 'White')
        self.wr1 = Rook((8,1), 'White')
        self.wk1 = Knight((8,2), 'White')
        self.wb1 = Bishop((8,3), 'White')
        self.wq = Queen((8,4), 'White')
        self.wk = King((8,5), 'White')
        self.wb2 = Bishop((8,6), 'White')
        self.wk2 = Knight((8,7), 'White')
        self.wr2 = Rook((8,8), 'White')
        self.bp1 = Pawn((2,1), 'Black')
        self.bp2 = Pawn((2,2), 'Black')
        self.bp3 = Pawn((2,3), 'Black')
        self.bp4 = Pawn((2,4), 'Black')
        self.bp5 = Pawn((2,5), 'Black')
        self.bp6 = Pawn((2,6), 'Black')
        self.bp7 = Pawn((2,7), 'Black')
        self.bp8 = Pawn((2,8), 'Black')
        self.br1 = Rook((1,1), 'Black')
        self.bk1 = Knight((1,2), 'Black')
        self.bb1 = Bishop((1,3), 'Black')
        self.bq= Queen((1,4), 'Black')
        self.bk = King((1,5), 'Black')
        self.bb2 = Bishop((1,6), 'Black')
        self.bk2 = Knight((1,7), 'Black')
        self.br2 = Rook((1,8), 'Black')
        self.pieces = [self.wp1, self.wp2, self.wp3, self.wp4, self.wp5, 
                       self.wp6, self.wp7, self.wp8, self.wr1, self.wb1, 
                       self.wk1, self.wk, self.wq, self.wb2, self.wk2, self.wr2,
                       self.bp1, self.bp2, self.bp3, self.bp4, self.bp5, self.bp6,
                       self.bp7, self.bp8, self.br1, self.bk1, self.bb1, self.bq,
                       self.bk, self.bb2, self.bk2, self.br2]
        self.black_pieces = [self.bp1, self.bp2, self.bp3, self.bp4, self.bp5, self.bp6,
                       self.bp7, self.bp8, self.br1, self.bk1, self.bb1, self.bq,
                       self.bk, self.bb2, self.bk2, self.br2]
        self.white_pieces = [self.wp1, self.wp2, self.wp3, self.wp4, self.wp5, 
                       self.wp6, self.wp7, self.wp8, self.wr1, self.wb1, 
                       self.wk1, self.wk, self.wq, self.wb2, self.wk2, self.wr2]

    def return_board_state(self):
        output = {}
        
    def check_valid_moves(self, moves):
        valid_moves = []
        for move in moves:
            if move[0] in range(1,9) and move[1] in range(1,9):
                valid_moves.append(move)
        return valid_moves

    def all_moves(self):
        output = {}
        for piece in self.pieces:
            output[piece.pos] = piece.valid_moves(self)
        return output

    def all_team_moves(self, team):
        output = {}
        for piece in self.pieces:
            if piece.team == team:
                if piece.valid_moves(self) != []:
                    output[piece.pos] = piece.valid_moves(self)
        return output

    def get_white_spaces(self):
        spaces = []
        for piece in self.pieces:
            if piece.team == 'White':
                spaces.append(piece.pos)
        return spaces
    
    def get_black_spaces(self):
        spaces = []
        for piece in self.pieces:
            if piece.team == 'Black':
                spaces.append(piece.pos)
        return spaces

    def get_threatened_by_black(self):
        spaces = []
        for piece in self.black_pieces:
            if not isinstance(piece, King):
                spaces.extend(piece.valid_moves(self))
            else:
                space = (piece.pos[0]+1, piece.pos[1]+1)
                spaces.extend([space])
                space = (piece.pos[0]+1, piece.pos[1])
                spaces.extend([space])
                space = (piece.pos[0]+1, piece.pos[1]-1)
                spaces.extend([space])
                space = (piece.pos[0], piece.pos[1]+1)
                spaces.extend([space])
                space = (piece.pos[0], piece.pos[1]-1)
                spaces.extend([space])
                space = (piece.pos[0]-1, piece.pos[1]+1)
                spaces.extend([space])
                space = (piece.pos[0]-1, piece.pos[1])
                spaces.extend([space])
                space = (piece.pos[0]-1, piece.pos[1]-1)
                spaces.extend([space])
        spaces = self.check_valid_moves(spaces)
        return spaces

    def get_threatened_by_white(self):
        spaces = []
        for piece in self.white_pieces:
            if not isinstance(piece, King):
                spaces.extend(piece.valid_moves(self))
            else:
                space = (piece.pos[0]+1, piece.pos[1]+1)
                spaces.extend([space])
                space = (piece.pos[0]+1, piece.pos[1])
                spaces.extend([space])
                space = (piece.pos[0]+1, piece.pos[1]-1)
                spaces.extend([space])
                space = (piece.pos[0], piece.pos[1]+1)
                spaces.extend([space])
                space = (piece.pos[0], piece.pos[1]-1)
                spaces.extend([space])
                space = (piece.pos[0]-1, piece.pos[1]+1)
                spaces.extend([space])
                space = (piece.pos[0]-1, piece.pos[1])
                spaces.extend([space])
                space = (piece.pos[0]-1, piece.pos[1]-1)
                spaces.extend([space])
        spaces = self.check_valid_moves(spaces)
        return spaces

    def get_piece_from_position(self, space):
        for piece in self.pieces:
            if piece.pos == space:
                return piece
        return None

    def move(self, piece, space):
        piece_to_delete = self.get_piece_from_position(space)
        if piece_to_delete != None:
            self.delete_piece(space)
        piece.move(space)

    def delete_piece(self, space):
        piece_to_delete = self.get_piece_from_position(space)
        for piece in self.pieces:
            if piece_to_delete == piece:
                self.pieces.remove(piece)
                if piece_to_delete.team == 'White':
                    self.white_pieces.remove(piece)
                if piece_to_delete.team == 'Black':
                    self.black_pieces.remove(piece)
                del piece

    def find_orig_space_and_new_space(self, pieces_class):
        for piece in self.pieces:
            other_piece = pieces_class.get_piece_from_position(piece.pos)
            if type(piece) != type(other_piece):
                orig_space = piece.pos
        for piece in pieces_class.pieces:
            other_piece = self.get_piece_from_position(piece.pos)
            if type(piece) != type(other_piece) or piece.team != other_piece.team:
                new_space = piece.pos
        return [orig_space, new_space]

class AI:
    def __init__(self, team, model):
        self.team = team
        self.model = model

    def change_team(self, team):
        if team == 'White':
            return 'Black'
        return 'White'

    def check_board_state(self, model_class):
        own_score = 0
        opponent_score = 0
        opponent_team = self.change_team(self.team)
        for piece in model_class.pieces.pieces:
            if piece.team == self.team:
                own_score += piece.score
            else:
                opponent_score += piece.score
        if model_class.check_win(self.team):
            return 100000
        elif model_class.check_win(opponent_team):
            return -100000
        else:
            return own_score/float(opponent_score)

    def make_child_model(self, model_class, piece, space):
        model = copy.deepcopy(model_class)
        new_piece = model.pieces.get_piece_from_position(piece.pos)
        model.pieces.move(new_piece, space)
        model.change_turn()
        return model

    def make_all_child_nodes(self, model):
        output = []
        for piece in model.all_valid_moves:
            if piece.team == model.turn:
                for space in model.all_valid_moves[piece]:
                    output.append(self.make_child_model(model, piece, space))
        return output

    def return_all_child_nodes_scores(self, model):
        output = []
        list_of_nodes = self.make_all_child_nodes(model)
        for node in list_of_nodes:
            output.append(self.check_board_state(node))
        return output

    def return_dictionary_of_scores(self, model, depth, max_depth):
        if depth == 1:
            return self.return_all_child_nodes_scores(model)
        if depth == max_depth:
            output = {}
            nodes = self.make_all_child_nodes(model)
            for node in nodes:
                output[node] = self.return_dictionary_of_scores(node, depth-1, max_depth)
            return output
        output = []
        for node in self.make_all_child_nodes(model):
            output.append(self.return_dictionary_of_scores(node, depth-1, max_depth))
        return output

    def flatten_dictionary(self, dictionary_or_list, depth, max_depth):
        if depth == max_depth:
            output = {}
            for model in dictionary_or_list:
                output[model] = self.flatten_dictionary(dictionary_or_list[model], depth-1, max_depth)
            return output
        if depth == 1:
            if (max_depth-depth) % 2 == 1:
                return min(dictionary_or_list)
            elif (max_depth-depth) % 2 == 0:
                return max(dictionary_or_list)
        output = []
        for entry in dictionary_or_list:
            if (max_depth-depth) % 2 == 1:
                output.append(self.flatten_dictionary(entry, depth-1, max_depth))
                return min(output)
            elif (max_depth-depth) % 2 == 0:
                output.append(self.flatten_dictionary(entry, depth-1, max_depth))
                return max(output)

    def return_model_to_scores(self, model, depth):
        dictionary_of_scores = self.return_dictionary_of_scores(model, depth, depth)
        return self.flatten_dictionary(dictionary_of_scores, depth, depth)

    def convert_model_to_move(self, model):
        master_model = self.model
        res = master_model.pieces.find_orig_space_and_new_space(model.pieces)
        orig_space = res[0]
        new_space = res[1]
        piece = self.model.pieces.get_piece_from_position(orig_space)
        return [piece, new_space]

    def find_best_move(self, model, depth):
        dictionary = self.return_model_to_scores(model, depth)
        score = 0
        model = None
        for key in dictionary:
            if dictionary[key]>score:
                score = dictionary[key]
                model = key
        move_rec = self.convert_model_to_move(model)
        return [move_rec, score]

class Model:
    def __init__(self):
        self.pieces = Pieces()
        self.selected = None
        self.turn = 'White'
        self.white_win = False
        self.black_win = False
        self.all_valid_moves = self.check_all_valid_moves()
        self.ai = AI('Black', self)

    def check_move(self, piece, space):
        model = copy.deepcopy(self)
        orig_spot = piece.pos
        new_piece = model.pieces.get_piece_from_position(orig_spot)
        model.pieces.move(new_piece, space)
        return not model.check_king_threatened(new_piece.team)

    def check_king_threatened(self, team):
        if team == 'White':
            if self.pieces.wk.pos in self.pieces.get_threatened_by_black():
                return True
        if team == 'Black':
            if self.pieces.bk.pos in self.pieces.get_threatened_by_white():
                return True
        return False

    def change_turn(self):
        if self.turn == 'White':
            self.turn = 'Black'
        elif self.turn == 'Black':
            self.turn = 'White'

    def check_all_valid_moves(self):
        output = {}
        for piece in self.pieces.pieces:
            moves = []
            for move in piece.valid_moves(self.pieces):
                if self.check_move(piece, move):
                    moves.append(move)
            if isinstance(piece, King):
                castle_moves = self.castle_moves(piece)
                if castle_moves != []:
                    moves.extend(castle_moves)
            output[piece] = moves
        return output

    def castle_moves(self, piece):
        moves = []
        if piece.moved == False:
            if piece.team == 'White':
                if piece.pos not in self.pieces.get_threatened_by_black():
                    rooks = [self.pieces.wr1, self.pieces.wr2]
                    if rooks[0].moved == False:
                        pos = (piece.pos[0], piece.pos[1]-1)
                        if self.pieces.get_piece_from_position(pos) == None and pos not in self.pieces.get_threatened_by_black():
                            pos = (piece.pos[0], piece.pos[1]-2)
                            if self.pieces.get_piece_from_position(pos) == None and pos not in self.pieces.get_threatened_by_black():
                                pos = (piece.pos[0], piece.pos[1]-3)
                                if self.pieces.get_piece_from_position(pos) == None and pos not in self.pieces.get_threatened_by_black():
                                    pos = (piece.pos[0], piece.pos[1]-2)
                                    moves.append(pos)
                    if rooks[1].moved == False:
                        pos = (piece.pos[0], piece.pos[1]+1)
                        if self.pieces.get_piece_from_position(pos) == None and pos not in self.pieces.get_threatened_by_black():
                            pos = (piece.pos[0], piece.pos[1]+2)
                            if self.pieces.get_piece_from_position(pos) == None and pos not in self.pieces.get_threatened_by_black():
                                moves.append(pos)
            if piece.team == 'Black':
                if piece.pos not in self.pieces.get_threatened_by_white():
                    rooks = [self.pieces.br1, self.pieces.br2]
                    if rooks[0].moved == False:
                        pos = (piece.pos[0], piece.pos[1]-1)
                        if self.pieces.get_piece_from_position(pos) == None and pos not in self.pieces.get_threatened_by_white():
                            pos = (piece.pos[0], piece.pos[1]-2)
                            if self.pieces.get_piece_from_position(pos) == None and pos not in self.pieces.get_threatened_by_white():
                                pos = (piece.pos[0], piece.pos[1]-3)
                                if self.pieces.get_piece_from_position(pos) == None and pos not in self.pieces.get_threatened_by_white():
                                    pos = (piece.pos[0], piece.pos[1]-2)
                                    moves.append(pos)
                    if rooks[1].moved == False:
                        pos = (piece.pos[0], piece.pos[1]+1)
                        if self.pieces.get_piece_from_position(pos) == None and pos not in self.pieces.get_threatened_by_white():
                            pos = (piece.pos[0], piece.pos[1]+2)
                            if self.pieces.get_piece_from_position(pos) == None and pos not in self.pieces.get_threatened_by_white():
                                moves.append(pos)
        return moves

    def castle(self, pos):
        if self.selected.team == 'White':
            if pos == (self.selected.pos[0], self.selected.pos[1]-2):
                self.pieces.move(self.pieces.wr1, (pos[0], pos[1]+1))
                self.move(pos)
                return
            if pos == (self.selected.pos[0], self.selected.pos[1]+2):
                self.pieces.move(self.pieces.wr2, (pos[0], pos[1]-1))
                self.move(pos)
                return
        if self.selected.team == 'Black':
            if pos == (self.selected.pos[0], self.selected.pos[1]-2):
                self.pieces.move(self.pieces.br1, (pos[0], pos[1]+1))
                self.move(pos)
                return
            if pos == (self.selected.pos[0], self.selected.pos[1]+2):
                self.pieces.move(self.pieces.br2, (pos[0], pos[1]-1))
                self.move(pos)
                return

    def get_valid_moves(self, piece):
        dictionary = self.all_valid_moves
        moves = dictionary[piece]
        return moves

    def move(self, space):
        piece = self.selected
        if self.turn == piece.team:
            if space in self.get_valid_moves(piece):
                self.pieces.move(piece, space)
                if isinstance(piece, Pawn):
                    print "pawn moved"
                    print space
                    if piece.team == "White" and space[0]==1:
                        print "became queen"
                        piece = Queen(piece.pos, piece.team)
                self.check_win(piece.team)
                self.change_turn()
                self.selected = None
                self.all_valid_moves = self.check_all_valid_moves()

    def check_win(self, team):
        valid_moves = []
        if team == 'White':
            for piece in self.pieces.black_pieces:
                moves = self.get_valid_moves(piece)
                if moves != []:
                    valid_moves.append(moves)
                    if valid_moves == []:
                        self.white_win = True
                        return True
        if team == 'Black':
            for piece in self.pieces.white_pieces:
                moves = self.get_valid_moves(piece)
                if moves != []:
                    valid_moves.append(moves)
                    if valid_moves == []:
                        self.white_win = True
                        return True

class View:
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen
        self.wp = pygame.transform.scale(pygame.image.load("sprites/white_pawn.png"), (size[0]/8, size[1]/8))
        self.wr = pygame.transform.scale(pygame.image.load("sprites/white_rook.png"), (size[0]/8, size[1]/8))
        self.wb = pygame.transform.scale(pygame.image.load("sprites/white_bishop.png"), (size[0]/8, size[1]/8))
        self.wkn = pygame.transform.scale(pygame.image.load("sprites/white_knight.png"), (size[0]/8, size[1]/8))
        self.wq = pygame.transform.scale(pygame.image.load("sprites/white_queen.png"), (size[0]/8, size[1]/8))
        self.wk = pygame.transform.scale(pygame.image.load("sprites/white_king.png"), (size[0]/8, size[1]/8))
        self.bp = pygame.transform.scale(pygame.image.load("sprites/black_pawn.png"), (size[0]/8, size[1]/8))
        self.br = pygame.transform.scale(pygame.image.load("sprites/black_rook.png"), (size[0]/8, size[1]/8))
        self.bb = pygame.transform.scale(pygame.image.load("sprites/black_bishop.png"), (size[0]/8, size[1]/8))
        self.bkn = pygame.transform.scale(pygame.image.load("sprites/black_knight.png"), (size[0]/8, size[1]/8))
        self.bq = pygame.transform.scale(pygame.image.load("sprites/black_queen.png"), (size[0]/8, size[1]/8))
        self.bk = pygame.transform.scale(pygame.image.load("sprites/black_king.png"), (size[0]/8, size[1]/8))

    def draw_board(self):
        self.screen.fill(pygame.Color(139,69,19))
        for i in range(4):
            for j in range(4):
                pygame.draw.rect(self.screen, (255,255,255), (size[0]*i/4, size[1]*j/4, size[0]/8, size[1]/8))
        for i in range(4):
            for j in range(4):
                pygame.draw.rect(self.screen, (255,255,255), (size[0]*i/4+size[0]/8, size[1]*j/4+size[1]/8, size[0]/8, size[1]/8))

    def draw(self):
        self.draw_board()
        self.draw_moves()
        for piece in self.model.pieces.pieces:
            self.draw_piece(piece)

    def draw_moves(self):
        if self.model.selected == None:
            return
        if self.model.get_valid_moves(self.model.selected) != []:
            self.draw_red(self.model.selected.pos)
            self.draw_square_small(self.model.selected.pos)
        for move in self.model.get_valid_moves(self.model.selected):
            self.draw_red(move)
            self.draw_square_small(move)

    def draw_red(self, space):
        color = (255,255,0)
        pos = [size[0]*(space[1]-1)/8.0, size[1]*(space[0]-1)/8.0]
        pygame.draw.rect(self.screen, color, (pos[0], pos[1], size[0]/8.0, size[1]/8.0))

    def draw_square_small(self, space):
        if (space[0]+space[1])%2 == 0:
            color = (255,255,255)
        else:
            color = (139,69,19)
        pos = [size[0]*(space[1]/8.0)-size[0]*15/16.0/8.0, size[1]*(space[0]/8.0)-size[1]*15/16.0/8.0]
        pygame.draw.rect(self.screen, color, (pos[0], pos[1], size[0]*7/8.0/8.0, size[1]*7/8.0/8.0))

    def draw_piece(self, piece):
        if isinstance(piece, King):
            if piece.team == 'Black':
                sprite = self.bk
            elif piece.team == 'White':
                sprite = self.wk
        if isinstance(piece, Queen):
            if piece.team == 'Black':
                sprite = self.bq
            elif piece.team == 'White':
                sprite = self.wq
        if isinstance(piece, Knight):
            if piece.team == 'Black':
                sprite = self.bkn
            elif piece.team == 'White':
                sprite = self.wkn
        if isinstance(piece, Bishop):
            if piece.team == 'Black':
                sprite = self.bb
            elif piece.team == 'White':
                sprite = self.wb
        if isinstance(piece, Rook):
            if piece.team == 'Black':
                sprite = self.br
            elif piece.team == 'White':
                sprite = self.wr
        if isinstance(piece, Pawn):
            if piece.team == 'Black':
                sprite = self.bp
            elif piece.team == 'White':
                sprite = self.wp
        pos = (size[0]/8.0*(piece.pos[1]-1), size[1]/8.0*(piece.pos[0]-1))
        self.screen.blit(sprite, pos)

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_pygame_event(self, event):
        if event.type == MOUSEBUTTONUP:
            mouse_position = pygame.mouse.get_pos()
            click_position = self.mouse_position_to_position(mouse_position)
            piece = self.model.pieces.get_piece_from_position(click_position)
            secondConditional = True
            if piece != None:
                if piece.team == self.model.turn:
                    self.model.selected = piece
                    secondConditional = False
            if secondConditional:
                if self.model.selected != None:
                    #print self.model.get_valid_moves(self.model.selected)
                    if click_position in self.model.selected.valid_moves(self.model.pieces):
                        self.model.move(click_position)
                    elif click_position in self.model.get_valid_moves(self.model.selected):
                        print 'ayy'
                        self.self.model.castle(click_position)
                    if self.model.white_win:
                        self.view.draw_board()
                    elif self.model.black_win:
                        self.view.draw_board()
                    else:
                        self.view.draw()
                    pygame.display.update()
            if self.model.turn == self.model.ai.team:
                [[piece, move], score] = self.model.ai.find_best_move(self.model, 2)
                self.model.selected = piece
                self.model.move(move)

    def mouse_position_to_position(self, mouse_position):
        x = mouse_position[0]
        sizex = size[0]/8.0
        y = mouse_position[1]
        sizey = size[1]/8.0
        for i in range(8):
            for j in range(8):
                if sizex*i<=x<=sizex*(i+1):
                    if sizey*j<=y<=sizey*(j+1):
                        return (j+1, i+1)

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Chess")
    screen = pygame.display.set_mode(size)

    model = Model()
    view = View(model, screen)
    controller = Controller(model, view)

    while True:
        for event in pygame.event.get():
            if  event.type == QUIT:
                pygame.quit()
                sys.exit()
            controller.handle_pygame_event(event)
        if model.white_win:
            view.draw_board()
        elif model.black_win:
            view.draw_board()
        else:
            view.draw()
        pygame.display.update()
    

        