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

    car.accelerate((-1, 0))
    car.accelerate((-1, 0))
    car.accelerate((-1, 0))
    car.accelerate((-1, 0))
    car.accelerate((-1, 0))

    car.accelerate((1, 1))
    car.accelerate((1, 1))
    car.accelerate((1, 1))
    car.accelerate((1, 1))
    car.accelerate((1, 1))

    car.accelerate((-1, -1))
    car.accelerate((-1, -1))
    car.accelerate((-1, -1))
    car.accelerate((0, 0))
    car.accelerate((0, 0))

    car.accelerate((-1, 1))
    car.accelerate((-1, 1))

    pass


if __name__ == '__main__':
    main()
