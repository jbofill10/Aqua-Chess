from monte_carlo.mcts import MonteCarloTreeSearch
from cnn import CovNet


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
        return MonteCarloTreeSearch(board, depth=self.depth, model=self.model).run_mcts(self.max_iter)
