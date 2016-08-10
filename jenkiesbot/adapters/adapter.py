""" Handles describing how all adapters should work at a low level."""

class Adapter:
    """ Base class for all things that are considered "adapters". """

    def set_context(self, ctx: dict):
        """ Sets an adapter's context."""
        self.context = ctx
        return self

    def get_context(self):
        """ Retrieves the adapter's context."""
        return self.context

