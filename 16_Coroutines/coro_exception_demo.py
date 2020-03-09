class DemoException(Exception):
    """An Exception Type for the demonstration"""


def demo_exec_handling():
    print("-> coroutine started")
    while True:
        try:
            x = yield
        except DemoException:
            print("*** DemoException handled. Continuing...")
        else:
            print("-> coroutine received: {!s}".format(x))
    # noinspection PyUnreachableCode
    raise RuntimeError("This line should never run.")


if __name__ == "__main__":
    exc_coro = demo_exec_handling()
    from inspect import getgeneratorstate

    print("=> ", getgeneratorstate(exc_coro))
    next(exc_coro)
    print("=> ", getgeneratorstate(exc_coro))
    exc_coro.send(11)
    print("=> ", getgeneratorstate(exc_coro))
    exc_coro.send(22)
    print("=> ", getgeneratorstate(exc_coro))
    exc_coro.throw(ZeroDivisionError)
    print("=> ", getgeneratorstate(exc_coro))
    # exc_coro.close()
    # print("=> ", getgeneratorstate(exc_coro))
