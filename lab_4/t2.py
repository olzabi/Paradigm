class Rectangle:

    #  constructor -> height=1, width=3
    def __init__(self, height=1, width=3):
        self.height = height
        self.width = width

    #  PERIMETER w/ condition >100
    def perimeter_finder(self):

        a = self.width
        b = self.height

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
    def square_finder(self):

        a = self.height
        b = self.width

        if (a <= 100) and (b <= 100):
            if a == b:
                s = a * a
            else:
                s = a * b
            return s
        else:
            return "Selected input numbers do not satisfy app's condition. Retry again next time."

    def output(self, chosen=3):
        if chosen == 0:
            quit()
        elif chosen == 1:
            print("Your choice: {}".format(chosen))
            print("The perimeter of rectangle is: {}".format(self.perimeter_finder()))
            input("Press ENTER to close.")
        elif chosen == 2:
            print("Your choice: {}".format(chosen))
            print("The square of rectangle is: {}".format(self.square_finder()))
            input("Press ENTER to close.")
        else:
            print("Your choice: {}".format(chosen))
            print("The perimeter of rectangle is: {}".format(self.perimeter_finder()))
            print("The square is: {}".format(self.square_finder()))
            input("Press ENTER to close.")


print(''' 
        This application will help you to find: 
        1. rectangle perimeter
        2. rectangle square.

        If you are interested in it,
        --Input your numbers,
        --Choose the way you want to output result:
        0. Press 0 to quit. 
        1. Press 1 if you need to find rectangle perimeter.
        2. Press 2 if you need to find rectangle square.
        3. Press 3 if you need to find in both ways.
        ''')

num1 = int(input("height: "))
num2 = int(input("width: "))
choice = int(input("Your choice: "))
obj1 = Rectangle(num1, num2)
obj1.output(choice)
