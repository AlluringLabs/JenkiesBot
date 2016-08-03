import asyncio

from ..adapter import Adapter


class Connection(Adapter):
    """ 'Interface' that connections must implement."""

    @asyncio.coroutine
    def connect(self):
        """ Called when the bot is attempting to connect to a connection."""
        raise ConnectionMethodNotImplemented(
            "A connection must implement the connect method.")

    @asyncio.coroutine
    def on_ready(self):
        """ Called when the bot has successfully connected to the connection's
        API."""
        raise ConnectionMethodNotImplemented(
            "A connection must implement the on_ready method.")

    @asyncio.coroutine
    def on_message(self):
        """ Called when the bot receives a message from the specified connection."""

        # Quick thoughts: Each connection will have to handle incoming messages on their
        # own. The reason being is that each service (slack, discord, etc.) has their own
        # way of structuring data. Each connection will have to implement the on_message
        # method, implement some form of parser/way to normalize the data incoming and then
        # pass that information to what I would call a "ConnectionSupervisor." This connection
        # supervisor would be passed to each connection via the Adapter class's context.
        #
        # From there the ConnectionSupervisor will figure out what the incoming message is
        # asking to do.
        raise ConnectionMethodNotImplemented(
            "A connection must implement the on_message method.")


class ConnectionMethodNotImplemented(NotImplementedError):
    """ This error is raised when a connection does not implement the
    methods described in the Connection class.
    """

    def __init__(self, message="A connection method was not implemented."):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message
