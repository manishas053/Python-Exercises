####################################################################################################
# Input line has 2 integers k and p                                                                #
# Find sum of first k zcy numbers and output this sum modulo p                                     #
# If a number is palindrome and the number of digits in it is even then it is called a zcy number  #
####################################################################################################

k, p = map(int, raw_input().split())
count = 0
sum = 0
for i in range (11, 100):
    reverse = 0
    num = i
    while num > 0:
        rem = num % 10
        reverse = reverse * 10 + rem
        num = num / 10
    if reverse == i:
        count += 1
        if count <= k:
            sum += i
output = sum % p
print output
