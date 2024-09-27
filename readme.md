simple NN-based Chess engine from georgehotz stream



<img width=600px src="https://raw.githubusercontent.com/geohot/twitchchess/master/screenshot.png" />


Usage
-----

```
 pip3 install python-chess torch torchvision numpy flask
 # then...
 ./play.py   # runs webserver on localhost:5000
```

Or with pypy (for max speed)
```
 pip_pypy install python-chess flask
 pypy ./play.py
 # web browse to localhost:5000
```


Implementation
-----

A simple 1 look ahead neural network value function. The trained net is in nets/value.pth. It takes in a serialized board and outputs a range from -1 to 1. -1 means black is win, 1 means white is win, and 0 means draw

Serialization
-----

We serialize the board into a 5x8x8 bitvector.

Training Set
-----

The value function was trained on 9M board positions from GM_Alphazer0 on chess.com forum

