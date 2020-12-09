Usage
	python main.py -t <str>

Args:
	-t <str>
	Required, specifies the track to use. Please use:
		R
		O
		L

	-rs <int>
	Optional, specifies the random_state of the data for splitting. Defaults to 1

	-rt <str>
	Optional, specifies the reset type. The params are:
		S, stop in place
		R, reset to start

    	-bt <int>
	Optional, specifies the brain type to use. The params are:
		Q, QLearning
		S, SARSA

	-dr <float>
	Optional, Discount rate in Bellman's equation for value iteration

	-cd <float>
	Optional, Convergence delta for value iteration

	-lr <float>
	Optional, Rate of learning for Reinforcement learning
