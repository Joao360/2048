import curses
from curses import KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_UP
from random import choice, randint

from view.board import Board

class Game:
    
    @staticmethod
    def create_board_with_size(size):
        rows = [None] * size
        for i in range(size):
            rows[i] = [0] * size
        return rows

    def __init__(self, size):
        self.board = Game.create_board_with_size(size)
        self.freePositions = self.getFreePositions()
        self.insert_random_number_in_board()
        self.insert_random_number_in_board()
        #print (self.board)

    def insert_random_number_in_board(self):
        if len(self.freePositions) == 0:
            #TODO: Draw Loser
            pass
        (row, column) = choice(self.freePositions)

        self.board[row][column] = 2
        self.freePositions.remove((row, column))

    def getFreePositions(self):
        positions = []
        for row, columns in enumerate(self.board):
            for column, value in enumerate(columns):
                if value == 0:
                    positions.append((row, column))
        return positions

    @staticmethod
    def moveLeft(columns):
        current_value = -1
        current_value_pos = -1
        positions_to_delete = []
        for column, value in enumerate(columns):
            if value == 0:
                positions_to_delete.insert(0, column)
                continue
            if current_value != value:
                current_value = value
                current_value_pos = column
                continue
            else:
                columns[current_value_pos] += value
                positions_to_delete.insert(0, column)
                current_value = -1
                current_value_pos = -1
        for column in positions_to_delete: 
            del columns[column]
            columns.append(0)

    def transposeBoard(self):
        return [[self.board[j][i] for j in range(len(self.board))] for i in range(len(self.board[0]))]

    def run(self):
        print(self.board)
        view = Board(lambda: self.board)
        view.draw_board()

        while True:
            key = view.window.getch()
            if key == ord('q'):
                break
            if key in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
                if key == KEY_LEFT:
                    for _, columns in enumerate(self.board):
                        Game.moveLeft(columns)
                elif key == KEY_RIGHT:
                    for _, columns in enumerate(self.board):
                        columns.reverse()
                        Game.moveLeft(columns)
                        columns.reverse()
                elif key == KEY_UP:
                    self.board = self.transposeBoard()
                    for _, columns in enumerate(self.board):
                        Game.moveLeft(columns)
                    self.board = self.transposeBoard()
                elif key == KEY_DOWN:
                    self.board = self.transposeBoard()
                    for _, columns in enumerate(self.board):
                        columns.reverse()
                        Game.moveLeft(columns)
                        columns.reverse()
                    self.board = self.transposeBoard()



                #TODO Optimize this
                self.freePositions = self.getFreePositions()
                self.insert_random_number_in_board()
                view.draw_board()

        curses.endwin()


if __name__ == '__main__':
    """ a = [2, 2, 4, 4]
    Game.moveLeft(a)
    a.reverse()
    print(a) """
    
    """ matrix = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
    print(matrix)
    matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    print(matrix) """
    
    Game(4).run()
