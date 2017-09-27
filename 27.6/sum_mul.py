""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""                                                                                                               ""
""" Given a number, find the sum of all the multiples of particular numbers up to but not including that number  ""
""                                                                                                               ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

limit = input("Enter the limit : ")
num1 = input("Enter the 1st number : ")
num2 = input("Enter the 2nd number : ")
for i in range(1, limit-1):
    if (i % num1 == 0 or i % num2 == 0):
        print i
