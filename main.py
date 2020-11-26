from utils.args import args
from objects.track import Track
from objects.car import Car


def main():
    """
    Main function to run Neural Network
    """
    # Parse arguments
    arguments = args()

    kwargs = {
        'track_name': arguments.track_name
    }
    track = Track(**kwargs)

    kwargs = {
        'track': track
    }
    car = Car(**kwargs)

    pass


if __name__ == '__main__':
    main()
