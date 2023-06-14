import pprint

ROWS = 7
COLS = 7
KNIGHT_MOVES = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]
KNIGHT_START_POS = (1, 1)

board = [["O" for x in range(COLS)] for y in range(ROWS)]

visited_moves_dict = {KNIGHT_START_POS: True}


def is_valid_move(x, y):
    """Validates if the move is valid

    Args:
        x (integer): coordinate x
        y (integer): coordinate y

    Returns:
        boolean: True if the move is valid, False otherwise
    """
    if -1 < x < ROWS and -1 < y < COLS and (x, y) not in visited_moves_dict:
        return True
    return False


def get_valid_moves(x, y):
    """Returns a list of valid moves

    Args:
        x (integer): coordinate x
        y (integer): coordinate y

    Returns:
        list: list of valid moves
    """
    return [
        (x + move[0], y + move[1])
        for move in KNIGHT_MOVES
        if is_valid_move(x + move[0], y + move[1])
    ]


def main(coords, board, move_number=1):
    if len(visited_moves_dict) == ROWS * COLS:
        return True

    valid_moves = get_valid_moves(coords[0], coords[1])
    if len(valid_moves) == 0:
        return False

    for move in valid_moves:
        board[move[0]][move[1]] = move_number
        visited_moves_dict[move] = move_number
        move_number += 1
        if main(move, board, move_number):
            return True
        visited_moves_dict.pop(move)
        board[move[0]][move[1]] = "O"
        move_number -= 1
    return False


main(KNIGHT_START_POS, board)
pprint.pprint(board)

