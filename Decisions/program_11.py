def liespoint():
    x1=int(input('Enter first point : '))
    y1=int(input('Enter second point : '))
    x2=int(input('Enter third point : '))
    y2=int(input('Enter fourth point : '))
    x3=int(input('Enter fifth point : '))
    y3=int(input('Enter sixsth point : '))
    if (y2-y1)/(x2-x1)==(y3-y2)/(x3-x2):
        print('The points Lies in Straight line')
        
    else:
        print('Points doesnt lies in straight line')
    
liespoint()