Tic-Tac-Toe python
==================

## Running the game
1. To run this game you will need Python 3.x.x,
I used 3.5.2
2. Simply run in the terminal `python game.py` and enjoy!

## Algorithm
- We represent each player's decision with 1 
(for the first player) or -1 (for the second player)
in a 3x3 array
- When the sum of a row, column or diagonal is
3 or -3, player 1 or player 2 wins respectively

## Features to add
- Single player mode, with computer to play randomly
- Single player mode, with computer to play with simple AI,
 by minimizing the sums:
    * Medium difficulty: the sum is close to zero
    * Hard: the sum is -3 (computer wins)
- Test cases