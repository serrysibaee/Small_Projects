#هHere we import some libraries to use thier commands like pi and tan 
from math import atan as ta
from math import pi as pi 

#
#we have put some constants like M , Y and x is for the while loop under 
M = 7.0
Y1 = 1.39
x =1

#print((1+((Y1-1)/2)*(M**2))**(Y1/(Y1-1)))
#every Value under is an equation from the book 
Value = (1+((Y1-1)/2)*(M**2))**(Y1/(Y1-1))
real = 1/Value
value2 = (1+((Y1-1)/2)*(M**2))
value3 = ((1/M)*((1+((Y1-1)/2)*(M**2))/((Y1+1)/2))**(Y1+1)/(2*(Y1-1)))
value4 = ((((Y1+1)/(Y1-1))**(1/2))*ta(((Y1-1)/(Y1+1))*((M**2)-1)))**(1/2)-ta(((M**2)-1)**(1/2))
print("start")
# i have used while loop to make any number of unswers for the equations 
while x < 7 :
    #Value = (1+((Y1-1)/2)*(M**2))**(Y1/(Y1-1))
    #real1 = 1/Value
    #value2 = (1+((Y1-1)/2)*M**2)
    #value3 = ((1/M)*((1+((Y1-1)/2)*(M**2))/((Y1+1)/2))**(Y1+1)/(2*(Y1-1)))
    #real2 = value3
    value4 = ((Y1+1)/(Y1-1))**(1/2)
    value5 = ((((Y1-1)/(Y1+1))*((M**2)-1))**(1/2))*(180/pi)
    tavalue = ta(value5)
    value6 = (((M**2)-1)**(1/2))*(180/pi)
    tavalue2 = ta(value6)
    all = value4*tavalue-tavalue2
    #multi = real1 * real2
    real3 = value4*(180/pi)
    print (",",all,",")
    M = M+0.5 # that is like the book for the add 
    x = x + 1 # this for making the while loop have un condition to complete and stop 


