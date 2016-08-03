import asyncio


def async_test(test_func):
    def wrapper(*args, **kwargs):
        def run():
            yield from test_func(*args, **kwargs)
        event_loop = asyncio.get_event_loop()
        event_loop.run_until_complete(run())
    return wrapper
