import curses
import os
import sys
import time

class Board:
    column_width = 6
    blank_column_line = "{}|".format(" " * column_width)
    column_divider = "{}+".format("-" * column_width)

    def __init__(self, boardSupplier):
        self.boardSupplier = boardSupplier
        board = boardSupplier()
        
        self.divider = "\r+{0}".format(self.column_divider * len(board))
        self.column_separators = "\r|{0}".format(self.blank_column_line * len(board))
        self.width = len(self.column_separators)

        curses.initscr()
        self.window = curses.newwin(20, self.width, 0, 0)
        self.window.keypad(1)
        curses.noecho()
    
    def draw_board(self):
        """ It will (re)print the string representation of the board """
        x = 1
        for _, columns in enumerate(self.boardSupplier()):
            self.window.addstr(x, 0, self.divider)
            self.window.addstr(x + 1, 0, self.column_separators)
            self.draw_board_line_with_value(x + 2, columns)
            self.window.addstr(x + 3, 0, self.column_separators)
            x += 4
        self.window.addstr(x, 0, self.divider)

        self.window.addstr(x + 2, 0, "Q - exit; Arrows for movement")

    def draw_board_line_with_value(self, x, columns):
        line = "|"
        for num in columns:
            if num == 0:
                line += self.blank_column_line
            else:
                space_remainder = self.column_width - len(str(num))
                line += "{0}{1}{2}|".format(" " * (space_remainder//2 + space_remainder % 2), num, " " * (space_remainder//2))
        self.window.addstr(x, 0, line)
