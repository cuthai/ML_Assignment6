from utils.args import args
from objects.track import Track
from objects.car import Car


def main():
    """
    Testing:
        from random import randint
        car.accelerate((randint(-1, 1), randint(-1, 1)))
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
