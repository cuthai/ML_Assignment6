from utils.args import args
from objects.track import Track
from objects.car import Car
from objects.driver import Driver
from random import seed


def main():
    """
    Main function to create a track and race car

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
    # Parse arguments
    arguments = args()

    # Set seed
    if arguments.random_seed:
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

    # Drive
    while not car.get_finish():
        driver.accelerate_car()

    # Save Data
    driver.summarize(arguments.random_seed)


if __name__ == '__main__':
    main()
