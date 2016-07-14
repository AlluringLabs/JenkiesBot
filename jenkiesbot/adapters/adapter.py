""" Describes how all adapters should work."""

class AdapterMethodNotImplementedError(NotImplementedError):
    """ Top level error that should be implemented by other adapter not-implemented errors."""

    def __init__(self, message: str="An adapter method was not implemented."):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message
