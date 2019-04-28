# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 14:01:59 2019

@author: Callum
"""

'''

PRIME NUMBER GENERATION - by Callum Alexander

Ok, so this program does generate all the prime numbers below a certain value using AKS Primality
Testing, by I edited it a bit so that it would try and generate the smallest prime number that is
the product of all the previous prime numbers. It then occured to me that that number would not be a prime
number if it was the product of other numbers apart from itself and zero lol

p.s. this is very nasty code, if you can't understand it, I apologize.

'''





array = []

def MainLoop(limit, array):
    
    n=4
    primeMultiple = 3
    multipleBool = False
    while multipleBool == False:
        
        output = False
        output = aksPrimalityTest(n)
        if output == True:
            
            #print(' ' + str(n) + ' - Prime')
            array.append(n)
            primeMultiple = primeMultiple * n
            #print(str(primeMultiple))
            multipleBool = aksPrimalityTest(primeMultiple)
            if multipleBool == True:
                print('The prime multiple is also prime!!!!!!')
            else:
                print('The prime multiple is NOT prime :(')
            
        else:
            #print(' ' + str(n) + ' - Composite')
        
        n+=1

    lenCalc = str(primeMultiple)
    lenCalc = len(lenCalc)
    print(str(lenCalc))

    with open('TheMegaPrimeNumber.txt', 'w') as filehandle:  
        filehandle.write('%s\n' % primeMultiple)


def aksPrimalityTest(n):
    if n==2:
        return True
    c=1
    for i in range(n//2+1):
        c=c*(n-i)//(i+1)
        if c%n:
            return False
    return True



limit = int(input('Enter the limit that you would like to go up to    '))
MainLoop(limit, array)
