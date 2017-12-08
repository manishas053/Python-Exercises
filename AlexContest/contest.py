########################################################################################################
# One day Alex was creating a contest about his friends, but accidentally deleted it.                  #
# Fortunately, all the problems were saved, but now he needs to find them among other problems.        #
# write a program, which will determine if a problem is from this contest by its name.                 #
# It is known, that problem is from this contest if and only if its name contains one of Alex's        #
# friends' name exactly once. His friends' names are "Danil", "Olya", "Slava", "Ann" and "Nikita".     #
# Print "YES", if problem is from this contest, and "NO" otherwise.                                    #
########################################################################################################


input = raw_input()
strLength = len(input)
count = 0
for i in range(0, strLength - 1):
    if i + 5 <= strLength:
        if (input[i] == 'D' and input[i+1] == 'a' and input[i+2] == 'n' and input[i+3] == 'i' and input[i+4] == 'l'):
            count += 1

    if i + 4 <= strLength:
        if (input[i] == 'O' and input[i+1] == 'l' and input[i+2] == 'y' and input[i+3] == 'a'):
            count += 1

    if i + 5 <= strLength:
        if (input[i] == 'S' and input[i+1] == 'l' and input[i+2] == 'a' and input[i+3] == 'v' and input[i+4] == 'a'):
            count += 1

    if i + 3 <= strLength:
        if (input[i] == 'A' and input[i+1] == 'n' and input[i+2] == 'n'):
            count += 1

    if i + 6 <= strLength:
        if (input[i] == 'N' and input[i+1] == 'i' and input[i+2] == 'k' and input[i+3] == 'i' and input[i+4] == 't' and input[i+5] == 'a'):
            count += 1

if count == 1:
    print "YES"
else:
    print "NO"
