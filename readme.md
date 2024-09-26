Zero Knowledge Chess Engine

Establish the search tree
Use a neural network to prune the search tree

Definition: Value Network

V - f(board)
V = -1: black win board
V = 0: draw
V = 1: white win board
State(board)


Pieces(2+7x2 = 16):
+ Universal
++ Blank (En passant)
++ Blank
+ Pieces
++ Rook (can castle)
++ Bishop
++ Knight
++ Queen
++ King
++ Pawn


Extra State:
+ To move
+ Castle available x4

8x8x5  = 257 bits (vector of 0 or 1)