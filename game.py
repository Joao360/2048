from random import randint, choice
from view.board import Board

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

class Game:
    
    @staticmethod
    def create_board_with_size(size):
        result = [None] * size
        for i in range(size):
            result[i] = [0] * size
        return result

    def __init__(self, size):
        self.board = Game.create_board_with_size(size)
        self.freePositions = self.getFreePositions()
        self.insert_random_number_in_board()
        self.insert_random_number_in_board()
        self.view = Board(self.board)
        #print (self.board)

    def insert_random_number_in_board(self):
        position = choice(self.freePositions)

        self.board[position.row][position.column] = 2
        self.freePositions.remove(position)

    def getFreePositions(self):
        positions = []
        for row, columns in enumerate(self.board):
            for column, value in enumerate(columns):
                if value == 0:
                    positions.append(Position(column, row))
        return positions

    def run(self):
        self.view.draw_board()


if __name__ == '__main__':
    Game(4).run()
