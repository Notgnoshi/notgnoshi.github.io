#!/usr/bin/python3
from delegate import Delegated
from modifiers import Exponentiator, Incrementer
from observer import Observer


class Doubler(Delegated):
    """A delegated class to double numbers"""

    def __init__(self):
        super().__init__()

    def double(self, val):
        """A method to double the given value"""
        self.delegate(2 * val)


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
        # Call the first modifier in the chain, and let the delegates handle the rest
        incrementer(i)

    incrementer.unsubscribe(doubler.double)
    doubler.unsubscribe(squarer)
    squarer.unsubscribe(observer)


if __name__ == '__main__':
    main()
