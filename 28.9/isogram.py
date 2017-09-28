#Determine if a word or phrase is an isogram

string = raw_input("Enter a string : ")
count = 0
for i in range(0, len(string)):
    for j in range(0, len(string)):
        if i != j:
            if string[i] == string[j]:
                count += 1
if count == 0:
    print("Isogram")
else:
    print("Not an isogram")
