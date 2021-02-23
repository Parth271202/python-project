print("check your result here")
ch=input('Enter your name:')
ch=input('Enter your roll no.: ')
x=int(input('mathematics marks:'))
y=int(input('physics marks:'))
z=int(input('chemistry marks:'))
c=int(input('english marks:'))

sum=x+y+z+c
print('sum= ',sum)

if sum<=400 and sum>=360: print("congratulations you passed with A grade")
elif sum<=360 and sum>=320: print("congratulations you passed with B grade")
elif sum<=320 and sum>=280: print("congratulations you passed with C grade")
elif sum<=280 and sum>=240: print("congratulations you passed with D grade")
elif sum<=240 and sum>=200: print("congratulations you passed with E grade")
else:
    print("sorry you failed better luck next time")
