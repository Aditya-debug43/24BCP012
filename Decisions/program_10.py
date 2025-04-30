length=int(input('Enter the length of the Rectangle : '))
brath=int(input('Enter the Breath of the Rectangle : '))
def area():
    are=length*brath
    para=2*(length+brath)
    if are > para :
        print(are,'>',para)
        
    else:
        print(are,'<',para)
        
area()
area()
    
