from collections import namedtuple

Result = namedtuple('Result', 'count average')

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total = total + term
        count += 1
        average = total/count
    return Result(count, average)

if __name__ == '__main__':
    from inspect import getgeneratorstate
    coro_avg = averager()
    print("=> ", getgeneratorstate(coro_avg))
    next(coro_avg)
    print("=> ", getgeneratorstate(coro_avg))
    coro_avg.send(10)
    print("=> ", getgeneratorstate(coro_avg))
    coro_avg.send(30)
    coro_avg.send(6.5)
    coro_avg.send(None)
    print("=> ", getgeneratorstate(coro_avg))