from utils.args import args
from objects.track import Track
from objects.car import Car
from random import seed


def main():
    """
    """
    # Parse arguments
    arguments = args()

    # Set seed
    seed(arguments.random_seed)

    # Create Track
    kwargs = {
        'track_name': arguments.track_name
    }
    track = Track(**kwargs)

    # Create Car
    kwargs = {
        'track': track,
        'reset_type': arguments.reset_type
    }
    car = Car(**kwargs)

    pass


if __name__ == '__main__':
    main()
