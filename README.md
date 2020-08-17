# Aqua Chess

Sister of [Magma-Chess](https://github.com/jbofill10/Magma-Chess)

Self-Learning Chess AI that only started with knowledge of the rules of chess  

Inspired by the same learning techniques used by AlphaZero

# How it works

* Use python-chess for game state management

* Will play games against itself over and over and then train on those games

* Similar to [Magma-Chess](https://github.com/jbofill10/Magma-Chess), it will create a 9x8 numerical representation of the board and pass that through a CNN

* Will establish a policy network which can decide whether positions are favorable or not

* Use MCTS for move generation

# Learning Process
* Will play against itself to improve using Reinforcement Learning
