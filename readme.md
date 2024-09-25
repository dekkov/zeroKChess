Zero Knowledge Chess Engine

Establish the search tree
Use a neural network to prune the search tree

Definition: Value Network

V - f(board)

State(board)


Pieces(1+6x2 = 13):
+ Blank
+ Rook
+ Bishop
+ Knight
+ Queen
+ King
+ Pawn
+ En passant



Extra State:
+ To move
+ Castle available x4

8x8x4+4 = 260 bits (vector of 0 or 1)