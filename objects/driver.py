from objects.q_learning import QLearningBrain
from objects.sarsa import SARSABrain


class Driver:
    def __init__(self, car, brain_type='Q', discount_rate=.9):
        if brain_type == 'Q':
            self.brain = QLearningBrain()
        else:
            self.brain = SARSABrain()

        self.discount_rate = discount_rate

        self.car = car
        self.track = car.track
        self.x = self.track.x
        self.y = self.track.y
        self.finish_positions = self.track.finish_positions

        self.values = [[0 for _ in range(self.y)] for _ in range(self.x)]

        self.position = None

    def value_iteration(self):
        flag_convergence = False
        convergence_value_new = 0
        convergence_value_old = 0

        while not flag_convergence:
            for x in range(self.x):
                for y in range(self.y):
                    track_position = self.track.get_track_position((x, y))
                    if track_position == 'F':
                        self.values[x][y] = 0

                    elif track_position == '#':
                        self.values[x][y] = -1000

                    else:
                        max_value = -1000

                        for x_action in [-1, 0, 1]:
                            for y_action in [-1, 0, 1]:
                                x_move = x + x_action
                                y_move = y + y_action
                                if (x_move < 0) | (x_move >= self.x) | (y_move < 0) | (y_move >= self.y):
                                    value = -1000
                                else:
                                    value = -1 + (self.discount_rate * self.values[x_move][y_move])

                                if value > max_value:
                                    max_value = value

                        self.values[x][y] = max_value

                        if max_value < convergence_value_new:
                            convergence_value_new = max_value

            if abs(convergence_value_new - convergence_value_old) < .0001:
                flag_convergence = True
            else:
                convergence_value_old = convergence_value_new
