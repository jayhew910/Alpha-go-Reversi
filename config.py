"""Class to represent a configuration file."""


class CFG(object):
    """Represents a static configuration file used through the application.

    Attributes:
        num_iterations: Number of iterations.
        num_games: Number of self play games played during each iteration.
        num_mcts_sims: Number of MCTS simulations per game.
        c_puct: The level of exploration used in MCTS.
        l2_val: The level of L2 weight regularization used during training.
        momentum: Momentum Parameter for the momentum optimizer.
        learning_rate: Learning Rate for the momentum optimizer.
        t_policy_val: Value for policy prediction.
        temp_init: Initial Temperature parameter to control exploration.
        temp_final: Final Temperature parameter to control exploration.
        temp_thresh: Threshold where temperature init changes to final.
        epochs: Number of epochs during training.
        batch_size: Batch size for training.
        dirichlet_alpha: Alpha value for Dirichlet noise.
        epsilon: Value of epsilon for calculating Dirichlet noise.
        model_directory: Name of the directory to store models.
        num_eval_games: Number of self-play games to play for evaluation.
        eval_win_rate: Win rate needed to be the best model.
        load_model: Binary to initialize the network with the best model.
        human_play: Binary to play as a Human vs the AI.
        resnet_blocks: Number of residual blocks in the resnet.
        record_loss: Binary to record policy and value loss to a file.
        loss_file: Name of the file to record loss.
        game: Number of the game. 0: Tic Tac Toe, 1: Othello, 2: Connect Four.
    """
    num_iterations = 5
    num_games = 30
    num_mcts_sims = 100
    c_puct = 5
    l2_val = 0.0001
    momentum = 0.9
    learning_rate = 0.01
    t_policy_val = 0.0001
    temp_init = 1
    temp_final = 0.001
    temp_thresh = 10
    epochs = 30
    batch_size = 128
    dirichlet_alpha = 0.5
    epsilon = 0.25
    model_directory = "./othello/models3c"
    model_directory2 = "./othello/models3b"
    num_eval_games = 10
    eval_win_rate = 0.55
    load_model = 1
    human_play = 1
    AI_play = 0
    resnet_blocks = 5
    record_loss = 1
    loss_file = "loss.txt"
    game = 1
