<p align="center">
  <img width="460" height="300" src="https://github.com/Mario181091/Mario_content/blob/master/Senza%20titolo-3.jpg">
</p>

# PitE-TicTacToeMultiplayer

This is the third homework of the course "Python in the Enterprise", as requested has been implemented an exention of the Tic Tac Toe single player version (for the previous version you can find further information in this [page](https://github.com/mark91m12/PitE-TicTacToe)), in particular has been implemented a simple Client - Server game.

<p align="center">
  <img width="460" height="300" src="https://github.com/Mario181091/Mario_content/blob/master/client-server.jpg">
</p>

## Features

* possibility to choose single or multiplayer game mode
* 1 Vs PC mode
* Player1 Vs Player2 multiplayer mode

## Getting Started

**Prerequisites**
* In order to run this project is important to use python version 3 or upper.                                                    
  Install it with:
  
  ```shell
  $ sudo apt-get install python3
  ```
  now check your version: 
  ```shell
  $ python --version
  ```
## Basic Usage
**Server Side**
* Running this command to start the Server : 

  ```shell
  $ python3 Server.py
  ```
  
  ```shell
     Server listening.
     10.205.12.240
  ```
 

**Client Side**
* Running this command to start the Game : 

  ```shell
  $ python3 Client.py
  ```
  
  ```shell
  ************************************************
  *****           Tic Tac Toe Game          ******
  ************************************************
  *                                              *
  *               Play single player  --- s      *
  *                                              *
  *               Play multi player   --- m      *
  *                                              *
  ************************************************
  Please, choose one mode ( s or m ) ----> _
  ```
 
* Once that multiplayer mode is choosed first user must enter the ip address of the server and the port, at this point he will be put on hold from the server waiting for opponents :


   ```
    please insert ip address of the game server
   >10.205.12.240
    please insert Port number of the game server
   >9999
    waiting for server connection...
    Welcome ('10.205.12.240', 59287)
    Please insert your name
   >Marco
    Prepare for the match Marco
    Waiting for opponents
   ```
    
 * When the second player enter the data the game can start :
    
    
   ```
    please insert ip address of the game server
   >10.205.12.240
    please insert Port number of the game server
   >9999
    waiting for server connection...
    Welcome ('127.0.1.1', 59346)
    Please insert your name
   >Mario
    Prepare to play againts Marco
   ```
   
## Game Screen

In this section are proprosed some screenshots of game, both Server and Client sides. 

* Server side
<p align="center">
  <img width="660" height="300" src="https://github.com/Mario181091/Mario_content/blob/master/Schermata%20del%202018-04-15%2018-25-34.png">
</p>


* Client side
<p align="center">
  <img width="660" height="300" src="https://github.com/Mario181091/Mario_content/blob/master/Schermata%20del%202018-04-15%2018-22-36.png">
</p>


  
  
## Authors

* **Mario Egidio Carricato** - *Erasmus student AGH* - [other projects](https://github.com/mario181091)
* **Marco Amato** - *Erasmus student AGH* - [other projects](https://github.com/mark91m12)
