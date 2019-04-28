
'''

PRIME NUMBER GENERATION - by Callum Alexander
Trial by Division Strategy

This program generates calculates all the prime numbers up to given end value, in this case 1,000,000 which
it completes in a few minutes. I found that this version takes a lot less time that AKS Primality Testing.

Uncomment the bottom to handle all the prime numbers to an external txt file.

'''


import datetime
from math import sqrt

val = 2
primeArray = [] # initializes an empty list of prime numebrs

print('Start Time - ' + str(datetime.datetime.now()))

end = 1000000 # upper bound in this case is one million

while val < end:

    if val%1000 == 0: # This condition prints the percentage completed to the command prompt
        print(str(round((val/end) * 100 , 3)) + '%') 
       
    
    
    div = int(sqrt(val)) # sets the highest divisor to the square root of the value
    found = True
    while div > 1:

        if val%div == 0: # if the value is composite, it breaks the loop
            found = False
            break
                  
        div -= 1
                  
    if found == True: # if the value is found not to be composite, then it is prime 
        primeArray.append(val) # the value is added to the list of primes
        

    val += 1
        
print(primeArray) # prints the list of primes once it is completed
print(str(datetime.datetime.now()))

'''
with open('primeHundredThousand.txt', 'w') as filehandle:  
    for listitem in primeArray:
        filehandle.write('%s\n' % listitem)
'''