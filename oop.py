"""
Basic concept of Object oriented programming
"""


class InterchangeElements:
    """Class to interchange the first and last element"""

    def __init__(self):
        self.elements = []

    def exchange_elements(self):
        print(f"Before exchange: {self.elements}")
        temp = self.elements[0]
        self.elements[0] = self.elements[-1]
        self.elements[-1] = temp
        print(f"After exchange: {self.elements}")

    def get_input(self):
        length = int(input("Enter Length of List: "))
        for el in range(length):
            self.elements.append(int(input(f"Enter element for {el} index: ")))


if __name__ == '__main__':
    interchange_elements = InterchangeElements()
    interchange_elements.get_input()
    interchange_elements.exchange_elements()

