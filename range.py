def multi_2():
    print('Numbers divisible by 2 include:')
    print (*range(0, 100, 2), sep=", ")
def multi_3():
    print('Numbers divisible by 3 include:')
    print (*range(0, 100, 3), sep=',')

multi_2()
print("")
multi_3()
#comment