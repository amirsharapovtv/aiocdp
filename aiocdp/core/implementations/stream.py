import asyncio
from dataclasses import dataclass, field
from typing import TypeVar, AsyncGenerator, TYPE_CHECKING

from aiocdp.core.interfaces.connection import IConnection
from aiocdp.core.interfaces.stream import IEventStream

if TYPE_CHECKING:
    from aiocdp import Connection

_T = TypeVar('_T')


def _create_future():
    """
    Utility function to create a new future.
    """
    return asyncio.get_event_loop().create_future()


@dataclass(eq=False)
class EventStream(IEventStream):
    """
    Represents an asynchronous stream of CDP events received from the connection.
    """

    """
    The connection
    """
    connection: 'Connection'

    """
    The list of event names to listen to
    """
    events_to_listen: list[str]

    """
    The list of recorded events
    """
    events: list[_T] = field(
        default_factory=list,
        init=False
    )

    """
    Instance of the reader for this class
    """
    reader: 'EventStreamReader | None' = field(
        default=None,
        init=False
    )

    """
    An async future resolved everytime an event is recorded
    """
    next: asyncio.Future = field(
        default_factory=_create_future,
        init=False
    )

    @property
    def is_closed(self):
        """
        Public readonly access to the closed status of the stream.
        """
        return self.connection.is_stream_closed(self)

    def __enter__(self):
        """
        Allows this object to be used as a context manager.
        """
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Closes this stream when used as a context manager.
        """
        self.close()

        if exc_type is not None:
            return False

    def close(self):
        """
        Unsubscribes this stream from receiving events from the connection.
        """
        self.connection.close_stream(self)

    def get_connection(self) -> 'IConnection':
        """
        Returns the connection this event stream is associated to.
        """
        return self.connection

    def get_events_to_listen(self):
        """
        Returns the list of events this stream is subscribed to
        """
        return self.events_to_listen

    def get_reader(self):
        """
        Creates the reader for this stream.

        Notes:
            - This method returns the same instance for the lifetime of this stream.
        """

        if self.reader is None:
            self.reader = EventStreamReader(self)

        return self.reader

    async def iterate(self) -> AsyncGenerator[_T, None]:
        """
        Iterates over all the events in this stream and asynchronously yields new events as they are received.

        Notes:
            - Should not be used by public API. First call `EventStream.get_reader`
              and then use `EventStreamReader.iterate` instead.
        """
        for item in self.events:
            yield item

        while True:
            yield await self.next

    def write(self, item: _T):
        """
        Writes an item to the stream. Responsible for resolving futures.
        """
        self.events.append(item)
        self.next.set_result(item)
        self.next = _create_future()


@dataclass
class EventStreamReader:
    """
    Object that has read only access to an event stream.
    """
    stream: EventStream

    @property
    def events_to_listen(self) -> list[str]:
        """
        Public readonly access to the CDP events to listen for. Provided by the stream.
        """
        return self.stream.events_to_listen

    @property
    def connection(self):
        """
        Public readonly access to the `Connection` instance. Provided by the stream.
        """
        return self.stream.connection

    @property
    def is_closed(self):
        """
        Public readonly access to the closed status of the stream. Provided by the stream.
        """
        return self.stream.is_closed

    def __enter__(self):
        """
        Allows this object to be used as a context manager.
        """
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Closes this stream when used as a context manager.
        """
        self.close()

        if exc_type is not None:
            return False

    def close(self):
        """
        Closes this stream.
        """
        self.stream.close()

    async def iterate(self) -> AsyncGenerator[_T, None]:
        """
        Iterates over the events asynchronously in this stream.
        """
        async for item in self.stream.iterate():
            yield item