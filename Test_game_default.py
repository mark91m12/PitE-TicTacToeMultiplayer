import unittest
import os

from Grid import Grid
from Computer import Computer
from Player import Player

grid_obj = Grid()
computer = Computer()
player = Player()


class TestGame(unittest.TestCase):

    def test_winner_in_row1(self):
        grid_obj.grid[1] = "X"; grid_obj.grid[2] = "X";  grid_obj.grid[3]= "X"
        grid_obj.grid[4] = "O"; grid_obj.grid[5] = "5";  grid_obj.grid[6] = "O"
        grid_obj.grid[7] = "7"; grid_obj.grid[8] = "O";  grid_obj.grid[9] = "O"

        winner_combination_right = [1, 2, 3]
        res = grid_obj.is_winner_player("X")
        response_combination = grid_obj.get_winner_combination()

        self.assertTrue(res)
        self.assertIsInstance(response_combination, list)
        self.assertEqual(response_combination, winner_combination_right)

    def test_winner_in_row2(self):
        grid_obj.grid[1] = "O"; grid_obj.grid[2] = "O";  grid_obj.grid[3]= "9"
        grid_obj.grid[4] = "O"; grid_obj.grid[5] = "5";  grid_obj.grid[6] = "O"
        grid_obj.grid[7] = "X"; grid_obj.grid[8] = "X";  grid_obj.grid[9] = "X"

        winner_combination_right = [7, 8, 9]
        res = grid_obj.is_winner_player("X")
        response_combination = grid_obj.get_winner_combination()

        self.assertTrue(res)
        self.assertIsInstance(response_combination, list)
        self.assertEqual(response_combination, winner_combination_right)

    def test_winner_in_row3(self):
        grid_obj.grid[1] = "X"; grid_obj.grid[2] = "X";  grid_obj.grid[3]= "9"
        grid_obj.grid[4] = "O"; grid_obj.grid[5] = "O";  grid_obj.grid[6] = "O"
        grid_obj.grid[7] = "X"; grid_obj.grid[8] = "X";  grid_obj.grid[9] = "O"

        winner_combination_right = [4, 5, 6]
        res = grid_obj.is_winner_player("O")
        response_combination = grid_obj.get_winner_combination()

        self.assertTrue(res)
        self.assertIsInstance(response_combination, list)
        self.assertEqual(response_combination, winner_combination_right)

    def test_winner_in_column1(self):

        grid_obj.grid[1] = "O"; grid_obj.grid[2] = "2";  grid_obj.grid[3]= "X"
        grid_obj.grid[4] = "O"; grid_obj.grid[5] = "5";  grid_obj.grid[6] = "O"
        grid_obj.grid[7] = "O"; grid_obj.grid[8] = "X";  grid_obj.grid[9] = "O"

        winner_combination_right = [1, 4, 7]
        res = grid_obj.is_winner_player("O")
        response_combination = grid_obj.get_winner_combination()

        self.assertTrue(res)
        self.assertIsInstance(response_combination, list)
        self.assertEqual(response_combination, winner_combination_right)

    def test_winner_in_column2(self):
        grid_obj.grid[1] = "O"; grid_obj.grid[2] = "X";  grid_obj.grid[3]= "X"
        grid_obj.grid[4] = "4"; grid_obj.grid[5] = "X";  grid_obj.grid[6] = "O"
        grid_obj.grid[7] = "7"; grid_obj.grid[8] = "X";  grid_obj.grid[9] = "O"

        winner_combination_right = [2, 5, 8]
        res = grid_obj.is_winner_player("X")
        response_combination = grid_obj.get_winner_combination()

        self.assertTrue(res)
        self.assertIsInstance(response_combination, list)
        self.assertEqual(response_combination, winner_combination_right)

    def test_winner_in_column3(self):
        grid_obj.grid[1] = "X"; grid_obj.grid[2] = "2";  grid_obj.grid[3]= "O"
        grid_obj.grid[4] = "O"; grid_obj.grid[5] = "5";  grid_obj.grid[6] = "O"
        grid_obj.grid[7] = "O"; grid_obj.grid[8] = "X";  grid_obj.grid[9] = "O"

        winner_combination_right = [3, 6, 9]
        res = grid_obj.is_winner_player("O")
        response_combination = grid_obj.get_winner_combination()

        self.assertTrue(res)
        self.assertIsInstance(response_combination, list)
        self.assertEqual(response_combination, winner_combination_right)

    def test_winner_in_diagonal1(self):
        grid_obj.grid[1] = "X"; grid_obj.grid[2] = "O";  grid_obj.grid[3]= "X"
        grid_obj.grid[4] = "4"; grid_obj.grid[5] = "X";  grid_obj.grid[6] = "O"
        grid_obj.grid[7] = "7"; grid_obj.grid[8] = "8";  grid_obj.grid[9] = "X"

        winner_combination_right = [1, 5, 9]
        res = grid_obj.is_winner_player("X")
        response_combination = grid_obj.get_winner_combination()

        self.assertTrue(res)
        self.assertIsInstance(response_combination, list)
        self.assertEqual(response_combination, winner_combination_right)

    def test_winner_in_diagonal2(self):
        grid_obj.grid[1] = "X"; grid_obj.grid[2] = "O";  grid_obj.grid[3]= "X"
        grid_obj.grid[4] = "O"; grid_obj.grid[5] = "X";  grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "X"; grid_obj.grid[8] = "8";  grid_obj.grid[9] = "9"

        winner_combination_right = [3,5,7]
        res = grid_obj.is_winner_player("X")
        response_combination = grid_obj.get_winner_combination()

        self.assertTrue(res)
        self.assertIsInstance(response_combination, list)
        self.assertEqual(response_combination, winner_combination_right)

    def test_check_who_wins(self):
        grid_obj.grid[1] = "X"; grid_obj.grid[2] = "X";  grid_obj.grid[3]= "O"
        grid_obj.grid[4] = "O"; grid_obj.grid[5] = "X";  grid_obj.grid[6] = "X"
        grid_obj.grid[7] = "O"; grid_obj.grid[8] = "X";  grid_obj.grid[9] = "O"
        winner_player_right= "X"
        winner_player_wrong = "O"

        res = grid_obj.is_winner_player("X")
        self.assertTrue(res)
        response_combination = grid_obj.get_winner()
        self.assertIsInstance(response_combination, str)
        self.assertEqual(response_combination, winner_player_right)
        self.assertNotEqual(response_combination, winner_player_wrong)

    def test_draw(self):
        grid_obj.grid[1] = "X"; grid_obj.grid[2] = "O";  grid_obj.grid[3]= "X"
        grid_obj.grid[4] = "O"; grid_obj.grid[5] = "X";  grid_obj.grid[6] = "O"
        grid_obj.grid[7] = "O"; grid_obj.grid[8] = "X";  grid_obj.grid[9] = "O"
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
        grid_obj.grid[1] = "X";  grid_obj.grid[2] = "X"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 3

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "X";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "X"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 2

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "X"; grid_obj.grid[3] = "X"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 1

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)


    def test_defense_computer_ai_second_row(self):
        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "X";  grid_obj.grid[5] = "X"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "O"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 6

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "X";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "X"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "O"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 5

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "X"; grid_obj.grid[6] = "X"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "O"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 4

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)



    def test_defense_computer_ai_third_row(self):
        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "X";  grid_obj.grid[8] = "X"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 9

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "X"; grid_obj.grid[9] = "X"
        right_cell_to_choice = 7

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "X";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "X"
        right_cell_to_choice = 8

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)


    def test_defense_computer_ai_first_column(self):
        grid_obj.grid[1] = "X";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "X";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 7

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "X";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "X";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 4

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "X";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "X";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 1

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)



    def test_defense_computer_ai_second_column(self):
        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "X"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "X"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 8

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "X"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "X"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 5

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "X"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "X"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 2

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)



    def test_defense_computer_ai_third_column(self):
        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "X"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "X"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 9

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "X"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "X"
        right_cell_to_choice = 6

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "X"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "X"
        right_cell_to_choice = 3

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)


    def test_defense_computer_ai_first_diagonal(self):
        grid_obj.grid[1] = "X";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "X"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 9

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "X";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "X"
        right_cell_to_choice = 5

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "X"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "X"
        right_cell_to_choice = 1

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)



    def test_defense_computer_ai_second_diagonal(self):
        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "X"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "X";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 3

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "X"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "X";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 5

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "X"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "X"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 7

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)




    def test_attack_computer_ai_first_row(self):
        grid_obj.grid[1] = "O";  grid_obj.grid[2] = "O"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 3

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)


        grid_obj.grid[1] = "O";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "O"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 2

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "O"; grid_obj.grid[3] = "O"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 1

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)


    def test_attack_computer_ai_second_row(self):
        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "O";  grid_obj.grid[5] = "O"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "O"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 6

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)


        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "O";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "O"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "O"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 5

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "O"; grid_obj.grid[6] = "O"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "O"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 4

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)


    def test_attack_computer_ai_third_row(self):
        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "O";  grid_obj.grid[8] = "O"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 9

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)


        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "O"; grid_obj.grid[9] = "O"
        right_cell_to_choice = 7

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "O";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "O"
        right_cell_to_choice = 8

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)


    def test_attack_computer_ai_first_column(self):
        grid_obj.grid[1] = "O";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "O";  grid_obj.grid[5] = "3"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "4"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 7

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "O";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "O";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 4

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "O";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "O";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 1

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)




    def test_attack_computer_ai_second_column(self):
        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "O"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "O"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 8

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)


        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "O"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "O"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 5

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "O"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "O"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 2

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)




    def test_attack_computer_ai_third_column(self):
        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "O"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "O"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 9

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)


        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "O"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "O"
        right_cell_to_choice = 6

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "O"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "O"
        right_cell_to_choice = 3

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)



    def test_attack_computer_ai_first_diagonal(self):
        grid_obj.grid[1] = "O";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "O"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 9

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "O";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "O"
        right_cell_to_choice = 5

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "O"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "O"
        right_cell_to_choice = 1

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)




    def test_attack_computer_ai_second_diagonal(self):
        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "O"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "O";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 3

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)


        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "O"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "O";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 5

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "O"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "O"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 7

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

    def test_attack_first_movement_if_grid_is_empty(self):
        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "5"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "9"
        right_cell_to_choice = 5

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertEqual(cell_for_defense, right_cell_to_choice)

    def test_attack_first_movement_if_central_cell_is_full(self):
        grid_obj.grid[1] = "1";  grid_obj.grid[2] = "2"; grid_obj.grid[3] = "3"
        grid_obj.grid[4] = "4";  grid_obj.grid[5] = "X"; grid_obj.grid[6] = "6"
        grid_obj.grid[7] = "7";  grid_obj.grid[8] = "8"; grid_obj.grid[9] = "9"

        cell_for_defense = computer.get_move_ai(grid_obj.grid)
        self.assertIsInstance(cell_for_defense, int)


    def test_player_name(self):
        player_name = "Player1"
        response_symbol = player.get_player_name()
        self.assertEqual(player_name, response_symbol)



    def test_player_symbol(self):
        player_symbol = "X"
        wrong_symbol = "LMK"

        response_symbol = player.get_player_symbol()
        self.assertEqual(player_symbol, response_symbol)
        self.assertNotEqual(wrong_symbol, response_symbol)


    def test_input_name(self):
        test_player = Player()
        test_player.insert_player_name("Adam")
        self.assertEqual("Adam",test_player.name)

if __name__ == '__main__':
    unittest.main()