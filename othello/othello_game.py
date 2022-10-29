"""Class for Board State and Logic."""
from copy import deepcopy
from collections import Counter

import numpy as np

from game import Game


class OthelloGame(Game):
    """Represents the game board and its logic.

    Attributes:
        row: An integer indicating the length of the board row.
        column: An integer indicating the length of the board column.
        current_player: An integer to keep track of the current player.
        state: A list which stores the game state in matrix form.
        action_size: An integer indicating the total number of board squares.
        directions: A dictionary containing tuples to check for valid moves.
    """

    def __init__(self):
        """Initializes TicTacToeGame with the initial board state."""
        super().__init__()
        self.row = 8
        self.column = 8
        self.current_player = -1
        self.state = []
        self.action_size = self.row * self.column

        # Create a n x n matrix to represent the board
        for i in range(self.row):
            self.state.append([0 * j for j in range(self.column)])

        self.state[(self.row // 2) - 1][(self.column // 2) - 1] = -1
        self.state[(self.row // 2)][(self.column // 2)] = -1
        self.state[(self.row // 2) - 1][(self.column // 2)] = 1
        self.state[(self.row // 2)][(self.column // 2) - 1] = 1

        self.state = np.array(self.state)

        self.directions = {
            0: (-1, -1),
            1: (-1, 0),
            2: (-1, 1),
            3: (0, -1),
            4: (0, 1),
            5: (1, -1),
            6: (1, 0),
            7: (1, 1)
        }

    def clone(self):
        """Creates a deep clone of the game object.

        Returns:
            the cloned game object.
        """
        game_clone = OthelloGame()
        game_clone.state = deepcopy(self.state)
        game_clone.current_player = self.current_player
        return game_clone
    
    def is_on_board(self, x, y):
        """
        判断坐标是否出界
        :param x: row 行坐标
        :param y: col 列坐标
        :return: True or False
        """
        return x >= 0 and x <= 7 and y >= 0 and y <= 7

    def play_action(self, action):
        """Plays an action on the game board.

        Args:
            action: A tuple in the form of (row, column, direction).
        """
        x = action[1]
        y = action[2]
        d = action[3]

        self.state[x][y] = self.current_player

        count = 0

        # Flip all opponent pieces which are in the sandwich.
        while True:
            row = x + d[0] * count
            col = y + d[1] * count

            if self.state[row][col] == -self.current_player:
                self.state[row][col] = self.current_player
                count += 1
            else:
                break

        self.current_player = -self.current_player
        
    def play_action_human(self, action):
        """Plays an action on the game board.

        Args:
            action: A tuple in the form of (row, column, direction).
        """
        xstart = action[1]
        ystart = action[2]
        
        if not self.is_on_board(xstart, ystart) or self.state[xstart][ystart] != 0:
            return False
            
        self.state[xstart][ystart] = self.current_player
        Flip = []
        adjecent = [[0, 1], [0, -1], [1, 1], [1, -1], [1, 0], [-1, 0], [-1, 1],[-1, -1]]
        for xd, yd in adjecent:
            x, y = xstart, ystart
            x += xd
            y += yd
            if self.is_on_board(x, y) and self.state[x][y] == -self.current_player:
                 x += xd
                 y += yd
                 if not self.is_on_board(x, y):
                     continue
                 #untile it reach the position where not the opponent's chess
                 while self.state[x][y] == -self.current_player:
                     x += xd
                     y += yd
                     if not self.is_on_board(x, y):
                         break
            #out of board
            if not self.is_on_board(x, y):
                     continue
            #own chess
            if self.state[x][y] == self.current_player:
                while True:
                    x -= xd
                    y -= yd
                    #back to the beginning position
                    if x == xstart and y == ystart:
                        break
                    #chess that need to be flip
                    Flip.append([x, y])
                    
        #undo the temporally chess
        #self.state[xstart][ystart] = 0
    
        #if no chess to flip, invalid move
        if len(Flip) == 0:
            self.state[xstart][ystart] = 0
            return False
        
        for nx,ny in Flip:
            x, y = nx,ny
            self.state[x][y] = self.current_player

        self.current_player = -self.current_player

    def get_valid_moves(self, current_player):
        """Returns a list of moves along with their validity.

        Searches the board for valid sandwich moves.

        Returns:
            A list containing moves as (validity, row, column, direction).
        """
        valid_moves = []

        pl = current_player

        side = self.row

        for x in range(self.row):
            for y in range(self.column):
                found = False

                # Search for empty squares.
                if self.state[x][y] == 0:

                    # Search in all 8 directions for a square of the opponent.
                    for i in range(len(self.directions)):
                        d = self.directions[i]

                        row = x + d[0]
                        col = y + d[1]

                        if row < side and col < side:
                            if self.state[row][col] == -pl:
                                found_valid_move = False
                                count = 2

                                # Keep searching for a sandwich condition.
                                while True:
                                    row = x + d[0] * count
                                    col = y + d[1] * count

                                    if 0 <= row < side and 0 <= col < side:
                                        if self.state[row][col] == pl:
                                            valid_moves.append((1, x, y, d))
                                            found_valid_move = True
                                            break
                                    else:
                                        break

                                    count += 1

                                if found_valid_move:
                                    found = True
                                    break

                if not found:
                    valid_moves.append((0, None, None, None))

        return np.array(valid_moves)

    def check_game_over(self, current_player):
        """Checks if the game is over and return a possible winner.

        There are 3 possible scenarios.
            a) The game is over and we have a winner.
            b) The game is over but it is a draw.
            c) The game is not over.

        Args:
            current_player: An integer representing the current player.

        Returns:
            A bool representing the game over state.
            An integer action value. (win: 1, loss: -1, draw: 0
        """

        player_a = current_player
        player_b = -current_player

        player_a_moves = self.get_valid_moves(player_a)
        player_b_moves = self.get_valid_moves(player_b)

        player_a_valid_count = Counter(x[0] == 1 for x in player_a_moves)
        player_b_valid_count = Counter(x[0] == 1 for x in player_b_moves)

         # Check if both players can't play any more moves.
        if player_a_valid_count[True] == 0 or player_b_valid_count[True] == 0:
            #unique, piece_count = np.unique(self.state,
             #                               return_counts=True)
            piece_count_a = piece_count_b = 0
            for x in range(self.row):
                for y in range(self.column):
                    if self.state[x][y]==player_a:
                        piece_count_a += 1
                    if self.state[x][y]==player_b:
                        piece_count_b += 1
                        
            # Check for the player with the most number of pieces.
            if piece_count_a > piece_count_b:
                return True, 1
            elif piece_count_a == piece_count_b:
                return True, 0
            else:
                return True, -1
        else:
            return False, 0

    def print_board(self):
        """Prints the board state."""
        print("   0    1    2    3    4    5    6    7")
        for x in range(self.row):
            print(x, end='')
            for y in range(self.column):
                if self.state[x][y] == 0:
                    print('  -  ', end='')
                elif self.state[x][y] == 1:
                    print('  X  ', end='')
                elif self.state[x][y] == -1:
                    print('  O  ', end='')
            print('\n')
        print('\n')
