#Convert a phrase to its acronym.

inp = raw_input("Enter a phrase : ")
print inp
inp = inp.upper()
print inp[0],
for i in range(1, len(inp) - 1):
    if inp[i] == ' ':
        print inp[i + 1],
