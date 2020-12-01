from random import randint
from objects.bresenham import BresenhamPath


class Car:
    """
    Class car that drives along the track. Takes inputs through the accelerate function. After acceleration, velocity
        and new position are calculated. This object also handles communication between the Bresenham's line algorithm
        and the track
    """
    def __init__(self, track, reset_type='S'):
        """
        Init function, takes a track and a reset_type. Retrieves a start position from the track and then awaits
            acceleration commands. Car starts at the start position.

        Args:
            track: track, track object with a track read in from data
            reset_type: char, defines the rest type. Default is 'S', which stops the car, sets velocity to (0, 0), and
                increments time by 1. Use 'R' to have a hard rest to the start position
        """
        # Track
        self.track = track

        # Car meta variables - reset type
        if reset_type not in ['S', 'R']:
            raise ValueError("Car Reset type not found, Please specify 'S' or 'R'")
        else:
            self.reset_type = reset_type

        # Car meta variables - flag finished
        self.flag_finished = False

        # Position variables for start and current. Resets to start if reset is 'R'
        self.start_position = self.track.get_start_position()
        self.position = self.start_position
        self.track_position = track.get_track_position(self.position)

        # Previous position variables, used if reset is 'S'
        self.last_position = self.position
        self.last_track_position = track.get_track_position(self.last_position)

        # Movement variables & acceleration status
        self.time = 0
        self.velocity = (0, 0)
        self.acceleration = (0, 0)
        self.acceleration_status = (True, True)

    def accelerate(self, acceleration):
        """
        Accelerate function. Main function for driving the car

        Pass a tuple where x is the 0 index and y is the 1 index. This function rolls a 20% chance of acceleration
            failure for either x or y. Failure can only occur if the car is already moving in that direction or stopped.
            If the acceleration is the opposite direction of the current velocity (as in braking), then there is no
            chance of failure. This function also calls to check_acceleration_bounds and converts the acceleration to:
            {-1, 0, 1}. And input not in that bound is converted to match. After the conversion and failure check,
            velocity is updated.

        Args:
            acceleration: tuple (int, int), 0 index is acceleration for x and 1 index is acceleration for y
        """
        # x acceleration
        # Check bounds and convert if needed
        acceleration_x = self.check_acceleration_bounds(acceleration[0])

        # Set initial status to true
        acceleration_status_x = True

        # Check to make sure this isn't a break command (sign of velocity differs from the sign of acceleration = break)
        if (acceleration_x * self.velocity[0] >= 0) & acceleration_x != 0:
            # Roll an int between 0 and 4, 0 is a failure (20%)
            if randint(0, 4) == 0:
                # If failed, update status and set acceleration to 0
                acceleration_x = 0
                acceleration_status_x = False

        # y acceleration
        # Check bounds and convert if needed
        acceleration_y = self.check_acceleration_bounds(acceleration[1])

        # Set initial status to true
        acceleration_status_y = True

        # Check to make sure this isn't a break command (sign of velocity differs from the sign of acceleration = break)
        if (acceleration_y * self.velocity[1] >= 0) & acceleration_y != 0:
            # Roll an int between 0 and 4, 0 is a failure (20%)
            if randint(0, 4) == 0:
                # If failed, update status and set acceleration to 0
                acceleration_y = 0
                acceleration_status_y = False

        # Save acceleration results and the status
        self.acceleration = (acceleration_x, acceleration_y)
        self.acceleration_status = (acceleration_status_x, acceleration_status_y)

        print('-------------')
        print(f'Acceleration: {self.acceleration}')
        print(f'Status: {self.acceleration_status}')

        # Update velocity
        self.update_velocity()

    def check_acceleration_bounds(self, acceleration_value):
        """
        This function ensures that the input to acceleration match the desired range. Any positive numbers are converted
            to 1. Any negative to -1.

        Args:
            acceleration_value: int, acceleration value passed to accelerate function

        Returns:
            acceleration_value: int, bounded acceleration
        """
        if not self:
            raise NotImplementedError

        # Positive values
        if acceleration_value >= 1:
            return 1

        # Negative values
        elif acceleration_value <= -1:
            return -1

        # Anything in between set to 0
        else:
            return 0

    def update_velocity(self):
        """
        Function to update velocity based on saved acceleration results

        Uses the results after acceleration has been determined. Should only be called with the accelerate function.
            After velocity is updated, update_position is called.
        """
        # X velocity
        # Add acceleration to our temp variable
        velocity_x = self.velocity[0]
        velocity_x += self.acceleration[0]

        # Velocity can only be 5, so bound the variable if needed. Any acceleration beyond is ignored
        if velocity_x > 5:
            velocity_x = 5
        elif velocity_x < -5:
            velocity_x = -5

        # Y velocity
        # Add acceleration to our temp variable
        velocity_y = self.velocity[1]
        velocity_y += self.acceleration[1]

        # Velocity can only be 5, so bound the variable if needed. Any acceleration beyond is ignored
        if velocity_y > 5:
            velocity_y = 5
        elif velocity_y < -5:
            velocity_y = -5

        # Save the results
        self.velocity = (velocity_x, velocity_y)

        print(f'Velocity: {self.velocity}')

        # Call to update_position
        self.update_position()

    def update_position(self):
        """
        Update position function to handle car movement on track

        This function takes the results of the velocity to update movement. The path is then calculated by creating
            a BresenhamPath object. The path is checked for any collisions before movement occurs. If any collisions
            occurs, the car is stopped and reset based on the reset type.

        Returns:
            flag_finished: Boolean, if the finish line has passed
        """
        # Take current position and save as last
        self.last_position = self.position
        self.last_track_position = self.track_position

        # Update our temporary x position variable
        position_x = self.position[0]
        position_x += self.velocity[0]

        # Update our temporary y position variable
        position_y = self.position[1]
        position_y += self.velocity[1]

        # Temporarily save our new position variables
        new_position = (position_x, position_y)
        new_track_position = self.track.get_track_position(new_position)

        # Pass the temporary new position to check movement. This function calls to the Bresenham's line algorithm
        # Retrieve flags based on crash and finish status
        flag_crashed, flag_finished = self.check_movement(new_position)
        self.flag_finished = flag_finished
        print(f'Crashed: {flag_crashed}, Finished: {flag_finished}')

        # Increment time
        self.time += 1
        print(f'Time: {self.time}')

        # If finished, return True
        if flag_finished:
            print('DONE')
            return True

        # If crashed, trigger the reset function
        elif flag_crashed:
            print('RESET')
            self.reset()

        # Otherwise, move the car
        else:
            self.move(new_position, new_track_position)

        print(f'Position: {self.position}')
        print(f'Track: {self.track_position}')

    def check_movement(self, new_position):
        """
        Function to check movement of the car before moving the car

        This takes a new position and checks against the old position. The two positions are used to create a
            BresenhamPath object. This object is used to retrieve the positions traveled. These positions are then
            passed to the track to retrieve the track status at those positions. Crash status and finished status are
            then checked and returned to the update_position function for movement.

        Args:
            new_position: tuple (int, int). New position the car is attempting to move to

        Returns:
            flag_crashed: Boolean, flag if a crash has occured
            flag_finished: Boolean, flag if the finish line has been reached
        """
        # Initial flag status
        flag_crashed = False
        flag_finished = False

        # Variable for storing the track types passed over
        track_types = []

        # Grab the positions between new and last by creating a BresenhamPath object.
        positions = BresenhamPath(self.last_position, new_position).get_positions()

        # Call to the track to retrieve the track status of those positions
        print(f'Positions: {positions}')
        for position in positions:
            # Retrieve the track type for each position
            track_type = self.track.get_track_position(position)

            # Flag for crash
            if track_type == '#':
                flag_crashed = True

            # Flag for finish
            elif track_type == 'F':
                flag_finished = True

            # Save the track type, for debugging
            track_types.append(track_type)

        print(f'Track Types: {track_types}')

        return flag_crashed, flag_finished

    def reset(self):
        """
        Reset function

        Depending on the reset_type for this car, this function will zero out velocity and then either leave car or
            move it back to the start
        """
        # Stop the car by setting velocity to 0
        self.velocity = (0, 0)

        # If reset, move back to start_position
        if self.reset_type == 'R':
            self.position = self.start_position

    def move(self, new_position, new_track_position):
        """
        Move function

        This function sets the cars current position to the new position

        Args:
            new_position: tuple (int, int), position to move car to
            new_track_position: char, track type at this position, retrieved from the track
        """
        self.position = new_position
        self.track_position = new_track_position

    def get_position(self):
        """
        This function returns the car's current position

        Returns:
            position: tuple (int, int), car's current position on the track
        """
        return self.position

    def get_velocity(self):
        """
        This function returns the car's current velocity

        Returns:
            position: tuple (int, int), car's current velocity
        """
        return self.velocity

    def get_finish(self):
        """
        This function returns the car's finish status

        Returns:
            flag_finished: Boolean, car's current finished status
        """
        return self.flag_finished

    def get_time(self):
        """
        This function returns the car's current time, for the cost function

        Returns:
           time: int, time the car has been driving
        """
        return self.time
