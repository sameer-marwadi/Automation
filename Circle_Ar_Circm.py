#!/usr/bin/env python3
import math
def calculate_area(radius):
    area = math.pi * radius ** 2
    return area

def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

def main():
    radius = float(input("Enter the radius of the circle: "))
    area = calculate_area(radius)
    circumference = calculate_circumference(radius)
    
    print(f"The area of the circle is: {area:.2f}")
    print(f"The circumference of the circle is: {circumference:.2f}")

if __name__ == "__main__":
    main()
    