from random import randint
from objects.bresenham import BresenhamPath


class Car:
    def __init__(self, track, reset_type='p'):
        self.track = track
        self.reset_type = reset_type

        self.start_position = self.track.get_start_position()
        self.position = self.start_position
        self.track_position = track.get_track_position(self.position)

        self.last_position = self.position
        self.last_track_position = track.get_track_position(self.last_position)

        self.time = 0
        self.velocity = (0, 0)
        self.acceleration = (0, 0)
        self.acceleration_status = (True, True)

    def accelerate(self, acceleration):
        acceleration_x = self.check_acceleration_bounds(acceleration[0])
        acceleration_status_x = True

        if (acceleration_x * self.velocity[0] >= 0) & acceleration_x != 0:
            if randint(0, 4) == 0:
                acceleration_x = 0
                acceleration_status_x = False

        acceleration_y = self.check_acceleration_bounds(acceleration[1])
        acceleration_status_y = True

        if (acceleration_y * self.velocity[1] >= 0) & acceleration_y != 0:
            if randint(0, 4) == 0:
                acceleration_y = 0
                acceleration_status_y = False

        self.acceleration = (acceleration_x, acceleration_y)
        self.acceleration_status = (acceleration_status_x, acceleration_status_y)

        print('-------------')
        print(f'Acceleration: {self.acceleration}')
        print(f'Status: {self.acceleration_status}')

        self.update_velocity()

    def check_acceleration_bounds(self, acceleration_value):
        if not self:
            raise NotImplementedError

        if acceleration_value >= 1:
            return 1
        elif acceleration_value <= -1:
            return -1
        else:
            return 0

    def update_velocity(self):
        velocity_x = self.velocity[0]
        velocity_x += self.acceleration[0]

        if velocity_x > 5:
            velocity_x = 5
        elif velocity_x < -5:
            velocity_x = -5

        velocity_y = self.velocity[1]
        velocity_y += self.acceleration[1]

        if velocity_y > 5:
            velocity_y = 5
        elif velocity_y < -5:
            velocity_y = -5

        self.velocity = (velocity_x, velocity_y)

        print(f'Velocity: {self.velocity}')

        self.update_position()

    def update_position(self):
        self.last_position = self.position
        self.last_track_position = self.track_position

        position_x = self.position[0]
        position_x += self.velocity[0]

        position_y = self.position[1]
        position_y += self.velocity[1]

        new_position = (position_x, position_y)
        new_track_position = self.track.get_track_position(new_position)

        flag_crashed, flag_finished = self.check_movement(new_position)
        print(f'Crashed: {flag_crashed}, Finished: {flag_finished}')

        self.time += 1
        if flag_finished:
            return True
        elif flag_crashed:
            self.reset()
        else:
            self.move(new_position, new_track_position)

        print(f'Position: {self.position}')
        print(f'Track: {self.track_position}')

    def check_movement(self, new_position):
        flag_crashed = False
        flag_finished = False

        track_types = []

        bresenham_path = BresenhamPath(self.last_position, new_position)

        for position in bresenham_path.get_positions():
            track_types.append(self.track.get_track_position(position))
        print(f'Track Types: {track_types}')

        for track_type in track_types:
            if track_type == '#':
                flag_crashed = True

                return flag_crashed, flag_finished

            elif track_type == 'F':
                flag_finished = True

                return flag_crashed, flag_finished

        return flag_crashed, flag_finished

    def reset(self):
        if self.reset_type == 's':
            self.velocity = (0, 0)
            self.position = self.start_position
        else:
            self.velocity = (0, 0)

    def move(self, new_position, new_track_position):
        self.position = new_position
        self.track_position = new_track_position
