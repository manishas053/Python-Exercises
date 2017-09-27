""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'""""'"""""""""
""     Author         :   Maneesha S                                           ""
""     Date           :   25 / 09 / 2017                                       ""
""     Program        :   Compute the prime factors of a given natural number  ""
""                                                                             ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

input = input("Enter a number : ")
print("Prime factors are :")
for i in range(2, input-1):
    if input % i == 0:
        count = 0
        for j in range(2, i-1):
            if i % j == 0:
                count += 1
        if count == 0:
            print i
