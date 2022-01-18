"""
Interchange the Elements
"""


class InterchangeSecond:
    """Interchange third Element with third element from last """

    def __init__(self):
        self.elements = []

    def exchange_elements(self):
        print(f"Before exchange:{self.elements}")
        temp = self.elements[2]
        self.elements[2] = self.elements[-3]
        self.elements[-3] = temp
        print(f"After exchange: {self.elements}")

    def get_input(self):
        length = int(input("Enter length of list:"))
        for el in range(length):
            self.elements.append(int(input(f"Enter element for {el}th index")))


if __name__ == '__main__':
    interchangeSecond = InterchangeSecond()
    interchangeSecond.get_input()
    interchangeSecond.exchange_elements()
