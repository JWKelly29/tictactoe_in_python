#TicTacToe

#Description

Simple multiplayer TicTacToe game built using python. The program was built in order to help myself learn object orientated design and test driven development in python.

#How to setup the project on your Computer

*Assuming you have OS X*

- In the terminal, enter the command `git clone https://github.com/JWKelly29/tictactoe_in_python.git`. This will create a copy of this project.

- In the terminal, enter the command `cd tictactoe`. This will change your directory to the project directory.

- In the terminal enter the command `brew install python`. This will install the latest version of python, pip and setup tools.

#How to use

- After completing initial setup...

- In the terminal, enter the command `python`. This will open up the python interactive shell.

- In the terminal, interact with the program by first executing the app file `execfile('app/game.py')` and then creating an instance of a game `game = Game()`

- In the terminal, run the command `game.main()` to start the game. The rest of the instructions are in the game.

#How to run the Tests

- After completing initial setup...

- In the terminal, install nosetests by entering the command `pip install nose`.

- In the terminal, enter the command `nosetests`.

#Possible future additions

- Adding the option to play a computer opponent.

- Use a minmax algorithm to make the computer opponent unbeatable.

- Adding mocks and stubs to tests.

- Adding integration tests.

