""" creating a calculator """
from calculator import subtract,add,multiply,divide
class calculator:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2

    def operation(self,op):
        if op=="+":
            print(f"addition:{add(int(self.n1),int(self.n2))}")
        elif op=="-":
            print(f"subtraction:{subtract(int(self.n1),int(self.n2))}")
        elif op=="*":
            print(f"multiplication:{multiply(int(self.n1),int(self.n2))}")
        elif op=="/":
            print(f"divide:{divide(int(self.n1),int(self.n2))}")

    def add(self):
        return self.n1+self.n2
    def subtract(self):
        return self.n1-self.n2
    def multiply(self):
        return self.n1*self.n2
    def divide(self):
        return self.n1/self.n2

    def get_input(self):
        op = input("enter the operator:")
        n1 = int(input("enter the first number:"))
        n2 = int(input("enter the second number:"))
