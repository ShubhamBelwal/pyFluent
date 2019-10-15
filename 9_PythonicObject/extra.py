def countnumber(i):

    if i<0:
        temp = i*-1
    else:
        temp = i

    if i==0:
        print('0')
    else:
        for y in range(temp+1):
            if i<0:
                print(i+y)
            else:
                print(y)

countnumber(10)