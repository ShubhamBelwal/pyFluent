class DemoException(Exception):
    """An exception type for the demo"""
    pass

def demo_finally():
    print("-> coroutine started")
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print("*** DemoException Handled! Continuing...")
            else:
                print("-> coroutine received: {!r}".format(x))
    finally:
        print("-> coroutine ending")    