from monte_carlo.mcts import MonteCarloTreeSearch
from cnn import CovNet

import threading


class Agent:

    color = None
    depth = None
    max_iter = None
    model = None

    def __init__(self, mcts_depth, mcts_max_iter, color):

        self.depth = mcts_depth
        self.max_iter = mcts_max_iter
        self.model = CovNet()
        self.color = color

    def get_move(self, board):
        mcts = MonteCarloTreeSearch(board, depth=self.depth, model=self.model)

        threads = [threading.Thread(target=mcts.run_mcts, args=(self.max_iter//5,)) for _ in range(5)]

        [thread.start() for thread in threads]

        [thread.join() for thread in threads]

        return mcts.get_best_move()
