"""this program interchange the  4th element with  4th last element of a list"""
class Interchange4:
    "class to  interchange the elements of list"
    def __init__(self):
        self.elements =[]

    def get_input(self):
        length = int(input("enter the elements:"))
        for el in range(length):
            self.elements.append(int(input(f"Enter element for {el} index: ")))

    def exchange_elements(self):
        print(f'before exchange elements: {self.elements}')
        temp = self.elements[3]
        self.elements[3]=self.elements[-4]
        self.elements[-4]= temp
        print(f'after exchange elements: {self.elements}')

if __name__=='__main__':
    interchange=Interchange4()
    interchange.get_input()
    interchange.exchange_elements()


