
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'""""'""""""""""""""""""""""""""""""""""
""     Author         :   Maneesha S                                                                    ""
""     Date           :   25 / 09 / 2017                                                                ""
""     Program        :   Find the difference between the square of the sum and the sum of the squares  ""
""                                                                                                      ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

limit = input("Enter the limit: ")
sum = 0
sumOfSquare = 0
for i in range(1, limit+1):
    sum = sum + i
    square = i * i
    sumOfSquare = sumOfSquare + square
squareOfSum = sum * sum
diff = squareOfSum - sumOfSquare
print("The difference is : ")
print diff
