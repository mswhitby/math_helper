import math

# This a python class
class MathHelper:

    # All functions start with "def
    # Ms. Whitby
    def square_area(side):
        return side * side

    # Saw []
    def triangle_area(base, height):
        return base * height / 2

    # Luis
    def rectangle_area(base, height):
        return base * height

    # Jordan
    def trapezoid_area(base_a, base_b, height):
       return base_a + base_b * height / 2
      
 
    # Sanaya
    def circle_area(base=None, height=None, diagonal_1=None, diagonal_2=None):
        return a2 + b2   
       
    # Nedavien
    def rhombus_area(base=None, height=None, diagonal_1=None, diagonal_2=None):
        if base and height:
            return base * height
        if diagonal_1 and diagonal_2:
            return diagonal_1 * diagonal_2 / 2
        else:
            return "You must enter either the base and height or the two diagionals"

    # Jaynarvious
    def line_eq(y=None, m=None, x=None, b=None):
      if m and x and b:
        return m * x + b

      if y and x:
        return y / x

    # Ashlinn
    # def octagon_area(side):
    #  return 2 * (1 + sqrt(2)) * (side**2)

    # Ethan
    def dodecagon_area(side):
    # return 2 *(2+sqrt(3)*s**)
     print(area)
    # Leroy


    # Leonardo
    # math.pi
    def oval_area():
      return math.pi*(major/2)*(minor/2)


# Ms. Whitby
area = MathHelper.square_area(2)
print(area)

# chance stanley
area = MathHelper.triangle_area(2, 3)      
print(area)

# Nedavien
area = MathHelper.rectangle_area(2, 4)
print(area)

#ashlinn
area = MathHelper.octagon_area(2, 8)
print(area)


area = MathHelper.trapezoid_area(2,4,6)
print(area)





