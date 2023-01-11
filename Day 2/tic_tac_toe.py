class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player = 'X'

    def play(self):
        while True:
            self.print_board()
            x, y = self.get_move()
            if self.is_valid_move(x, y):
                self.board[x][y] = self.player
                if self.is_game_over():
                    print(f'Player {self.player} wins!')
                    return
                self.player = 'O' if self.player == 'X' else 'X'
            else:
                print('Invalid move')

    def get_move(self):
        x, y = input('Enter coordinates (row column): ').split()
        return int(x), int(y)

    def is_valid_move(self, x, y):
        return 0 <= x < 3 and 0 <= y < 3 and self.board[x][y] == ' '

    def is_game_over(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def print_board(self):
        for row in self.board:
            print('|'.join(row))

game = TicTacToe()
game.play()
