my_list = [42,69,322,13,0,99,-5,9,8,7,-6,5]
while 1 > 0:
    my_list =int(input('введите число'))
    if my_list %2==0:
        print('положительное число')
    else:
        print('отрицательное число')
        print('конец')
        break