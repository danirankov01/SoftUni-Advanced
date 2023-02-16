def rectangle(length, width):
    if(isinstance(length, int) == False or isinstance(width, int) == False):
        output = "Enter valid values!"
        return output
    
    result = ""

    def perimeter():
        perimeter = 2 * length + 2 * width
        return perimeter


    def area():
        area = length * width
        return area

    result += f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"
    return result


print(rectangle(2, 10))