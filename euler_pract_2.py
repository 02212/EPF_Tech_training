#fibunacci seq

first_term = 0
second_terms = 1
following_term = 0
_sum = 0
while following_term < 4000000: #4000000
    #fibunacci sequesnce init 
    following_term = first_term+second_terms
    first_term = second_terms
    second_terms = following_term

    #finding all the even fibunacci terms 
    if following_term % 2 == 0: 
        _sum += following_term
        
# print the sum of all the term
print(f"\nsum of all even = {_sum}")


