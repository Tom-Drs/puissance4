import os


class Puissance4:

    def __init__(self, width=7, height=6):
        self.width = width
        self.height = height
        self.grid = [0 for _ in range(width * height)]

    def get_index(self, row, column):
        return self.width * row + column

    def put_pawn(self, column, color):

        # Input value error
        try:
            column = int(column)
        except ValueError:
            return -1
        row = 0
        # Outside the grid
        if not self.is_in_grid(column, color):
            return -1
        # Column full
        if self.get_pawn(row, column):
            return -1

        while self.get_pawn(row, column) == 0 and row < self.height - 1:
            row += 1
        if self.get_pawn(row, column) == 0:
            self.grid[self.get_index(row, column)] = color
        else:
            self.grid[self.get_index(row - 1, column)] = color
        self.print_grid()
        return self.check_win(row, column, color)

    def print_grid(self):
        os.system("clear")
        for row in range(self.height):
            print([self.get_pawn(row, column) for column in range(self.width)])

    def get_pawn(self, row, column):
        return self.grid[self.get_index(row, column)]

    def get_lines(self, row, column):
        vertical_line = [self.get_pawn(index, column)
                         if 0 <= index < self.height else None
                         for index in range(row - 3, row + 4)]
        horizontal_line = [self.get_pawn(row, index)
                           if 0 <= index < self.width else None
                           for index in range(column-3, column+4)]
        left_diagonal = [self.get_pawn(row+index, column+index)
                         if 0 <= row + index < self.height and
                         0 <= column + index < self.width else None
                         for index in range(-3, 4)
]
        right_diagonal = [self.get_pawn(row+index, column-index)
                          if 0 <= row + index < self.height and
                          0 <= column-index < self.width else None
                          for index in range(-3, 4)]
        return [right_diagonal, left_diagonal, vertical_line, horizontal_line]

    @staticmethod
    def check_line(line, color):
        count = 0
        left, right = 3, 3
        while line[left-1] == color and left - 1 >= 0:
            left -= 1
            count += 1
        while line[right+1] == color and right + 1 < 7:
            right += 1
            count += 1
        return count >= 3

    def check_win(self, row, column, color):
        lines = self.get_lines(row, column)
        for line in lines:
            if self.check_line(line, color):
                return True
        return False

    def is_in_grid(self, row, column):
        return 0 <= row < self.height and 0 <= column < self.width
