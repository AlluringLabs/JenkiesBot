""" Handles describing how all adapters should work at a low level."""

class Adapter:
    """ Base class for all things that are considered "adapters". """

    def set_context(self, ctx: dict):
        """ Sets an adapter's context."""
        self.context = ctx

    def get_context(self):
        """ Retrieves the adapter's context."""
        return self.context


class AdapterMethodNotImplementedError(NotImplementedError):
    """ Top level error that should be implemented by other adapter
    not-implemented errors."""

    def __init__(self, message: str="An adapter method was not implemented."):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message
