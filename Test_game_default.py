import unittest
import os

from Grid import Grid
from Computer import Computer
from Player import Player

grid_obj = Grid()
computer = Computer()
player = Player()


class TestGame(unittest.TestCase):

    def test_draw(self):
        grid_obj.list[1] = "X"; grid_obj.list[2] = "O";  grid_obj.list[3]= "X"
        grid_obj.list[4] = "O"; grid_obj.list[5] = "X";  grid_obj.list[6] = "O"
        grid_obj.list[7] = "O"; grid_obj.list[8] = "X";  grid_obj.list[9] = "O"
        res_x = grid_obj.is_winner_player("O")
        res_o = grid_obj.is_winner_player("X")

        if not res_x and not res_o:
            draw = True

        self.assertTrue(draw)

    def test_is_grid_full(self):
        num_of_cell_full = 9
        response = grid_obj.is_grid_full(num_of_cell_full)
        os.system("clear")

        self.assertTrue(response)

    def test_is_grid_not_full(self):
        num_of_cell_full = 4
        response = grid_obj.is_grid_full(num_of_cell_full)
        os.system("clear")

        self.assertFalse(response)

    def test_defense_computer_ai_first_row(self):
        grid_obj.list[1] = "X";  grid_obj.list[2] = "X"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "8"; grid_obj.list[9] = "9"
        right_cell_to_choice = 3

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "X";  grid_obj.list[2] = "2"; grid_obj.list[3] = "X"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "8"; grid_obj.list[9] = "9"
        right_cell_to_choice = 2

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "1";  grid_obj.list[2] = "X"; grid_obj.list[3] = "X"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "8"; grid_obj.list[9] = "9"
        right_cell_to_choice = 1

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)


    def test_defense_computer_ai_second_row(self):
        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "X";  grid_obj.list[5] = "X"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "O"; grid_obj.list[9] = "9"
        right_cell_to_choice = 6

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "X";  grid_obj.list[5] = "5"; grid_obj.list[6] = "X"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "O"; grid_obj.list[9] = "9"
        right_cell_to_choice = 5

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "X"; grid_obj.list[6] = "X"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "O"; grid_obj.list[9] = "9"
        right_cell_to_choice = 4

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)



    def test_defense_computer_ai_third_row(self):
        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "X";  grid_obj.list[8] = "X"; grid_obj.list[9] = "9"
        right_cell_to_choice = 9

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "X"; grid_obj.list[9] = "X"
        right_cell_to_choice = 7

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "X";  grid_obj.list[8] = "8"; grid_obj.list[9] = "X"
        right_cell_to_choice = 8

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)


    def test_defense_computer_ai_first_column(self):
        grid_obj.list[1] = "X";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "X";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "8"; grid_obj.list[9] = "9"
        right_cell_to_choice = 7

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "X";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "X";  grid_obj.list[8] = "8"; grid_obj.list[9] = "9"
        right_cell_to_choice = 4

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "X";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "X";  grid_obj.list[8] = "8"; grid_obj.list[9] = "9"
        right_cell_to_choice = 1

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)



    def test_defense_computer_ai_second_column(self):
        grid_obj.list[1] = "1";  grid_obj.list[2] = "X"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "X"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "8"; grid_obj.list[9] = "9"
        right_cell_to_choice = 8

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "1";  grid_obj.list[2] = "X"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "X"; grid_obj.list[9] = "9"
        right_cell_to_choice = 5

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "X"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "X"; grid_obj.list[9] = "9"
        right_cell_to_choice = 2

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)



    def test_defense_computer_ai_third_column(self):
        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "X"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "X"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "8"; grid_obj.list[9] = "9"
        right_cell_to_choice = 9

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "X"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "8"; grid_obj.list[9] = "X"
        right_cell_to_choice = 6

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "X"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "8"; grid_obj.list[9] = "X"
        right_cell_to_choice = 3

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)


    def test_defense_computer_ai_first_diagonal(self):
        grid_obj.list[1] = "X";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "X"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "8"; grid_obj.list[9] = "9"
        right_cell_to_choice = 9

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "X";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "8"; grid_obj.list[9] = "X"
        right_cell_to_choice = 5

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "X"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "8"; grid_obj.list[9] = "X"
        right_cell_to_choice = 1

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)



    def test_defense_computer_ai_second_diagonal(self):
        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "X"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "X";  grid_obj.list[8] = "8"; grid_obj.list[9] = "9"
        right_cell_to_choice = 3

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "X"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "X";  grid_obj.list[8] = "8"; grid_obj.list[9] = "9"
        right_cell_to_choice = 5

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "X"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "X"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "8"; grid_obj.list[9] = "9"
        right_cell_to_choice = 7

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)




    def test_attack_computer_ai_first_row(self):
        grid_obj.list[1] = "O";  grid_obj.list[2] = "O"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "8"; grid_obj.list[9] = "9"
        right_cell_to_choice = 3

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)


        grid_obj.list[1] = "O";  grid_obj.list[2] = "2"; grid_obj.list[3] = "O"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "8"; grid_obj.list[9] = "9"
        right_cell_to_choice = 2

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "1";  grid_obj.list[2] = "O"; grid_obj.list[3] = "O"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "8"; grid_obj.list[9] = "9"
        right_cell_to_choice = 1

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)


    def test_attack_computer_ai_second_row(self):
        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "O";  grid_obj.list[5] = "O"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "O"; grid_obj.list[9] = "9"
        right_cell_to_choice = 6

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)


        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "O";  grid_obj.list[5] = "5"; grid_obj.list[6] = "O"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "O"; grid_obj.list[9] = "9"
        right_cell_to_choice = 5

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "O"; grid_obj.list[6] = "O"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "O"; grid_obj.list[9] = "9"
        right_cell_to_choice = 4

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)


    def test_attack_computer_ai_third_row(self):
        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "O";  grid_obj.list[8] = "O"; grid_obj.list[9] = "9"
        right_cell_to_choice = 9

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)


        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "O"; grid_obj.list[9] = "O"
        right_cell_to_choice = 7

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "O";  grid_obj.list[8] = "8"; grid_obj.list[9] = "O"
        right_cell_to_choice = 8

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)


    def test_attack_computer_ai_first_column(self):
        grid_obj.list[1] = "O";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "O";  grid_obj.list[5] = "3"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "4"; grid_obj.list[9] = "9"
        right_cell_to_choice = 7

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "O";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "O";  grid_obj.list[8] = "8"; grid_obj.list[9] = "9"
        right_cell_to_choice = 4

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "O";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "O";  grid_obj.list[8] = "8"; grid_obj.list[9] = "9"
        right_cell_to_choice = 1

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)




    def test_attack_computer_ai_second_column(self):
        grid_obj.list[1] = "1";  grid_obj.list[2] = "O"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "O"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "8"; grid_obj.list[9] = "9"
        right_cell_to_choice = 8

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)


        grid_obj.list[1] = "1";  grid_obj.list[2] = "O"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "O"; grid_obj.list[9] = "9"
        right_cell_to_choice = 5

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "O"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "O"; grid_obj.list[9] = "9"
        right_cell_to_choice = 2

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)




    def test_attack_computer_ai_third_column(self):
        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "O"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "O"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "8"; grid_obj.list[9] = "9"
        right_cell_to_choice = 9

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)


        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "O"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "8"; grid_obj.list[9] = "O"
        right_cell_to_choice = 6

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "O"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "8"; grid_obj.list[9] = "O"
        right_cell_to_choice = 3

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)



    def test_attack_computer_ai_first_diagonal(self):
        grid_obj.list[1] = "O";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "O"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "8"; grid_obj.list[9] = "9"
        right_cell_to_choice = 9

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "O";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "8"; grid_obj.list[9] = "O"
        right_cell_to_choice = 5

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "O"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "8"; grid_obj.list[9] = "O"
        right_cell_to_choice = 1

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)




    def test_attack_computer_ai_second_diagonal(self):
        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "O"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "O";  grid_obj.list[8] = "8"; grid_obj.list[9] = "9"
        right_cell_to_choice = 3

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)


        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "O"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "O";  grid_obj.list[8] = "8"; grid_obj.list[9] = "9"
        right_cell_to_choice = 5

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "O"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "O"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "8"; grid_obj.list[9] = "9"
        right_cell_to_choice = 7

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

    def test_attack_first_movement_if_grid_is_empty(self):
        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "5"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "8"; grid_obj.list[9] = "9"
        right_cell_to_choice = 5

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

    def test_attack_first_movement_if_central_cell_is_full(self):
        grid_obj.list[1] = "1";  grid_obj.list[2] = "2"; grid_obj.list[3] = "3"
        grid_obj.list[4] = "4";  grid_obj.list[5] = "X"; grid_obj.list[6] = "6"
        grid_obj.list[7] = "7";  grid_obj.list[8] = "8"; grid_obj.list[9] = "9"

        cell_for_defense = computer.get_move_ai(grid_obj.list)
        self.assertIsInstance(cell_for_defense, int)


    def test_input_name(self):
        test_player = Player()
        test_player.insert_player_name("Adam")
        self.assertEqual("Adam",test_player.name)

if __name__ == '__main__':
    unittest.main()