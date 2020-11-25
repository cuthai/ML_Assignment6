import argparse


def args():
    """
    Function to create command line arguments

    Arguments:
        -t <char>, --track_name <char>
            Track letter to use as the track. Please use: 'R', 'O', or 'L'. Capitalization matters
    """
    # Initialize the parser
    parser = argparse.ArgumentParser()

    # Add arguments
    parser.add_argument('-t', '--track_name', type=str,
                        help="Track letter to use as the track. Please use: 'R', 'O', or 'L'. Capitalization matters")

    # Parse arguments
    command_args = parser.parse_args()

    # Return the parsed arguments
    return command_args
