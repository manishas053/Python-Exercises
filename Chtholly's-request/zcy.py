####################################################################################################
# Input line has 2 integers k and p                                                                #
# Find sum of first k zcy numbers and output this sum modulo p                                     #
# If a number is palindrome and the number of digits in it is even then it is called a zcy number  #
####################################################################################################

k, p = map(int, raw_input().split())

#print k
#print p
count = 0
reverse = 0
sum = 0
for i in range (11, 100):
    num = i
    while num > 0:
        rem = num % 10
        reverse = reverse * 10 + rem
        num = num / 10
    if reverse == i:
        print reverse
        count += 1
        #print count
        if count <= k:
            sum += i
            #print sum
#output = sum % p
#print output
