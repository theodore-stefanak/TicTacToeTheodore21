from itertools import product

class GameError(Exception):
    """
    GameError
    """


class Game:

    P1 = 'o'
    P2 = 'x'
    DRAW = 'D'
    _EMPTY = ' '
    _DIM = 3

    def __init__(self):
        self._board = [[Game._EMPTY for _ in range(Game._DIM)] for _ in range(Game._DIM)]
        self._player = Game.P1

    def __repr__(self):
        result = "  " + " ".join(str(i+1) for i in range(Game._DIM))
        for row in range(Game._DIM):
            result += f"\n{row+1} " + "|".join(self._board[row])
            if row != Game._DIM - 1:
                dashes = "-" * (2 * Game._DIM - 1)
                result += f"\n  {dashes}"
        result += f"\n\n{self._player} turn to play"
        return result

    def play(self,row,col):
        row -= 1
        col -= 1
        if self._board[row][col] != self._EMPTY:
            raise GameError("Cannot play here")
        else:
            self._board[row][col] = self._player 
        self._player = Game.P2 if self._player is Game.P1 else Game.P1
    
    def at(self,row,col):
        row -= 1 # 0-indexing internally, but interface is 1-index
        col -= 1
        return self._board[row][col]
    
    @property
    def winner(self):
        for p in [Game.P1,Game.P2]:
            for row in range(Game._DIM):
                if all(self._board[row][col] is p for col in range(Game._DIM)):
                    return p
            for col in range(Game._DIM):
                if all(self._board[row][col] is p for row in range(Game._DIM)):
                    return p
            if all(self._board[i][i] is p for i in range(Game._DIM)):
                return p
            if all(self._board[i][Game._DIM - 1 - i] is p for i in range(Game._DIM)):
                return p
            
        num_empty = 0
        for row, col in product(range(self._DIM), range(self._DIM)):
            if self._board[row][col] == self._EMPTY:
                num_empty += 1
        if num_empty == 0:
            return Game.DRAW
        return None

if __name__ == "__main__":
    g = Game()
    print(g)

