import sys
import time
import os

class Board:
    column_width = 6
    blank_column_line = "{}|".format(" " * column_width)

    def __init__(self, board):
        self.board = board
        
        self.divider = "\r+{0}".format("------+" * len(self.board))
        self.column_separators = "\r|{0}".format(self.blank_column_line * len(self.board))
    
    def draw_board(self):
        """ It will (re)print the string representation of the board """
        #os.system('cls' if os.name == 'nt' else 'clear')

        for row in self.board:
            print(self.divider)
            print(self.column_separators)
            self.draw_board_line_with_value(row)
            print(self.column_separators)
        print(self.divider)

        print()
        self.draw_instructions()

    def draw_instructions(self):
        print("ESC - exit; Arrows for movement;")

    def draw_board_line_with_value(self, row):
        line = "|"
        for num in row:
            if num == 0:
                line += self.blank_column_line
            else:
                space_remainder = self.column_width - len(str(num))
                line += "{0}{1}{2}|".format(" " * (space_remainder//2 + space_remainder % 2), num, " " * (space_remainder//2))
        print(line)
        
