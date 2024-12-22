print('=====================')
print('Area Calculator')
print('=====================')

print("""Please select a shape:
        1) Triangle
        2) Rectangle
        3) Square
        4) Circle
        5) Quit""")

def get_shape():
    shape = int(input('Enter the number of the shape you would like to calculate the area for: '))
    if shape == 1:
        base = float(input('Enter the base of the triangle: '))
        height = float(input('Enter the height of the triangle: '))
        area = 0.5 * base * height
        print('The area of the triangle is ', area)
    elif shape == 2:
        length = float(input('Enter the length of the rectangle: '))
        width = float(input('Enter the width of the rectangle: '))
        area = length * width
        print('The area of the rectangle is ', area)
    elif shape == 3:
        side = float(input('Enter the side of the square: '))
        area = side * side
        print('The area of the square is ', area)
    elif shape == 4:
        radius = float(input('Enter the radius of the circle: '))
        area = 3.14 * radius * radius
        print('The area of the circle is ', area)
    elif shape == 5:
        print('Goodbye!')
    else:
        print('Invalid input. Please try again.')
        get_shape()

get_shape()


