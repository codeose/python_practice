def multi_2():
    print('Numbers divisible by 2 include:')
    print (*range(0, 100, 2), sep=", ")
    #'*' is used to unpack the argument.
def multi_3():
    print('Numbers divisible by 3 include:')
    print (*range(0, 100, 3), sep=',')

multi_2()
multi_3()