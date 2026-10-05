
SIZE = 5
total = 0

def print_board(board):
    for row in board:
        for col in row:
            print(str(col).ljust(4), end = ' ')
        print()

def patrol(board, row, col, step = 1):
    if row < 0 or row >= SIZE or \
         col < 0 or col >= SIZE or \
         board[row][col] != 0:
        return
    board[row][col] = step
    if step == SIZE * SIZE:
        global total # 声明 total 是全局变量
        total += 1
        print(f'第{total}种走法:')
        print_board(board)
    patrol(board, row - 2, col - 1, step + 1)
    patrol(board, row - 1, col - 2, step + 1)
    patrol(board, row + 1, col - 2, step + 1)
    patrol(board, row + 2, col - 1, step + 1)
    patrol(board, row + 2, col + 1, step + 1)
    patrol(board, row + 1, col + 2, step + 1)
    patrol(board, row - 1, col + 2, step + 1)
    patrol(board, row - 2, col + 1, step + 1)
    board[row][col] = 0

def main():
    board = [[0] * SIZE for _ in range(SIZE)]
    patrol(board, 0, 0)

if __name__ == '__main__':
    main()