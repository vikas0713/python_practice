"""
reversing the list
"""

class ReverseTheList:
    """ class to reverse the list"""
    def __init__(self):
        self.element= []

    def get_input(self):
        length = int(input("enter length of list:"))
        for el in range(length):
            self.element.append(int(input(f"enter element for {el} index:")))

    def reverse_list(self):
        print(f"before reverse: {self.element}")
        temp= self.element[::-1]
        print(f"after reverse: {temp}")


if __name__ == '__main__':
 reverse=ReverseTheList()
 reverse.get_input()
 reverse.reverse_list()