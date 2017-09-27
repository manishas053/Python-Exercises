

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'""""'""""
""     Author         :   Maneesha S                                      ""
""     Date           :   25 / 09 / 2017                                  ""
""     Program        :   Given a year, find if it is a leap year         ""
""                                                                        ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


year = input("Enter a year : ")
if ((year%4==0) and (year%100!= 0)):
    print("Leap year\n")
elif (year%400==0):
    print("Leap year\n")
else:
    print("Not a leap year\n")
