import argparse


def args():
    """
    Function to create command line arguments

    Arguments:
        -rs <int>, --random_seed <int>
            Random seed for testing, seeds the rate of failed accelerations
        -t <char>, --track_name <char>
            Track letter to use as the track. Please use: 'R', 'O', or 'L'. Capitalization matters
            <R> r-track
            <O> o-track
            <L> l-track
        -rt <char>, --reset_type <char>
            Reset type for crash, S = stop, R = reset. Please use: 'S', 'R'. Capitalization matters
            <S> stop, resets velocity, increases time, but doesn't move car
            <R> reset, resets velocity, increases time, moves car back to start
        -bt <char>, --brain_type <char>
            Learning type, Q = QLearning, S = SARSA. Please use: 'Q', 'S'. Capitalization matters
            <Q> QLearning
            <S> SARSA
        -dr <float>, --discount_rate <float>
            Discount rate in Bellman's equation for value iteration
        -cd <float>, --convergence_delta <float>
            Convergence delta for value iteration
    """
    # Initialize the parser
    parser = argparse.ArgumentParser()

    # Add arguments
    parser.add_argument('-rs', '--random_seed', type=int, default=1,
                        help="Set a random seed for testing, seeds the rate of failed accelerations")
    parser.add_argument('-t', '--track_name', type=str,
                        help="Track letter to use as the track. Please use: 'R', 'O', or 'L'. Capitalization matters")
    parser.add_argument('-rt', '--reset_type', type=str, default='S',
                        help="Reset type for crash, S = stop, R = reset. Please use: 'S', 'R'. Capitalization matters")
    parser.add_argument('-bt', '--brain_type', type=str, default='Q',
                        help="Learning type, Q = QLearning, S = SARSA. Please use: 'Q', 'S'. Capitalization matters")
    parser.add_argument('-dr', '--discount_rate', type=float, default=.9,
                        help="Discount rate in Bellman's equation for value iteration")
    parser.add_argument('-cd', '--convergence_delta', type=float, default=.001,
                        help="Convergence delta for value iteration")
    parser.add_argument('-lr', '--learning_rate', type=float, default=.001,
                        help="Learning rate of value update from QLearning and SARSA")

    # Parse arguments
    command_args = parser.parse_args()

    # Return the parsed arguments
    return command_args
