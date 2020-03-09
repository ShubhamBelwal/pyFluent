def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count
        print(average)


if __name__ == '__main__':
    my = averager()
    next(my)
    my.send(10)
    my.send(30)
    my.send(5)
    my.close()
