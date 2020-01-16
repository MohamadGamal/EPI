from collections import defaultdict


def sudoku_state_checker(board):
    state = defaultdict(int)
    ROW, COLUMN, SQUARE = 0, 1, 2
    for row_indx, row in enumerate(board):
        for column_indx, element in enumerate(row):
            if element is not None:
                square_indx = str(row_indx) + '-' + str(column_indx)
                row_state, column_state, square_state = state[ROW,
                                                              row_indx], state[COLUMN, column_indx], state[SQUARE, square_indx]
                current_state = 1 << (element-1)
                if((row_state | column_state | square_state) & current_state):
                    return False
                state[ROW, row_indx] |= current_state
                state[COLUMN, column_indx] |= current_state
                state[SQUARE, square_state] |= current_state
    return True


board1 = [[5, 3, None, None, 7, None, None, None, None, None],
          [6, None, None, 1, 5, 9, None, None, None],
          [None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None]]
print(sudoku_state_checker(board1))
