from objects.q_learning import QLearningBrain
from objects.sarsa import SARSABrain


class Driver:
    """
    Class Driver which moves the car around the track

    This class implements a value iteration algorithm for determining the best track positions. It also calls to the
        QLearning or SARSA algorithms in order to make use of driving around the track.
    """
    def __init__(self, car, brain_type='Q', discount_rate=.9, convergence_delta=.01):
        """
        Init Function. The brain_type is used to implement one of the two reinforcement learning algorithms. The
            discount_rate is used during value iteration to discount the cost of movement along the track. The
            convergence_delta is used to check for convergence of the value algorithm.

        Args:
            car: car, car object already on a track
            brain_type: char, reinforcement learning algorithm to use. Use 'Q' for QLearning and 'S' for SARSA
            discount_rate: float, rate at which value iteration is discounted as time goes up
            convergence_delta: float, threshold to stop value iteration
        """
        # Brain type determination
        if brain_type == 'Q':
            self.brain = QLearningBrain()
        elif brain_type == 'S':
            self.brain = SARSABrain()
        else:
            raise ValueError("Brain_Type not found, please specify 'Q' or 'S'")

        # Value iteration variables
        self.discount_rate = discount_rate
        self.convergence_delta = convergence_delta

        # Car Info
        self.car = car
        self.position = None

        # Track Info
        self.track = car.track
        self.x = self.track.x
        self.y = self.track.y

        # Initialize a matrix the size of the track for value iteration. Set to 0
        self.values = [[0 for _ in range(self.y)] for _ in range(self.x)]

        # Begin value iteration
        self.value_iteration()

    def value_iteration(self):
        """
        Value iteration function

        This function looks at the track and determines the value of moving to each position based on the Bellman's
            equation with respect to the finish line. Walls on the tracks are given a -1000 value. The value matrix
            is then saved as part of the driver's value attribute
        """
        # Initial variables to check for convergence.
        flag_convergence = False
        convergence_value_new = 0
        convergence_value_old = 0

        # Loop while not converged
        while not flag_convergence:
            # Traverse each individual cell of the value matrix
            for x in range(self.x):
                for y in range(self.y):

                    # Get the track at the current position
                    track_position = self.track.get_track_position((x, y))

                    # Finish line gets a value of 0
                    if track_position == 'F':
                        self.values[x][y] = 0

                    # Walls get a value of -1000
                    elif track_position == '#':
                        self.values[x][y] = -1000

                    # Otherwise determine the value
                    else:
                        # Our initial max_value is -1000, we are check for the best action value
                        max_value = -1000

                        # Loop through all possible x and y actions
                        for x_action in [-1, 0, 1]:
                            for y_action in [-1, 0, 1]:

                                # Calculate the resulting (x, y) position after this action
                                x_move = x + x_action
                                y_move = y + y_action

                                # For out of bounds, set to -1000
                                if (x_move < 0) | (x_move >= self.x) | (y_move < 0) | (y_move >= self.y):
                                    value = -1000

                                # Otherwise, subtract -1 and add the value of that next move
                                else:
                                    value = -1 + (self.discount_rate * self.values[x_move][y_move])

                                # If this is our current best value, save
                                if value > max_value:
                                    max_value = value

                        # After iterating through all of the actions, save the resulting max_value
                        self.values[x][y] = max_value

                        # If our max_value is better than the current convergence_value, update
                        if max_value < convergence_value_new:
                            convergence_value_new = max_value

            # Check for convergence and break while loop
            if abs(convergence_value_new - convergence_value_old) < self.convergence_delta:
                flag_convergence = True

            # If not converged, set our old to new and continue
            else:
                convergence_value_old = convergence_value_new
