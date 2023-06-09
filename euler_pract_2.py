#fubunacci seq

first_term = 0
second_terms = 1
following_term = 0
while following_term < 4000000: #4000000
    #fibunacci
    following_term = first_term+second_terms
    first_term = second_terms
    second_terms = following_term
    if following_term % 2 == 0:
        print(following_term)


