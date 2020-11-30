from objects.q_learning import QLearningBrain
from objects.sarsa import SARSABrain


class Driver:
    def __init__(self, brain_type='Q'):
        if brain_type == 'Q':
            self.brain = QLearningBrain()
        else:
            self.brain = SARSABrain()
