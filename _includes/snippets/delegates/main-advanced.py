#!/usr/bin/python3
from modifiers import Multiplier, Exponentiator, Incrementer
from observer import Observer


class Doubler(Multiplier):
    """A class to double numbers"""

    def __init__(self):
        # Set the parent class's multiplier to 2
        super().__init__(2)

    def double(self, val):
        """A method to double the given value"""
        # Call the parent class's __call__() method
        self(val)


def main():
    incrementer = Incrementer(1)
    # Equivalent to Multiplier(2)
    doubler = Doubler()
    squarer = Exponentiator(2)

    observer = Observer()

    incrementer.subscribe(doubler.double)
    doubler.subscribe(squarer)
    squarer.subscribe(observer)

    for i in range(10):
        incrementer(i)

    incrementer.unsubscribe(doubler.double)
    doubler.unsubscribe(squarer)
    squarer.unsubscribe(observer)


if __name__ == '__main__':
    main()
