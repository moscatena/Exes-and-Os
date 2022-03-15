# TicTacToe

<img src="./images/TicTacToe.PNG" alt="TicTacToe game" height="250"/>

This repository contains my explorations trying to build a Tic Tac Toe game.

- The game is played by two players in a hash (#) board. The player who starts places an 'X' in the board. The second player places an 'O' in the board. The game ends whenever a player manager to get three consecutive linear Xs or Os in the board, or the board runs out of space.

## Objectives

What I wanted to accomplish with these games was:

- Be able to see the board state at all times
- Be able to play against a friend or the computer
- Know who won and why
- Be able to play again while keeping score

## Version 1

The first version uses global variables, a lot of repeated code, and badly constructed functions. It does let you play against either a computer or a person, while displaying he board and showing winning moves, but doesn't allow replays or saves the scores.

## Version 2

The second version has much less code. It doesn't allow you to play against a friend and doesn't save score, while having a confusing interface. It is much more concise, but the board doesn't look great.

## Version 3

The third eiteration of the game checks all my objectives listed above. It also has a clear board and instructions. It creates the board in a dictionary and populates it as the game progresses.

## Version 4

This last version was made so I could toy around with Tkinter. It doesn't have the funcionalities of Version 3, but is displayed in a neat pop up.
