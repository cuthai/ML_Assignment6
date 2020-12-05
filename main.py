from utils.args import args
from objects.track import Track
from objects.car import Car
from objects.driver import Driver
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

    # Create Driver
    kwargs = {
        'car': car,
        'brain_type': arguments.brain_type,
        'discount_rate': arguments.discount_rate,
        'convergence_delta': arguments.convergence_delta,
        'learning_rate': arguments.learning_rate
    }
    driver = Driver(**kwargs)

    while not car.get_finish():
        driver.accelerate_car()


if __name__ == '__main__':
    main()
