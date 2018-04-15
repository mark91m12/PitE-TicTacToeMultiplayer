#Grid
#Authors Mario Carricato & Marco Amato

import os


class Grid:
    def __init__(self):
        self.list = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.victory = []
        self.winner = ""

    def print_grid(self):
        print ("   *   *   ")
        print (" " + self.grid[1] + " * " + self.grid[2] + " * " + self.grid[3] + "  ")
        print ("   *   *   ")
        print ("***********")
        print ("   *   *   ")
        print (" " + self.grid[4] + " * " + self.grid[5] + " * " + self.grid[6] + "  ")
        print ("   *   *   ")
        print ("***********")
        print ("   *   *   ")
        print (" " + self.grid[7] + " * " + self.grid[8] + " * " + self.grid[9] + "  ")
        print ("   *   *   ")

    def is_winner_player(self, type):
        if self.grid[1] == type and self.grid[2] == type and self.grid[3] == type:
            self.victory_combination(1, 2, 3)
            self.winner = type
            return True
        elif self.grid[4] == type and self.grid[5] == type and self.grid[6] == type:
            self.victory_combination(4, 5, 6)
            self.winner = type
            return True
        if self.grid[7] == type and self.grid[8] == type and self.grid[9] == type:
            self.victory_combination(7, 8, 9)
            self.winner = type
            return True
        if self.grid[1] == type and self.grid[4] == type and self.grid[7] == type:
            self.victory_combination(1, 4, 7)
            self.winner = type
            return True
        if self.grid[2] == type and self.grid[5] == type and self.grid[8] == type:
            self.victory_combination(2, 5, 8)
            self.winner = type
            return True
        if self.grid[3] == type and self.grid[6] == type and self.grid[9] == type:
            self.victory_combination(3, 6, 9)
            self.winner = type
            return True
        if self.grid[3] == type and self.grid[5] == type and self.grid[7] == type:
            self.victory_combination(3, 5, 7)
            self.winner = type
            return True
        if self.grid[1] == type and self.grid[5] == type and self.grid[9] == type:
            self.victory_combination(1, 5, 9)
            self.winner = type
            return True

        return False

    def is_grid_full(self, num_of_cell_full):
        if num_of_cell_full == 9:
            self.get_snapschoot()
            print ("\n")
            print ("\033[31;1mResult:\033[0m Draw! ")
            print ("\n")
            return True
        else:
            return False

    def victory_combination(self, a, b, c):
        self.victory.append(a)
        self.victory.append(b)
        self.victory.append(c)

    def get_winner_combination(self):
        return self.victory

    def get_winner(self):
        return self.winner

    def get_snapschoot(self):
        os.system("clear")
        self.print_grid()
