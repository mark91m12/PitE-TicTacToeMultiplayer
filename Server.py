#Server
#Authors Mario Carricato & Marco Amato

import socket  # Import socket module
from Player import Player
from Grid import Grid
import json
import time

PORT = 9999  # Reserve a port for your service.
HOST = socket.gethostname()  # Get local machine name

# players index of Server list
PLAYER_1 = 0
PLAYER_2 = 1

# messages types codes
UPDATE_GUI = 0
MOVE_REQUEST = 1
END_GAME = 2


class Server:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create socket
        self.server_socket.bind((HOST, PORT))  # Bind to the port
        self.server_socket.listen(5)  # Now wait for client connection.
        self.players = []  # list of players
        self.grid = Grid()  # game Grid
        self.player_winner = ""  # winner
        self.draw = False  # draw

    # send request to client by Server
    def send_request(self, message, player, type):
        json_data = json.dumps(
            {"grid": self.grid.list, "message": message, "name": self.players[player].get_name(), "type": type})
        self.players[player].get_connection().send(json_data.encode())

    # check if player won the game
    def check_victory(self, player):
        if self.grid.is_winner_player(player.get_symbol()):
            print("\n")
            print("\033[31;1mResult:\033[0m " + player.get_name() + " wins")
            print("\n")
            self.player_winner = player.get_name()
            return True
        else:
            return False

    # check if the match terminates with a draw
    def check_draw(self, moves_number):
        if self.grid.is_grid_full(moves_number):
            self.draw = True
            return self.draw
        else:
            return self.draw

    # Server start listening
    def start_server(self):

        print('Server listening.')
        print(HOST)  # name of machine that host the game server

        while True:  # SERVER LISTENING FOR CLIENTS

            connection, address = self.server_socket.accept()  # Establish connection with client.
            print('Got connection from', address)
            player = Player()
            player.init_player("", address, connection)

            # server send welcome to client address and request a name
            player.get_connection().send(
                ("Welcome " + str(player.get_address()) + "\nPlease insert your name").encode())

            # server receive the name by client
            player.set_name(player.get_connection().recv(1024).decode())

            if len(self.players) >= 1:    # in this case player 2 join the match
                player.set_symbol("\033[38;5;14mO\033[0m")  # code used to color the symbol O
                player.get_connection().send(
                    ("Prepare to play againts " + self.players[PLAYER_1].get_name()).encode())

            else:  # in this case player 1 join the match
                player.set_symbol("\033[38;5;11mX\033[0m")  # code used to color the symbol X
                player.get_connection().send(
                    ("Prepare for the match " + str(player.get_name()) + "\nWaiting for opponents").encode())

            # add player to server list
            self.players.append(player)

            is_game_ended = False

            if (len(self.players) == 2):

                welcome_message = "***** START MATCH *****\n" + \
                                  self.players[PLAYER_1].get_name() + " VS " + self.players[
                                      PLAYER_2].get_name() + "\n" + \
                                  self.players[PLAYER_1].get_name() + " will play with symbol " + self.players[
                                      PLAYER_1].get_symbol() + "\n" + \
                                  self.players[PLAYER_2].get_name() + " will play with symbol " + self.players[
                                      PLAYER_2].get_symbol() + "\n"

                print(welcome_message)

                self.players[PLAYER_1].get_connection().send(welcome_message.encode())
                self.players[PLAYER_2].get_connection().send(welcome_message.encode())

                time.sleep(4)

                message_not_empty = "sorry this cell is not empty.\nChoose another one:"
                message_turn = "it's your turn\nPlease make your choice : "

                # counter used to see if the game terminates with a draw
                moves_number = 0
                while not is_game_ended:  # MAIN LOOP FOR THE GAME MATCH

                    self.send_request(message_turn, PLAYER_1, MOVE_REQUEST)
                    self.send_request("", PLAYER_2, UPDATE_GUI)

                    choice_check = True

                    # manage input player1
                    while choice_check:

                        choice = int((self.players[PLAYER_1].get_connection().recv(1024).decode()))

                        # check if the choice is valid or not ( empty cell )
                        if self.grid.list[choice] != self.players[PLAYER_1].get_symbol() and self.grid.list[choice] != \
                                self.players[PLAYER_2].get_symbol():
                            self.grid.list[choice] = self.players[PLAYER_1].get_symbol()
                            moves_number += 1
                            self.send_request("", PLAYER_1, UPDATE_GUI)
                            choice_check = False
                        else:

                            self.send_request(message_not_empty, PLAYER_1, MOVE_REQUEST)

                    if self.check_victory(self.players[PLAYER_1]) or self.check_draw(moves_number):
                        is_game_ended = True

                    if not is_game_ended:  # player 1 did not win the game

                        self.send_request(message_turn, PLAYER_2, MOVE_REQUEST)

                        choice_check = True

                        # manage input player1
                        while choice_check:

                            choice = int((self.players[PLAYER_2].get_connection().recv(1024).decode()))

                            # check if the choice is valid or not ( empty cell )
                            if self.grid.list[choice] != self.players[PLAYER_1].get_symbol() and self.grid.list[
                                choice] != self.players[PLAYER_2].get_symbol():
                                self.grid.list[choice] = self.players[PLAYER_2].get_symbol()
                                moves_number += 1
                                self.send_request("", PLAYER_2, UPDATE_GUI)
                                choice_check = False
                            else:
                                message = "sorry this cell is not empty.\nChoose another one:"
                                self.send_request(message_not_empty, PLAYER_2, MOVE_REQUEST)
                                time.sleep(1)

                        if self.check_victory(self.players[PLAYER_2]) or self.check_draw(moves_number):
                            is_game_ended = True

                if not self.draw:
                    message_winner = "\033[92mCongratulations, you won the game!!!\033[0m \n"
                    message_loser = "\033[31;1mYou Lose...\033[0m\n"

                    if self.player_winner == self.players[PLAYER_1].get_name():
                        self.send_request(message_winner, PLAYER_1, END_GAME)
                        self.send_request(message_loser, PLAYER_2, END_GAME)
                    else:
                        self.send_request(message_winner, PLAYER_2, END_GAME)
                        self.send_request(message_loser, PLAYER_1, END_GAME)
                else:
                    message_draw = "\033[38;5;13mThe Match terminates with a Draw!!!\033[0m\n"
                    self.send_request(message_draw, PLAYER_1, END_GAME)
                    self.send_request(message_draw, PLAYER_2, END_GAME)


Server().start_server()