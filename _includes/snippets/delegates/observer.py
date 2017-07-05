from delegate import Delegated


class Observer(Delegated):
    """An Observer callable object to observe values in a Delegate chain."""

    def __init__(self):
        super().__init__()

    def __call__(self, *things):
        """Observes given values and passes them along with no changes."""
        print('Observed value(s):', *things)
        self.delegate(*things)
