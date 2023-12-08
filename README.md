# alpha-go-reversi
AlphaReversi implementation based on ["Mastering the game of Go without human knowledge"](https://deepmind.com/documents/119/agz_unformatted_nature.pdf) and ["Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm"](https://arxiv.org/abs/1712.01815) by DeepMind.

The algorithm learns to play games like Chess and
Go without any human knowledge. It uses Monte Carlo Tree Search and a Deep Residual Network to evaluate
the board state and play the most promising move.

## Requirements
 - TensorFlow (Tested on 1.4.0)
 - NumPy
 - Python 3

**Options**:
* `--num_iterations`: Number of iterations.
* `--num_games`: Number of self play games played during each iteration.
* `--num_mcts_sims`: Number of MCTS simulations per game.
* `--c_puct`: The level of exploration used in MCTS.
* `--l2_val`: The level of L2 weight regularization used during training.
* `--momentum`: Momentum Parameter for the momentum optimizer.
* `--learning_rate`: Learning Rate for the momentum optimizer.
* `--t_policy_val`: Value for policy prediction.
* `--temp_init`: Initial Temperature parameter to control exploration.
* `--temp_final`: Final Temperature parameter to control exploration.
* `--temp_thresh`: Threshold where temperature init changes to final.
* `--epochs`: Number of epochs during training.
* `--batch_size`: Batch size for training.
* `--dirichlet_alpha`: Alpha value for Dirichlet noise.
* `--epsilon`: Value of epsilon for calculating Dirichlet noise.
* `--model_directory`: Name of the directory to store models.
* `--num_eval_games`: Number of self-play games to play for evaluation.
* `--eval_win_rate`: Win rate needed to be the best model.
* `--load_model`: Binary to initialize the network with the best model.
* `--human_play`: Binary to play as a Human vs the AI.
* `--resnet_blocks`: Number of residual blocks in the resnet.
* `--record_loss`: Binary to record policy and value loss to a file.
* `--loss_file`: Name of the file to record loss.
* `--game`: Number of the game. 0: Tic Tac Toe, 1: Othello.

**The models file in othello**
models3a : n=10
models3b : n=30, epoch=50
models3c : n=100
models4a : epoch=10
models4b : epoch=30, cpuct=5, epsilon=0.25
models5a : cpuct=1
models5b : cpuct=20
models6a : epsilon=0
models6c : epsilon=0.5

best param : n=100, cpuct=5, epoch=50, epsilon=0.25
