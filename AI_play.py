"""Class containing AI vs AI functions."""
from mcts import MonteCarloTreeSearch, TreeNode
from config import CFG


class AIplayer(object):
    """Class with functions for a Human vs an AI game.

    Attributes:
        game: An object containing the game state.
        net1: An object containing the neural network.
        net2: An object containing the neural network.
    """

    def __init__(self, net1, net2, game):
        """Initializes HumanPlay with the board state and neural network."""
        self.net1 = net1
        self.net2 = net2
        self.game = game
        

    def play(self):
        """Function to play a game vbetween the AI."""
        print("Start AI vs AI\n")
        
        AIreversi1 = MonteCarloTreeSearch(self.net1)
        AIreversi2 = MonteCarloTreeSearch(self.net2)
        game = self.game.clone()  # Create a fresh clone for each game.
        game_over = False
        value = 0
        node = TreeNode()
        wins = 0
        losses = 0
        draws = 0 

        # Self-play loop
        for i in range(CFG.num_eval_games):
            print("Start Game:", i, "\n")

            game = self.game.clone()  # Create a fresh clone for each game.
            game_over = False
            value = 0
            node = TreeNode()

            player = game.current_player

            # Keep playing until the game is in a terminal state.
            while not game_over:
                # MCTS simulations to get the best child node.
                # If player_to_eval is 1 play using the current network
                # Else play using the evaluation network.
                if game.current_player == -1:
                    best_child = AIreversi1.search(game, node, CFG.temp_final)
                else:
                    best_child = AIreversi2.search(game, node, CFG.temp_final)

                action = best_child.action
                game.play_action(action)  # Play the child node's action.

                game.print_board()

                game_over, value = game.check_game_over(player)

                best_child.parent = None
                node = best_child  # Make the child node the root node.

            if value == 1:
                print("win")
                wins += 1
            elif value == -1:
                print("loss")
                losses += 1
            else:
                print("draw")
                draws += 1
            print("\n")

        print("win = ",wins)
        print("lose = ",losses)
        print("draw = ",draws)
        win_r = wins/CFG.num_eval_games
        print("win_ratio",win_r)

