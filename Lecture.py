import math
# Konstruera en modul, area som inneåller funktioner 
# för att beräkna areor av rektanglear, cirklar och trianglar.
def rectangle_area(heigt, width):
    return heigt * width

def circle_area(radius):
    return int(math.pi * radius**2)

def triangle_area(base, height):
    return 1/2 * base * height

if __name__ == "__main__":
    print(rectangle_area(3,3))
    print(circle_area(5))
    print(triangle_area(2,8))