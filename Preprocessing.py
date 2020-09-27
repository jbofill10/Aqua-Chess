import chess
import numpy as np


def convert_to_int(board, white_kcastle, black_kcastle, white_qcastle, black_qcastle):

    white_pos = [None] * 64
    black_pos = [None] * 64
    for sq in chess.scan_reversed(board.occupied_co[chess.WHITE]):  # Check if white
        white_pos[sq] = board.piece_type_at(sq)
    for sq in chess.scan_reversed(board.occupied_co[chess.BLACK]):  # Check if black
        black_pos[sq] = board.piece_type_at(sq)
    white_map = [0 if v is None else v for v in white_pos]
    black_map = [0 if v is None else v for v in black_pos]

    matrix = np.zeros((7, 8, 8))

    counter = 0
    for i in range(len(matrix[0])):
        for j in range(len(matrix[0][0])):
            matrix[0][i][j] = white_map[counter]
            matrix[3][i][j] = black_map[counter]

            counter += 1

    # Turn
    if board.turn:
        matrix[6].fill(0)
    else:
        matrix[6].fill(1)

    # Check for castling rights
    if white_kcastle:
        matrix[1].fill(1)
    if white_qcastle:
        matrix[2].fill(1)
    if black_kcastle:
        matrix[4].fill(1)
    if black_qcastle:
        matrix[5].fill(1)

    return matrix