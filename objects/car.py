from random import randint


class Car:
    def __init__(self, track):
        self.track = track

        self.start_position = self.track.get_start_position()
        self.position = self.start_position
        self.track_position = track.get_track_position(self.position)

        self.last_position = self.position
        self.last_track_position = track.get_track_position(self.last_position)

        self.time = 0
        self.speed = (0, 0)
        self.acceleration = (0, 0)
        self.acceleration_status = (True, True)

    def accelerate(self, acceleration):
        acceleration_x = self.check_acceleration_bounds(acceleration[0])
        acceleration_status_x = True

        if (acceleration_x * self.speed[0] >= 0) & acceleration_x != 0:
            if randint(0, 4) == 0:
                acceleration_x = 0
                acceleration_status_x = False

        acceleration_y = self.check_acceleration_bounds(acceleration[1])
        acceleration_status_y = True

        if (acceleration_y * self.speed[1] >= 0) & acceleration_y != 0:
            if randint(0, 4) == 0:
                acceleration_y = 0
                acceleration_status_y = False

        self.acceleration = (acceleration_x, acceleration_y)
        self.acceleration_status = (acceleration_status_x, acceleration_status_y)

        print(f'Acceleration: {self.acceleration}')
        print(f'Status: {self.acceleration_status}')

        self.update_speed()

    def check_acceleration_bounds(self, acceleration_value):
        if not self:
            raise NotImplementedError

        if acceleration_value >= 1:
            return 1
        elif acceleration_value <= -1:
            return -1
        else:
            return 0

    def update_speed(self):
        speed_x = self.speed[0]
        speed_x += self.acceleration[0]

        if speed_x > 5:
            speed_x = 5
        elif speed_x < -5:
            speed_x = -5

        speed_y = self.speed[1]
        speed_y += self.acceleration[1]

        if speed_y > 5:
            speed_y = 5
        elif speed_y < -5:
            speed_y = -5

        self.speed = (speed_x, speed_y)

        print(f'Speed: {self.speed}')
