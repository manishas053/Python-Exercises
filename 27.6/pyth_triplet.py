""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""                                                                                            ""
"""  Find the product of pythagorean triplet a * b * c, for which a + b + c = 1000            ""
""                                                                                            ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'""'"""""

for a in range(1, 500):                                               #loop for base
    for b in range(1, 500):                                           #loop for altitude
        for c in range(1, 500):                                       #loop for hypotenuse
            if a*a + b*b == c*c :
                if a < b:
                    if a + b + c == 1000:
                        print("The pythagorean triplets are: ")
                        print a
                        print b
                        print c
                        print("Their product is : ")
                        print a * b * c
