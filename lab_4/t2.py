class Rectangle:

    #  constructor -> height=2, width=3
    def __init__(self, height=2, width=3):
        if not isinstance(height and width, (int, float)):
            raise TypeError('Error: value is incorrect')
        self.__height = height
        self.__width = width

    def __str__(self):
        return 'Rectangle info: w: {0}, h: {1}'.format(self.__width, self.__height)

    @property
    def _height(self):
        return self.__height

    @_height.setter
    def _height(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Error: value is incorrect')
        self.__height = value

    @property
    def _width(self):
        return self.__width

    @_width.setter
    def _width(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Error: value is incorrect')
        self.__width = value

    #  PERIMETER w/ condition >100
    def get_perimeter(self):
        a = self.__width
        b = self.__height

        # formula --> P = (a + b) * 2 or P = a * 4, if a = b
        if(a <= 100) and (b <= 100):
            if a == b:
                p = a * 4
            else:
                p = 2 * (a + b)
            return p
        else:
            return "Selected input numbers do not satisfy app's condition. Retry again next time."

    #  S = a * b or a * a if a = b
    def get_square(self):

        a = self.__height
        b = self.__width

        if (a <= 100) and (b <= 100):
            return a * b
        else:
            return "Selected input numbers do not satisfy app's condition. Retry again next time."


def main():
    q = False
    while not q:
        num1 = int(input("height: "))
        num2 = int(input("width: "))

        obj1 = Rectangle(num1, num2)
        print(obj1)

        choose = input('write -> find perimeter. Or write -> find square Or -> both ')

        if choose == 'find perimeter':
            print('Perimeter: ', obj1.get_perimeter())
        elif choose == 'find square':
            print('Square: ', obj1.get_square())
        elif choose == 'both':
            print('The perimeter is: ', obj1.get_perimeter())
            print('The square is: ', obj1.get_square())
        else:
            print('Sorry, it is hard to understand people, try again...')

        x = input('Press <Enter> to try again or just enter something...')
        if len(x) < 1:
            continue
        else:
            break


if __name__ == '__main__':
    main()
