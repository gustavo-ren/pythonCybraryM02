'''
Created on 19 de jan de 2017

@author: Gustavo
'''
#from pip._vendor.distlib.compat import raw_input

def isEven(num1):
    if (num1%2==0):
        return "Even"
    else:
        return "Odd"
 
def SumCal(valueOne, valueTwo):
    return valueOne+valueTwo

def evenList(numberList):
    countEven=0
    countOdd=0
    
    for number in numberList:
        if(number%2==0):
            countEven+=1
            
        else:
            countOdd+=1
            
    return countEven

def backwardString(inputString):
    return inputString[::-1]


def main():
    print("%s" %(isEven(6)))
    print("%d" %(SumCal(5, 8)))
    print("%d" %(evenList({1,2,3,4,5,6,7,8,9})))
    print("%s" %(backwardString("inputString")))
main()
