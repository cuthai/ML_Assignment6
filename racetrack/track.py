from random import choice


class Track:
    def __init__(self, track_name='R'):
        self.track_name = track_name

        self.x = 0
        self.y = 0
        self.track_data = []
        self.read_data()

        self.track = None
        self.start_positions = None
        self.finish_positions = None
        self.create_track()

    def read_data(self):
        file_name = self.track_name + '-track.txt'
        file_location = f'data//{file_name}'

        file = open(file_location, 'r')

        data = file.readlines()

        meta_data = data[0].split('\n')[0].split(',')

        self.x = int(meta_data[0])
        self.y = int(meta_data[1])
        self.track_data = data[1:]

    def create_track(self):
        track = []
        start_positions = []
        finish_positions = []

        for x_index in range(self.x):
            track_row = list(self.track_data[x_index])[:-1]

            for y_index in range(self.y):
                if track_row[y_index] == 'S':
                    start_positions.append((x_index, y_index))
                elif track_row[y_index] == 'F':
                    finish_positions.append((x_index, y_index))

            if len(track_row) != self.y:
                raise ValueError(f'Track row {x_index} does not match size {self.y}')

            track.append(track_row)

        if len(track) != self.x:
            raise ValueError(f'Track does not match size {self.x}')

        self.track = track
        self.start_positions = start_positions
        self.finish_positions = finish_positions

    def get_track_position(self, pos):
        return self.track[pos[0]][pos[1]]

    def get_start_position(self):
        return choice(self.start_positions)
