from math import exp
from random import choices


class Driver:
    """
    Class Driver which moves the car around the track

    This class implements a value iteration algorithm for determining the best track positions. It also calls to the
        QLearning or SARSA algorithms in order to make use of driving around the track.
    """
    def __init__(self, car, brain_type='Q', discount_rate=.9, convergence_delta=.001, learning_rate=.9):
        """
        Init Function. The brain_type is used to implement one of the two reinforcement learning algorithms. The
            discount_rate is used during value iteration to discount the cost of movement along the track. The
            convergence_delta is used to check for convergence of the value algorithm.

        Args:
            car: car, car object already on a track
            brain_type: char, reinforcement learning algorithm to use. Use 'Q' for QLearning and 'S' for SARSA
            discount_rate: float, rate at which value iteration is discounted as time goes up
            convergence_delta: float, threshold to stop value iteration
            learning_rate: float, rate to learn using QLearning or SARSA
        """
        # Brain type determination and variables
        if brain_type not in ['Q', 'S']:
            raise ValueError("Brain_Type not found, please specify 'Q' or 'S'")
        else:
            self.brain_type = brain_type
        self.learning_rate = learning_rate

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

    def accelerate_car(self):
        """
        This function interacts with the car by calling to the car accelerate function. The chosen acceleration is
            chosen using an E-Greedy algorithm. The E-Greedy algorithm uses a softmax of the reward for each action
            against the total reward. After actions, values are updated using a QLearning algorithm.
        """
        # Grab position variables
        position = self.car.get_position()
        position_x = position[0]
        position_y = position[1]

        # Grab velocity variables
        velocity = self.car.get_velocity()
        velocity_x = velocity[0]
        velocity_y = velocity[1]

        # Starting variables for rewards
        rewards = {x: {y: 0 for y in [-1, 0, 1]} for x in [-1, 0, 1]}
        total_rewards = 0
        max_reward = -1000

        # Loop through each possible acceleration x
        for acceleration_x in rewards.keys():
            # Calculate the new position based on the current position, velocity, and acceleration
            new_position_x = position_x + velocity_x + acceleration_x

            # Loop through each possible acceleration y
            for acceleration_y in rewards[acceleration_x].keys():
                # Calculate the new position based on the current position, velocity, and acceleration
                new_position_y = position_y + velocity_y + acceleration_y

                # Try grabbing the reward for moving to that position
                try:
                    reward = self.values[new_position_x][new_position_y]
                # If there is an index error, we are out of bounds. Set the reward to that as -1000
                except IndexError:
                    reward = -1000

                # Grab the reward for moving to there
                rewards[acceleration_x][acceleration_y] = reward

                # Only add the reward to total_reward if it's > -1000, we don't want to move there
                if reward > -1000:
                    total_rewards += exp(reward)

                # Keep track of our optimal reward
                if reward > max_reward:
                    max_reward = reward

        # Start variable for probabilities
        probabilities = []

        # Loop through the possible x and y acceleration
        for acceleration_x in rewards.keys():
            for acceleration_y in rewards[acceleration_x].keys():
                # If total_rewards is 0, then we have gone out of bounds
                if total_rewards == 0:
                    total_rewards = -1000

                # Softmax calculation, if out of bounds or crashed, it will turn to 0%
                probabilities.append(exp(rewards[acceleration_x][acceleration_y]) / total_rewards)

        # Sample a single choice based on the probabilities calculated above
        choice = choices(range(9), probabilities)[0]

        # The choice is not a tuple, call to convert_choice in order to convert it
        chosen_action = self.convert_choice(choice)
        reward = rewards[chosen_action[0]][chosen_action[1]]

        # Use the chosen action to accelerate
        self.car.accelerate(chosen_action)

        # Trigger q_learning based on the optimal action
        if self.brain_type == 'Q':
            self.q_learning(position, max_reward)
        else:
            self.sarsa(position, reward)

    def convert_choice(self, choice):
        """
        This function convert the choice received into a tuple. The choice is an int from range 0-8 inclusive.

        Args:
            choice: int, choice picked during the accelerate_car function

        Returns:
            chosen_action: tuple (int, int), represents the input to the car acceleration
        """
        if not self:
            raise NotImplementedError

        # Accelerate x = -1
        if choice == 0:
            return -1, -1
        elif choice == 1:
            return -1, 0
        elif choice == 2:
            return -1, 1

        # Accelerate x = 0
        elif choice == 3:
            return 0, -1
        elif choice == 4:
            return 0, 0
        elif choice == 5:
            return 0, 1

        # Accelerate x = 1
        elif choice == 6:
            return 1, -1
        elif choice == 7:
            return 1, 0
        elif choice == 8:
            return 1, 1

    def q_learning(self, position, max_reward):
        """
        Function for updating the value matrix using the q_learning function

        Args:
            position: tuple (int, int), represents the car current location to update the value
            max_reward: float, value of the optimal reward at the position above
        """
        self.values[position[0]][position[1]] += self.learning_rate * \
                                                 (max_reward - self.values[position[0]][position[1]])

    def sarsa(self, position, prime_reward):
        """
        Function for updating the value matrix using the SARSA function

        Args:
            position: tuple (int, int), represents the car current location to update the value
            prime_reward: float, value of the movement at the new position
        """
        self.values[position[0]][position[1]] += self.learning_rate * \
                                                 (prime_reward - self.values[position[0]][position[1]])
