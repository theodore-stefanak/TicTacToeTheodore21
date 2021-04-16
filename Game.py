
class Game:
    
    EMPTY = " "
    P1 = "O"
    P2 = "X"
    
    def __init__(self):
        self.__board = [[Game.EMPTY] * 3 for _ in range(3)]
        self.__player = Game.P1

    def __repr__(self):
        return ""

    def play(self,row,col):
        self.__board[row][col] = self.__player
        self.__player = Game.P1 if self.__player == Game.P2 else Game.P2
    
    @property
    def winner(self):
        if self.__board[0] == [Game.P1] * 3 or self.__board[0] == [Game.P2]:
            return True
            
        else:
            return False

if __name__ == "__main__":
    print("Testing the program")
