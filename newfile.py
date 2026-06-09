def calculate(a, b):
    area = a*b
    return area


totalarea =  calculate(5, 10) + calculate(3, 4)
print(totalarea)


from math import pi, sqrt

def circlearea (radius):
    area = pi * radius ** 2
    return area
def trianglearea (base, height):
    area = 0.5 * base * height
    return area

circle = circlearea(5)
triangle = trianglearea(10, 5)
print(circle)
print(triangle)