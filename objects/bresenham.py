class BresenhamPath:
    """
    Python 3 program for Bresenham’s Line Generation. Modified from the following source by ash264:
        https://www.geeksforgeeks.org/bresenhams-line-generation-algorithm/

    This class implements different path algorithms depending on direction of the slope and returns the positions
        traveled between a start and end position
    """
    def __init__(self, last_position, new_position):
        """
        Init function, takes two positional tuples determines the slope between them and then adds a list of the
            positional tuples between them to this object. There are 6 Bresenham's Line Generation to choose from
            depending on the magnitude and direction of the slope

        Args:
            last_position: tuple (int, int), starting position before movement
            new_position: tuple (int, int), end position after applying velocity changes
        """
        # Save last and new
        self.last_position = last_position
        self.new_position = new_position

        # Calculation of slope. If x delta or y delta = 0 hard code the slope to some positive number around 1
        # If y delta = 0, then set slope to less than 1 to trigger positive slope path calculation
        if last_position[1] - new_position[1] == 0:
            slope = .75
        # If x delta = 0, then set slope to greater than 1 to trigger positive slope path calculation
        elif last_position[0] - new_position[0] == 0:
            slope = 1.75
        # Otherwise, proceed with normal slope calculation
        else:
            slope = (last_position[1] - new_position[1]) / (last_position[0] - new_position[0])

        # Handler for grabbing the correct bresenhams algorithm depending on direction of slope
        # Positive slopes
        # y > x
        if slope > 1:
            self.positions = self.calculate_bresenhams_algorithm_1()
        # x > y
        elif 0 < slope < 1:
            self.positions = self.calculate_bresenhams_algorithm_2()

        # Negative slopes
        # x > y
        elif -1 < slope < 0:
            self.positions = self.calculate_bresenhams_algorithm_3()
        # y > x
        elif slope < -1:
            self.positions = self.calculate_bresenhams_algorithm_4()

        # Edge cases
        # Slope is positive x = y
        elif slope == 1:
            self.positions = self.calculate_bresenhams_algorithm_5()
        # Slope is negative x = y
        elif slope == -1:
            self.positions = self.calculate_bresenhams_algorithm_6()

    def calculate_bresenhams_algorithm_1(self):
        """
        Function to calculate bresenhams with a positive slope where y is increasing faster

        Returns:
            track_positions: list tuple (int, int), a list of the track positions passed through
        """
        # Define start and end, swap if needed
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

        # List for storing the positions passed through, add start
        positions = [start]

        # Functions for line generation
        m_new = 2 * (x2 - x1)
        slope_error_new = m_new - (y2 - y1)

        # Generate path, skipping start
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
        # Define start and end, swap if needed
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

        # List for storing the positions passed through, add start
        positions = [start]

        # Functions for line generation
        m_new = 2 * (y2 - y1)
        slope_error_new = m_new - (x2 - x1)

        # Generate path, skipping start
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
        # Define start and end, swap if needed
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

        # List for storing the positions passed through, add start
        positions = [start]

        # Functions for line generation
        m_new = 2 * (y1 - y2)
        slope_error_new = m_new - (x2 - x1)

        # Generate path, skipping start
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
        Function to calculate bresenhams with a negative slope where x is increasing faster

        Returns:
            track_positions: list tuple (int, int), a list of the track positions passed through
        """
        # Define start and end, swap if needed
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

        # List for storing the positions passed through, add start
        positions = [start]

        # Functions for line generation
        m_new = 2 * (x1 - x2)
        slope_error_new = m_new - (y2 - y1)

        # Generate path, skipping start
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

    def calculate_bresenhams_algorithm_5(self):
        """
        Function to calculate bresenhams with a positive slope where x = y

        Returns:
            track_positions: list tuple (int, int), a list of the track positions passed through
        """
        # Define start and end, swap if needed
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

        # List for storing the positions passed through, don't append start here
        positions = []

        # Functions for line generation
        m_new = 2 * (y2 - y1)
        slope_error_new = m_new - (x2 - x1)

        # Generate path, starting from start
        y = y1
        for x in range(x1, x2 + 1):
            # Save the position
            positions.append((x, y))

            # Add slope to increment angle formed
            slope_error_new += m_new

            # Slope error reached limit, time to increment y and update slope error.
            if slope_error_new >= 0:
                y += 1
                slope_error_new = slope_error_new - 2 * (x2 - x1)

        return positions

    def calculate_bresenhams_algorithm_6(self):
        """
        Function to calculate bresenhams with a negative slope where x = y

        Returns:
            track_positions: list tuple (int, int), a list of the track positions passed through
        """
        # Define start and end, swap if needed
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

        # List for storing the positions passed through, don't append start here
        positions = []

        # Functions for line generation
        m_new = 2 * (y1 - y2)
        slope_error_new = m_new - (x2 - x1)

        # Generate path, starting from start
        y = y1
        for x in range(x1, x2 + 1):
            # Save the position
            positions.append((x, y))

            # Add slope to increment angle formed
            slope_error_new += m_new

            # Slope error reached limit, time to increment y and update slope error.
            if slope_error_new >= 0:
                y -= 1
                slope_error_new = slope_error_new - 2 * (x2 - x1)

        return positions

    def get_positions(self):
        """
        Function for returning the list of position between start and end for this object

        Returns:
            track_positions: list tuple (int, int), a list of the track positions passed through
        """
        return self.positions
