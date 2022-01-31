"""sorting the list"""

class SortingTheList:
    """class to sorting the list"""
    def __init__(self):
        self.elements=[]

    def get_input(self):
        length = int(input("Enter Length of List:"))
        for el in range(length):
            self.elements.append(int(input(f"Enter element for {el} index:")))

    def sort_ar(self):
        print(f"before sorting:{self.elements}")
        self.elements.sort()
        print(f"after sorting:{self.elements}")

if __name__ == '__main__':
    sort = SortingTheList()
    sort.get_input()
    sort.sort_ar()







