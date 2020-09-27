from agent import Agent
from chess_interface.Game import ChessGame
from Preprocessing import convert_to_int

import sys, chess


def run():

    game_count = sys.argv[1]

    curr_game_count = 1

    while curr_game_count < int(game_count):
        print(f'Playing on game {curr_game_count}')
        p1 = Agent(mcts_depth=30, mcts_max_iter=500, color=1)
        p2 = Agent(mcts_depth=30, mcts_max_iter=500, color=0)

        board = ChessGame()
        train_data = []
        while not board.is_game_over():
            if p1.color and board.curr_turn():
                print(chr(27) + "[2J")
                p1_move = p1.get_move(board)
                board.make_move(p1_move, format='uci')

                train_data.append(create_input(board.get_pychess_board(), p1_move))
                board.show_board()

            else:
                print(chr(27) + "[2J")
                p2_move = p2.get_move(board)
                board.make_move(p2_move, format='uci')
                board.show_board()
                train_data.append(create_input(board.get_pychess_board(), p2_move))

        curr_game_count += 1
        p1.model.train(input=train_data)


def create_input(board, move):
    move = chess.Move.from_uci(move)
    white_kcastle = False
    black_kcastle = False

    white_qcastle = False
    black_qcastle = False


    if board.is_kingside_castling(move):
        if board.turn:
            white_kcastle = True
        else:
            black_kcastle = True

    if board.is_queenside_castling(move):
        if board.turn:
            white_qcastle = True
        else:
            black_qcastle = True

    return convert_to_int(board, white_kcastle=white_kcastle, black_kcastle=black_kcastle,
                          white_qcastle=white_qcastle, black_qcastle=black_qcastle)




if __name__ == '__main__':
    run()