def findLagestPrime(number):
    index = 2
    while index * index < number:
        if number % index: #check if true or false, if its true it will incement the diviser 
            index =  index +1 # it sums the divisers together
        else:
            number = number / index # decreases the value of the sentinel so that it will not be an infinite loop
    return number

#find largest prime  number of any prime number 
print(int(findLagestPrime(600851475143)))



def findHPF(number):
    
    for i in range(2,number):
        if number % i:
            i = i + 1
        else:
            number = number / i
    return number

print(f"Answer for for-loop {findHPF(600851475143)}")

