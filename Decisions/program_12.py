def checkPoint():
    print('The co-ordinates of center is (0,0)..')
    r=int(input('Enter the radius : '))
    x1=int(input('Enter first point : '))
    y1=int(input('Enter second point : '))
    if (x1**2 + y1**2)>r**2:
        print('The Point lies out of circle')
    elif(x1**2 + y1**2)<r**2:
        print('The Point lies inside of circle')
    else:
        print('Points lies on the circle')
        
checkPoint()
