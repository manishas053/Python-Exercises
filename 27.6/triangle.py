#Determine if a triangle is equilateral, isosceles, or scalene.


side1 = input("Enter the first side : ")
side2 = input("Enter the second side : ")
side3 = input("Enter the third side : ")

if side1 == side2 and side2 == side3:
    print("Equilateral triangle")
elif side1==side2 or side2 == side3 or side1 == side3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
