# first = input('Enter first number: ')
# second = input('Enter second number: ')

# _sum = float(first)+float(second)

# print('Sum = '+str(_sum))

#check how  many multiples of 3 in 1000
_sum_3 = 0

index = 1000
while index > 0:
    num1 = index % 3
    num2 = index % 5
    if num1 == 0 or num2 == 0:
        print(index)
        _sum_3 = _sum_3 + index
    index = index -1
print(f"Try to fix {_sum_3}")


def multiples():
    _sum = 0
    for i in range(1000):
        if i%3 == 0 or i%5 == 0:

            _sum += i
            
    print(_sum) 
#check how  many multiples of 5 in 1000

multiples()
#display multiples of 3 in 1000