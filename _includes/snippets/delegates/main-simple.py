#!/usr/bin/python3
from modifiers import Multiplier, Exponentiator, Incrementer
from observer import Observer


def main():
    # Modifiers that act on numbers.
    incrementer = Incrementer(1)
    doubler = Multiplier(2)
    squarer = Exponentiator(2)

    # An observer to view intermediate and/or final values in the delegate chain.
    observer = Observer()

    # Subscribe the doubler modifier to the output of the incrementer.
    incrementer.subscribe(doubler)
    # Subscribe the squarer modifier to the output of the doubler.
    doubler.subscribe(squarer)
    # Subscribe the observer to the output of the squarer.
    squarer.subscribe(observer)

    for i in range(10):
        # Call the first modifier in the chain, and let the delegates handle the rest
        incrementer(i)

    # Unsubscribe functors.
    incrementer.unsubscribe(doubler)
    doubler.unsubscribe(squarer)
    squarer.unsubscribe(observer)


if __name__ == '__main__':
    main()
