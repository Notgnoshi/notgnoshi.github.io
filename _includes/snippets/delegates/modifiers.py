from delegate import Delegated


class Multiplier(Delegated):
    """A Multiplier modifier to multiply numbers"""

    def __init__(self, multiplier=2):
        """Construct a Multiplier object with an optional multiplier. Defaults to 2."""
        super().__init__()
        self.multiplier = multiplier

    def __call__(self, num):
        """Multiplies a given number by a predetermined multiplier"""
        self.delegate(num * self.multiplier)


class Incrementer(Delegated):
    """An Incrementer modifier to increment numbers"""

    def __init__(self, increment_value=1):
        """Construct an Incrementer object with an optional increment value. Defaults to 1."""
        super().__init__()
        self.increment_value = increment_value

    def __call__(self, num):
        """Increment num by a predetermined value"""
        self.delegate(num + self.increment_value)


class Exponentiator(Delegated):
    """An Exponentiator modifier to exponentiate numbers"""

    def __init__(self, power=2):
        """Construct an Exponentiator object with an optional power. Defaults to 2."""
        super().__init__()
        self.power = power

    def __call__(self, num):
        """Exponentiates a given number by a predetermine value"""
        self.delegate(num ** self.power)
