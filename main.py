from utils.args import args
from racetrack.track import Track


def main():
    """
    Main function to run Neural Network
    """
    # Parse arguments
    arguments = args()

    kwargs = {
        'track_name': arguments.track_name
    }
    board = Track(**kwargs)

    pass


if __name__ == '__main__':
    main()
