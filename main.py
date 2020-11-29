from utils.args import args
from objects.track import Track
from objects.car import Car


def main():
    """
    Testing:
        from random import randint
        car.accelerate((randint(-1, 1), randint(-1, 1)))

        from objects.bresenham import BresenhamPath
        BresenhamPath((0, 0), (5, 5)).get_positions()
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

    pass


if __name__ == '__main__':
    main()
    # from objects.bresenham import BresenhamPath

    # BresenhamPath((6, 6), (5, 0)).get_positions()
    # BresenhamPath((7, 6), (5, 0)).get_positions()
    # BresenhamPath((8, 6), (5, 0)).get_positions()
    # BresenhamPath((9, 6), (5, 0)).get_positions()
    # BresenhamPath((10, 6), (5, 0)).get_positions()
    # BresenhamPath((5, 0), (6, 6)).get_positions()
    # BresenhamPath((5, 0), (7, 6)).get_positions()
    # BresenhamPath((5, 0), (8, 6)).get_positions()
    # BresenhamPath((5, 0), (9, 6)).get_positions()
    # BresenhamPath((5, 0), (10, 6)).get_positions()
    #
    # BresenhamPath((5, 5), (10, 6)).get_positions()
    # BresenhamPath((5, 5), (10, 7)).get_positions()
    # BresenhamPath((5, 5), (10, 8)).get_positions()
    # BresenhamPath((5, 5), (10, 9)).get_positions()
    # BresenhamPath((10, 6), (5, 5)).get_positions()
    # BresenhamPath((10, 7), (5, 5)).get_positions()
    # BresenhamPath((10, 8), (5, 5)).get_positions()
    # BresenhamPath((10, 9), (5, 5)).get_positions()
    #
    # BresenhamPath((10, 5), (4, 6)).get_positions()
    # BresenhamPath((10, 5), (4, 7)).get_positions()
    # BresenhamPath((10, 5), (4, 8)).get_positions()
    # BresenhamPath((10, 5), (4, 9)).get_positions()
    # BresenhamPath((10, 5), (4, 10)).get_positions()
    # BresenhamPath((4, 6), (10, 5)).get_positions()
    # BresenhamPath((4, 7), (10, 5)).get_positions()
    # BresenhamPath((4, 8), (10, 5)).get_positions()
    # BresenhamPath((4, 9), (10, 5)).get_positions()
    # BresenhamPath((4, 10), (10, 5)).get_positions()
    #
    # BresenhamPath((6, 4), (5, 10)).get_positions()
    # BresenhamPath((7, 4), (5, 10)).get_positions()
    # BresenhamPath((8, 4), (5, 10)).get_positions()
    # BresenhamPath((9, 4), (5, 10)).get_positions()
    # BresenhamPath((10, 4), (5, 10)).get_positions()
    # BresenhamPath((5, 10), (6, 4)).get_positions()
    # BresenhamPath((5, 10), (7, 4)).get_positions()
    # BresenhamPath((5, 10), (8, 4)).get_positions()
    # BresenhamPath((5, 10), (9, 4)).get_positions()
    # BresenhamPath((5, 10), (10, 4)).get_positions()
    #
    # BresenhamPath((5, 5), (5, 10)).get_positions()
    # BresenhamPath((5, 5), (5, 0)).get_positions()
    # BresenhamPath((5, 5), (10, 5)).get_positions()
    # BresenhamPath((5, 5), (0, 5)).get_positions()
    # BresenhamPath((5, 5), (10, 10)).get_positions()
    # BresenhamPath((5, 5), (0, 10)).get_positions()
    # BresenhamPath((5, 5), (10, 0)).get_positions()

