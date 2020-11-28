from random import choice


class Track:
    """
    Class track to keep track of the environment of the objects

    This class implements a board and has the ability to return the type of position given a tuple
    """
    def __init__(self, track_name='R'):
        """
        Creates a track, pass a char to pick one of the tracks located in the data folder.

        Args:
            track_name: char, letter of track to use. Please use: 'R', 'O', 'L'. Defaults to 'R'
        """
        # Set track name
        self.track_name = track_name

        # Meta data and read data
        self.x = 0
        self.y = 0
        self.track_data = []
        self.read_data()

        # Update and create track
        self.track = None
        self.start_positions = None
        self.finish_positions = None
        self.create_track()

    def read_data(self):
        """
        This function reads data from the specified track name and sets the track size and saves the data read
        """
        # Create file name and location
        file_name = self.track_name + '-track.txt'
        file_location = f'data//{file_name}'

        # Attempt to read file, raise error if wrong track name specified
        try:
            file = open(file_location, 'r')
        except FileNotFoundError:
            raise FileNotFoundError("Track not found. Please specify 'R', 'O', or 'L' for the track name")

        # Save data as a list. Each item in list is a single line. The first list item is the track size
        data = file.readlines()

        # Close the file
        file.close()

        # Split the first item for the track size
        meta_data = data[0].split('\n')[0].split(',')

        # Save track size as X = rows and Y = columns
        self.x = int(meta_data[0])
        self.y = int(meta_data[1])

        # Save the rest of the data as the track data
        self.track_data = data[1:]

    def create_track(self):
        """
        This functions handles parsing the main data and reading that into a matrix for accessing using a tuple
        """
        # Empty variables for holding the track, start positions, and finish positions
        track = []
        start_positions = []
        finish_positions = []

        # Loop through the rows of the matrix and read each lines
        for x_index in range(self.x):

            # Grab the current row, drop last character as that is the new line character and convert string to a list
            track_row = list(self.track_data[x_index])[:-1]

            # Loop through the columns of the matrix
            for y_index in range(self.y):
                # If this is a start position, save current (x_index, y_index)
                if track_row[y_index] == 'S':
                    start_positions.append((x_index, y_index))

                # If this is a finish position, save current (x_index, y_index)
                elif track_row[y_index] == 'F':
                    finish_positions.append((x_index, y_index))

            # If we have too many columns, raise an error as there was a problem with parsing
            if len(track_row) != self.y:
                raise ValueError(f'Track row {x_index} does not match size {self.y}')

            # Append the list to the track
            track.append(track_row)

        # After appending all of the lists, check size of x, raise an error if there's a mismatch
        if len(track) != self.x:
            raise ValueError(f'Track does not match size {self.x}')

        # Save our variables
        self.track = track
        self.start_positions = start_positions
        self.finish_positions = finish_positions

    def get_track_position(self, position):
        """
        This function returns the track position of a specified tuple

        Args:
            position: tuple (int, int), the first int is for X/Rows, the second for Y/Columns on a matrix

        Returns:
            string: string, the character at that position
        """
        return self.track[position[0]][position[1]]

    def get_start_position(self):
        """
        This function returns a random start position for the track. There are multiple start positions so we return one
            randomly

        Returns:
            tuple: tuple (int, int), randomly picked tuple location of a start position
        """
        return choice(self.start_positions)
