from abc import ABC, abstractmethod

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
        pass

    def run(self):
        print("Running the terminal")
