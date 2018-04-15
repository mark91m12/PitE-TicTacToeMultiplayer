#Computer
#Authors Mario Carricato & Marco Amato

import random


class Computer:
    def __init__(self):
        self.type = "O"

    def get_move_ai(self, grid):
        for i in [1, 4, 7]:
            if grid[i + 1] == self.type and grid[i + 2] == self.type and grid[i] == str(i):
                return i
            elif grid[i] == self.type and grid[i + 2] == self.type and grid[i + 1] == str(i + 1):
                return i + 1
            elif grid[i] == self.type and grid[i + 1] == self.type and grid[i + 2] == str(i + 2):
                return i + 2
        for i in [1, 4, 7]:
            if grid[i + 1] == "X" and grid[i + 2] == "X" and grid[i] == str(i):
                return i
            elif grid[i] == "X" and grid[i + 2] == "X" and grid[i + 1] == str(i + 1):
                return i + 1
            elif grid[i] == "X" and grid[i + 1] == "X" and grid[i + 2] == str(i + 2):
                return i + 2

        for i in [1, 2, 3]:
            if grid[i+3] == self.type and grid[i+6] == self.type and grid[i] == str(i):
                return i
            elif grid[i] == self.type and grid[i+6] == self.type and grid[i+3] == str(i+3):
                return i+3
            elif grid[i] == self.type and grid[i+3] == self.type and grid[i+6] == str(i+6):
                return i+6
        for i in [1, 2, 3]:
            if grid[i + 3] == "X" and grid[i + 6] == "X" and grid[i] == str(i):
                return i
            elif grid[i] == "X" and grid[i + 6] == "X" and grid[i + 3] == str(i + 3):
                return i + 3
            elif grid[i] == "X" and grid[i+3] == "X" and grid[i+6] == str(i+6):
                return i+6
       
        if grid[1] == self.type and grid[5] == self.type and grid[9] == str(9):
            return 9
        elif grid[1] == self.type and grid[9] == self.type and grid[5] == str(5):
            return 5
        elif grid[1] == str(1) and grid[5] == self.type and grid[9] == self.type:
            return 1
        if grid[1] == "X" and grid[5] == "X" and grid[9] == str(9):
            return 9
        elif grid[1] == "X" and grid[9] == "X" and grid[5] == str(5):
            return 5
        elif grid[1] == str(1) and grid[5] == "X" and grid[9] == "X":
            return 1

        if grid[3] == self.type and grid[5] == self.type and grid[7] == str(7):
            return 7
        elif grid[3] == self.type and grid[7] == self.type and grid[5] == str(5):
            return 5
        elif grid[3] == str(3) and grid[5] == self.type and grid[7] == self.type:
            return 3
        if grid[3] == "X" and grid[5] == "X" and grid[7] == str(7):
            return 7
        elif grid[3] == "X" and grid[7] == "X" and grid[5] == str(5):
            return 5
        elif grid[3] == str(3) and grid[5] == "X" and grid[7] == "X":
            return 3

        if grid[5] == "5":
            return 5
        else:
            mv = random.randint(1, 9)
            return mv

