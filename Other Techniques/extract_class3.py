# by Kami Bigdely
# Extract class
WELL_DONE = 3000
MEDIUM = 2500
COOKED_CONSTANT = 0.05


class PreparedFood():
    """Class for determining food cooked state"""

    def __init__(self, time, temp, pressure, desired_state):
        """Initialize variables"""
        self.time = time
        self.temp = temp
        self.pressure = pressure
        self.desired_state = desired_state

    def is_cookeding_criteria_satisfied(self):
        """Check whether cooked to desired state"""
        return self.is_well_done() or self.is_medium()

    def is_well_done(self):
        """Check if cooked well done"""
        return (self.desired_state == 'well-done'
                and self.get_cooking_progress() >= WELL_DONE)

    def is_medium(self):
        """Check if cooked medium"""
        return (self.desired_state == 'medium'
                and self.get_cooking_progress() >= MEDIUM)

    def get_cooking_progress(self):
        """Return how cooked food is"""
        return self.time * self.temperature * self.pressure * COOKED_CONSTANT


time = 30  # [min]
temp = 103  # [celcius]
pressure = 20  # [psi]
desired_state = 'well-done'

food = PreparedFood(time, temp, pressure, desired_state)

if food.is_cookeding_criteria_satisfied():
    print('cooking is done.')
else:
    print('ongoing cooking.')
