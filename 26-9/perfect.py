""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'""""'""""""""""""""""""""""""""""""""""
""     Author         :   Maneesha S                                                                    ""
""     Date           :   25 / 09 / 2017                                                                ""
""     Program        :   Determine if a number is perfect, abundant, or deficient                      ""
""                                                                                                      ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

input = input("Enter a number : ")
sum = 0
for i in range(1, input-1):
    if input % i == 0:
        sum = sum + i
if sum == input:
    print("Perfect\n")
elif sum > input:
    print("Abundant\n")
else:
    print("Deficient\n")
