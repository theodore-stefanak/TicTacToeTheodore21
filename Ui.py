from Game import Game
from Game import GameError
from abc import ABC, abstractmethod
from tkinter import Button, Tk, Frame, X

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        root = Tk()
        root.title("Tic Tac Toe")
        frame = Frame(root)
        frame.pack()
        Button(
            frame,
            text='Show Help',
            command= self._help_callback).pack(fill=X)
        
        Button(
            frame,
            text='Play Game',
            command= self._play_callback).pack(fill=X)
        Button(
            frame,
            text='Quit',
            command= self._quit_callback).pack(fill=X)
        
        self.__root = root
        
    def _help_callback(self):
        pass
    
    def _play_callback(self):
        pass
    
    def _quit_callback(self):
        self.__root.quit()
        pass

    def run(self):
        self.__root.mainloop()

class Terminal(Ui):
    def __init__(self):
        self._game = Game()

    def run(self):
        while not self._game.winner:
            print(self._game)
            try: # Type check
                row = int(input("Which row? "))
                col = int(input("Which column? "))
            except ValueError:
                print("Non numeric input")
                continue
            if 1 <= row <= self._game._DIM and 1 <= col <= self._game._DIM: # Range check
                try:
                    self._game.play(row,col)
                except GameError:
                    print("Invalid input")
            else:
                print("Row and column must be between 1 and 3")

        print(self._game)
        w = self._game.winner
        if w == Game.DRAW:
            print("The game was drawn")
        else:
            print(f"The winner was {w}")