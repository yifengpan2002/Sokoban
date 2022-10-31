'''
Name: YifengPan
UPI: ypan179
Description:
A class code for sokoban game. Which contains different functions\
like(calculate total steps, move the crate and player_position based on the\
input that the player used. And other correlate functions that need to \
help with finished the game.
'''


class Sokoban:
    def __init__(self, board):
        self.__board = board
        self.__reset_board = self.get_history(self.__board)
        self.__board_history = [self.get_history(self.__board)]
        self.__steps = 0

    def find_player(self):
        row = 0
        column = 0
        row_found = False
        column_found = False
        for element in self.__board:
            for i in range(len(element)):
                if element[i] == "P":
                    column = i
                    column_found = True
                    break
            if column_found:
                break
            row += 1
        return (row, column)

    def complete(self):
        game_state = True
        for element in self.__board:
            for i in range(len(element)):
                if element[i] == "o":
                    game_state = False
        return game_state

    def get_steps(self):
        return self.__steps

    def get_history(self, board):
        current = []
        current2 = []
        for row in board:
            for column in row:
                current.append(column)
            current2.append(current)
            current = []
        return current2

    def restart(self):
        self.__board = self.get_history(self.__reset_board)
        self.__reset_board = self.get_history(self.__board)
        self.__board_history = [self.get_history(self.__board)]
        self.__steps = 0

    def undo(self):
        if len(self.__board_history) <= 1:
            self.__steps = 0
            return
        else:
            self.__board_history.pop()
            self.__board = self.__board_history[-1]
            self.__steps -= 1

    def move_up(self, row, column):
        move_to_row = row - 1
        if row == 0:
            move_to_row = len(self.__board)-1
        if self.__board[move_to_row][column] == " ":
            self.__board[row][column] = " "
            self.__board[move_to_row][column] = "P"
        if self.__board[move_to_row][column] == "#":
            if move_to_row == 0:
                new_move_row = len(self.__board)-1
            else:
                new_move_row = move_to_row - 1
            if self.__board[new_move_row][column] == " ":
                self.__board[new_move_row][column] = "#"
                self.__board[move_to_row][column] = "P"
                self.__board[row][column] = " "
            if self.__board[new_move_row][column] == "o":
                self.__board[new_move_row][column] = " "
                self.__board[move_to_row][column] = "P"
                self.__board[row][column] = " "
        self.__board_history.append(self.get_history(self.__board))

    def move_down(self, row, column):
        move_to_row = row + 1
        if row == len(self.__board)-1:
            move_to_row = 0
        if self.__board[move_to_row][column] == " ":
            self.__board[row][column] = " "
            self.__board[move_to_row][column] = "P"
        if self.__board[move_to_row][column] == "#":
            if move_to_row == len(self.__board)-1:
                new_move_row = 0
            else:
                new_move_row = move_to_row + 1
            if self.__board[new_move_row][column] == " ":
                self.__board[new_move_row][column] = "#"
                self.__board[move_to_row][column] = "P"
                self.__board[row][column] = " "
            if self.__board[new_move_row][column] == "o":
                self.__board[new_move_row][column] = " "
                self.__board[move_to_row][column] = "P"
                self.__board[row][column] = " "
        self.__board_history.append(self.get_history(self.__board))

    def move_left(self, row, column):
        move_to_column = column - 1
        if column == 0:
            move_to_column = len(self.__board[row])-1
        if self.__board[row][move_to_column] == " ":
            self.__board[row][column] = " "
            self.__board[row][move_to_column] = "P"
        if self.__board[row][move_to_column] == "#":
            if move_to_column == 0:
                new_move_column = len(self.__board[row])-1
            else:
                new_move_column = move_to_column - 1
            if self.__board[row][new_move_column] == " ":
                self.__board[row][new_move_column] = "#"
                self.__board[row][move_to_column] = "P"
                self.__board[row][column] = " "
            if self.__board[row][new_move_column] == "o":
                self.__board[row][new_move_column] = " "
                self.__board[row][move_to_column] = "P"
                self.__board[row][column] = " "
        self.__board_history.append(self.get_history(self.__board))

    def move_right(self, row, column):
        move_to_column = column + 1
        if column == len(self.__board[row])-1:
            move_to_column = 0
        if self.__board[row][move_to_column] == " ":
            self.__board[row][column] = " "
            self.__board[row][move_to_column] = "P"
        if self.__board[row][move_to_column] == "#":
            if move_to_column == len(self.__board[row])-1:
                new_move_column = 0
            else:
                new_move_column = move_to_column + 1
            if self.__board[row][new_move_column] == " ":
                self.__board[row][new_move_column] = "#"
                self.__board[row][move_to_column] = "P"
                self.__board[row][column] = " "
            if self.__board[row][new_move_column] == "o":
                self.__board[row][new_move_column] = " "
                self.__board[row][move_to_column] = "P"
                self.__board[row][column] = " "
        self.__board_history.append(self.get_history(self.__board))

    def move(self, direction):
        row, column = self.find_player()
        if direction == "w":
            self.move_up(row, column)
        elif direction == "s":
            self.move_down(row, column)
        elif direction == "a":
            self.move_left(row, column)
        else:
            self.move_right(row, column)
        if self.__board[row][column] != "P":
            self.__steps += 1
        else:
            self.__board_history.pop()

    def __str__(self):

        s = ""
        for row in self.__board:
            for element in row:
                s = s + str(element)
                s += " "
            s = s[:-1]
            s += "\n"
        s = s[:-1]
        return s


def main(board):
    game = Sokoban(board)
    message = 'Press w/a/s/d to move, r to restart, or u to undo'
    print(message)
    while not game.complete():
        print(game)
        move = input('Move: ').lower()
        while move not in ('w', 'a', 's', 'd', 'r', 'u'):
            print('Invalid move.', message)
            move = input('Move: ').lower()
        if move == 'r':
            game.restart()
        elif move == 'u':
            game.undo()
        else:
            game.move(move)
    print(game)
    print(f'Game won in {game.get_steps()} steps!')


board = [
    ['*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', 'P', '#', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*', ' ', '#', '*'],
    ['*', 'o', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', 'o', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*']
]
main(board)
