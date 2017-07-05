class Delegate(object):
    """A class to implement delegates"""

    def __init__(self):
        self.functors = list()

    def __iadd__(self, functor):
        """Overload += to subscribe a given functor to this delegate."""
        # Verify that functor is callable. If not, don't subscribe.
        if callable(functor):
            self.functors.append(functor)
        return self

    def __isub__(self, functor):
        """Overload -= to unsubscribe a given functor to this delegate."""
        try:
            self.functors.remove(functor)
        # Functor wasn't subscribed.
        except ValueError:
            pass
        return self

    def __call__(self, *args):
        """Call each of the subscribed functors with the given values"""
        for functor in self.functors:
            functor(*args)


class Delegated(object):
    """A base class for delegated classes"""

    def __init__(self):
        self.delegate = Delegate()

    def subscribe(self, functor):
        """Subscribes the given functor to the output of self"""
        self.delegate += functor

    def unsubscribe(self, functor):
        """Unsubscribes the given functor from the output of self"""
        self.delegate -= functor
