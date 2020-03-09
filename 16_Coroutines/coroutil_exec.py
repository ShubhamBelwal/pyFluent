from coroutil import coroutine


@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total = total + term
        count += 1
        average = total / count
        print(average)


if __name__ == '__main__':
    coro_avg = averager
    from inspect import getgeneratorstate

    print(getgeneratorstate(coro_avg))
    coro_avg.send(10)
    coro_avg.send(30)
    coro_avg.send(5)
