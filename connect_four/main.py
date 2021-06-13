from typing import List, Optional
from itertools import islice, chain

BOARD_ROWS = 6
BOARD_COLS = 7
BOARD_DIAGONALS = 12
WINNING_SIZE = 4

class ConnectFour:

    _board_state: List[bool] = [None]

    def __init__(self):
        self._board_state = [None]  * BOARD_COLS * BOARD_ROWS

    def put(self, row: int, col: int, user: bool) -> bool:
        """
        Assume x,y are zero index like the array that represents the board
        row represents 'offset in row'
        col represents 'offset in col'
        user is the user playing, either true/false as 2 player game
        """
        if row < BOARD_ROWS and col < BOARD_COLS:
            pos = (BOARD_ROWS * col) + row
            if self._board_state[pos] is None:
                self._board_state[pos] = user
                return True
            
            print("Board position already taken")

        print("Invalid move: {}, {}".format(row,col))
        return False

    def boardState(self) -> List[bool]:
        board_array = [self._board_state[x * BOARD_ROWS: x * BOARD_ROWS + BOARD_COLS + 1] for x in range(0, BOARD_ROWS - 1)]
        return board_array


    def hasWon(self) -> Optional[bool]:
        """
        A win is horizontal, vertical, or diag
        Return the player if there's a win t/f, or none if no win so far.
        """

        for row_num in range(0, BOARD_ROWS):
            row_data = self._get_row(row_num)
            is_horiz_win = self._find_win(row_data)
            if is_horiz_win is not None:
                return is_horiz_win
            

        for col_num in range(0, BOARD_COLS):
            col_data = self._get_col(col_num)
            is_vert_win = self._find_win(col_data)
            if is_vert_win is not None:
                return is_vert_win

        for diag_num in range(0, BOARD_DIAGONALS):
            diag_data = self._get_diag(diag_num)
            is_diag_win = self._find_win(diag_data)
            if is_diag_win is not None:
                return is_diag_win

        return None

    def _find_win(self, row_data, offset=0):
        if offset > 3:
            return None
        elif row_data[offset: offset + 4] == [False] * WINNING_SIZE:
            return False
        elif row_data[offset: offset + 4] == [True] * WINNING_SIZE:
            return True

        return self._find_win(row_data, offset+1)

    def _get_row(self, number: int):
        return self._board_state[number * BOARD_ROWS: (number * BOARD_ROWS + BOARD_COLS)]

    def _get_col(self, number: int) -> List[bool]:
        return [self._get_row(x)[number] for x in range(0,BOARD_ROWS)]

    def _get_diag(self, diag=0, from_left = True) -> List[bool]:
        diag_data = []
        for x in range(0, diag+1):
            if from_left:
                diag_data.append(self._board_state[(BOARD_COLS * BOARD_ROWS) - BOARD_COLS + x])
        return diag_data
            

    def reset(self) -> bool:
        self._board_state = [None]  * 42


if __name__ == "__main__":
    newGame = ConnectFour()

    newGame.put(row=0,col=0, user=True)
    newGame.put(row=1,col=1, user=True)
    newGame.put(row=2,col=2, user=True)
    newGame.put(row=3,col=3, user=True)



    print(newGame._get_diag(0))
    print(newGame._get_diag(1))
    print(newGame._get_diag(2))
    print(newGame._get_diag(3))
    print(newGame._get_diag(4))
    print(newGame._get_diag(5))
    print(newGame._get_diag(6))
    