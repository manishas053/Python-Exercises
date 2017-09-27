""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'""""'""""
""     Author         :   Maneesha S                                      ""
""     Date           :   25 / 09 / 2017                                  ""
""     Program        :   Given a number n, find the nth prime            ""
""                                                                        ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

input = input("Enter a number :")
num_count = 0
for i in range(2, 100):
    count = 0
    for j in range(2, i):
        if i % j == 0:
            count += 1
    if count == 0:
        num_count += 1
        if num_count == input:
            print i
