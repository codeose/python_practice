def newton_2nd_law():
    print('Finding the value for newton Second law of motion using formula')
    print('S = u*t - 1/2*g*t^2')
    t = float(input('Enter the value of t: '))
    u = float(input('Enter the value of u: '))
    g = float(input('Enter the value of g: '))

    s = (u * t)-((1/2)*g*(t**2))

    print('The Value of S is', s)

newton_2nd_law()