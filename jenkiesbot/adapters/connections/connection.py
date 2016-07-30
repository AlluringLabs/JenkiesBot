from ..adapter import Adapter


class Connection(Adapter):
    """ 'Interface' that connections must implement."""

    def connect(self):
        """ Called when a bot is attempting to connect to a connection."""
        raise ConnectionMethodNotImplemented(
            "A connection must implement the connect method.")


class ConnectionMethodNotImplemented(NotImplementedError):
    """ This error is raised when a connection does not implement the
    methods described in the Connection class.
    """

    def __init__(self, message="A connection method was not implemented."):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message
