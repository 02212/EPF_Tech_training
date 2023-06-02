def findLagestPrime(number):
    index = 2
    while index * index < number:
        if number % index:
            index =  index +1
        else:
            number = number / index
    return number

#find largest prime  number of any prime number 
print(int(findLagestPrime(600851475143)))