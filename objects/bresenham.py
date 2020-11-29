class BresenhamPath:
    """
    Python 3 program for Bresenham’s Line Generation. Modified from the following source by ash264:
    https://www.geeksforgeeks.org/bresenhams-line-generation-algorithm/
    """
    def __init__(self, last_position, new_position):
        self.last_position = last_position
        self.new_position = new_position

        if last_position[1] - new_position[1] == 0:
            slope = 0
            self.positions = list(zip(range(min(last_position[0], new_position[0]),
                                            max(last_position[0], new_position[0]) + 1),
                                      [last_position[1] for _ in range(last_position[1] + 1)]))
        elif last_position[0] - new_position[0] == 0:
            slope = 0
            self.positions = list(zip([last_position[0] for _ in range(last_position[0] + 1)],
                                      range(min(last_position[1], new_position[1]),
                                            max(new_position[1], last_position[1]) + 1)))
        else:
            slope = (last_position[1] - new_position[1]) / (last_position[0] - new_position[0])

        if slope > 1:
            self.positions = self.calculate_bresenhams_algorithm_1()
        elif 0 < slope < 1:
            self.positions = self.calculate_bresenhams_algorithm_2()
        elif -1 < slope < 0:
            self.positions = self.calculate_bresenhams_algorithm_3()
        elif slope < -1:
            self.positions = self.calculate_bresenhams_algorithm_4()
        elif slope in [1, -1]:
            self.positions = list(zip(range(min(last_position[0], new_position[0]),
                                            max(last_position[0], new_position[0]) + 1),
                                      range(min(last_position[1], new_position[1]),
                                            max(last_position[1], new_position[1]) + 1)))

    def calculate_bresenhams_algorithm_1(self):
        """
        Function to calculate bresenhams with a positive slope where y is increasing faster

        Returns:
            track_positions: list tuple (int, int), a list of the track positions passed through
        """
        start = self.last_position
        end = self.new_position

        if self.last_position[1] > self.new_position[1]:
            start = self.new_position
            end = self.last_position

        # Assign x and y to match algorithm
        x1 = start[0]
        y1 = start[1]
        x2 = end[0]
        y2 = end[1]

        # List for storing the positions passed through
        positions = []

        # Functions for line generation
        m_new = 2 * (x2 - x1)
        slope_error_new = m_new - (y2 - y1)

        # Generate path
        x = x1
        for y in range(y1 + 1, y2 + 1):
            # Save the position
            positions.append((x, y))

            # Add slope to increment angle formed
            slope_error_new += m_new

            # Slope error reached limit, time to increment y and update slope error.
            if slope_error_new >= 0:
                x += 1
                slope_error_new = slope_error_new - 2 * (y2 - y1)

        return positions

    def calculate_bresenhams_algorithm_2(self):
        """
        Function to calculate bresenhams with a positive slope where x is increasing faster

        Returns:
            track_positions: list tuple (int, int), a list of the track positions passed through
        """
        start = self.last_position
        end = self.new_position

        if self.last_position[0] > self.new_position[0]:
            start = self.new_position
            end = self.last_position

        # Assign x and y to match algorithm
        x1 = start[0]
        y1 = start[1]
        x2 = end[0]
        y2 = end[1]

        # List for storing the positions passed through
        positions = []

        # Functions for line generation
        m_new = 2 * (y2 - y1)
        slope_error_new = m_new - (x2 - x1)

        # Generate path
        y = y1
        for x in range(x1 + 1, x2 + 1):
            # Save the position
            positions.append((x, y))

            # Add slope to increment angle formed
            slope_error_new += m_new

            # Slope error reached limit, time to increment y and update slope error.
            if slope_error_new >= 0:
                y += 1
                slope_error_new = slope_error_new - 2 * (x2 - x1)

        return positions

    def calculate_bresenhams_algorithm_3(self):
        """
        Function to calculate bresenhams with a negative slope where x is increasing faster

        Returns:
            track_positions: list tuple (int, int), a list of the track positions passed through
        """
        start = self.last_position
        end = self.new_position

        if self.last_position[0] > self.new_position[0]:
            start = self.new_position
            end = self.last_position

        # Assign x and y to match algorithm
        x1 = start[0]
        y1 = start[1]
        x2 = end[0]
        y2 = end[1]

        # List for storing the positions passed through
        positions = []

        # Functions for line generation
        m_new = 2 * (y1 - y2)
        slope_error_new = m_new - (x2 - x1)

        # Generate path
        y = y1
        for x in range(x1 + 1, x2 + 1):
            # Save the position
            positions.append((x, y))

            # Add slope to increment angle formed
            slope_error_new += m_new

            # Slope error reached limit, time to increment y and update slope error.
            if slope_error_new >= 0:
                y -= 1
                slope_error_new = slope_error_new - 2 * (x2 - x1)

        return positions

    def calculate_bresenhams_algorithm_4(self):
        """
        Function to calculate bresenhams with a negative slope where y is increasing faster

        Returns:
            track_positions: list tuple (int, int), a list of the track positions passed through
        """
        start = self.last_position
        end = self.new_position

        if self.last_position[1] > self.new_position[1]:
            start = self.new_position
            end = self.last_position

        # Assign x and y to match algorithm
        x1 = start[0]
        y1 = start[1]
        x2 = end[0]
        y2 = end[1]

        # List for storing the positions passed through
        positions = []

        # Functions for line generation
        m_new = 2 * (x1 - x2)
        slope_error_new = m_new - (y2 - y1)

        # Generate path
        x = x1
        for y in range(y1 + 1, y2 + 1):
            # Save the position
            positions.append((x, y))

            # Add slope to increment angle formed
            slope_error_new += m_new

            # Slope error reached limit, time to increment y and update slope error.
            if slope_error_new >= 0:
                x -= 1
                slope_error_new = slope_error_new - 2 * (y2 - y1)

        return positions

    def get_positions(self):
        print(f'Positions: {self.positions}')
        return self.positions
