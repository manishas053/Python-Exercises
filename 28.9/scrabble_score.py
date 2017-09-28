#Given a word, compute the scrabble score for that word.

word = raw_input("Enter a word in uppercase : ")
sum = 0
count = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0

for i in range(0, len(word)):
    if (word[i] == 'A' or word[i] == 'E' or word[i] == 'I' or word[i] == 'O' or word[i] == 'U' or word[i] == 'L' or word[i] == 'N'):
        count1 += 1
    elif (word[i] == 'R' or word[i] == 'S' or word[i] == 'T'):
        count += 1
    elif (word[i] == 'D' or word[i] == 'G'):
        count2 += 1
    elif (word[i] == 'B' or word[i] == 'C' or word[i] == 'M' or word[i] == 'P'):
        count3 += 1
    elif (word[i] == 'F' or word[i] == 'H' or word[i] == 'V' or word[i] == 'W' or word[i] == 'Y'):
        count4 += 1
    elif (word[i] == 'K'):
        count5 += 1
    elif (word[i] == 'J' or word[i] == 'X'):
        count6 += 1
    else:
        count7 += 1
sum =  (1 * count1) + (1 * count) + (2 * count2) + (3 * count3) + (4 * count4) + (5 * count5) + (8 * count6) + (10 * count7)
print sum
