#Program to find palindrome products in a given range

lower_limit = input("Enter the lower_limit : ")
upper_limit = input("Enter the upper limit : ")

for i in range(lower_limit, upper_limit):
    for j in range(lower_limit, upper_limit):
        product = i * j
        sum = 0
        limit = product
        while limit > 0:
            remainder = limit % 10
            sum = sum * 10 + remainder
            limit = limit / 10
        if sum == product:
            print i, j, product
