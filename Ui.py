from abc import ABC, abstractmethod
from Game import Game

class Ui(ABC):

    @abstractmethod # anything that is a Ui must have a run method
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        pass

    def run(self):
        print("Running the GUI")

class Terminal(Ui):
    def __init__(self):
        self.__game = Game()

    def run(self):
        print("Running the terminal")
        while not self.__game.winner:
            print(self.__game)
            row = int(input("Enter the row: "))
            col = int(input("Enter the column: "))
            self.__game.play(row,col)
