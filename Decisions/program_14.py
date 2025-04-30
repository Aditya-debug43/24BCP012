
math=int(input('Enter the score of maths : '))
phy=int(input('Enter the score of physics : '))
com=int(input('Enter the score of computer : '))
total=math+phy+com
avg=total/3
print('Total marks : ',total)
print('Avareg marks is : ',avg)
def maths():
    if math<=39 :
        print('Sorry, You are Failed in maths !!')
    elif 40<=math<=44:
        print('You have P Grade in maths')
    elif 45<=math<=49:
        print('You have C Grade in maths')
    elif 50<=math<=54:
        print('You have B Grade in maths')
    elif 55<=math<=59:
        print('You have B+ Grade in maths')
    elif 60<=math<=69:
        print('You have A Grade in maths')
    elif 70<=math<79:
        print('You have A+ Grade in maths')
    elif 80<=math<=100:
        print('You have O Grade in maths')
        
def physics():
    
    if phy<=39:
        
        print('Sorry, You are Failed in physics !!')
    elif 40<=phy<=44:
        print('You have P Grade in physics')
    elif 45<=phy<=49:
        print('You have C Grade in physics')
    elif 50<=phy<=54:
        print('You have B Grade in physics')
    elif 55<=phy<=59:
        print('You have B+ Grade in physics')
    elif 60<=phy<=69:
        print('You have A Grade in physics')
    elif 70<=phy<79:
        print('You have A+ Grade in physics')
    elif 80<=phy<=100:
        print('You have O Grade in physics')
        
def computer():
    
    if com<=39:
        print('Sorry, You are Failed in computer !!')
    elif 40<=com<=44:
        print('You have P Grade in computer')
    elif 45<=com<=49:
        print('You have C Grade in computer')
    elif 50<=com<=54:
        print('You have B Grade in computer')
    elif 55<=com<=59:
        print('You have B+ Grade in computer')
    elif 60<=com<=69:
        print('You have A Grade in computer')
    elif 70<=com<79:
        print('You have A+ Grade in computer')
    elif 80<=com<=100:
        print('You have O Grade in computer')
        
maths()
physics()
computer()
