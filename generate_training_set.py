#!/usr/bin/env python3
import chess.pgn
import os 
from state import State 

pgn  = open("../chessdb/DATABASE4U.pgn")

while 1:
    try:
        game = chess.pgn.read_game(pgn)
    except:
        break
    if game.headers['Result'] == '*':
        continue
    values = {"1/2-1/2": 0, "1-0": 1, "0-1" : -1}[game.headers['Result']]
  
    board = game.board()
    for i, move in enumerate(game.mainline_moves()) :
        board.push(move) 
        print(State(board).serialize()[:,:,0])
    # exit(0)  
 