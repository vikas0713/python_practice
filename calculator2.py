"""creating a calculator class"""
from calculator import substract,add,multi,div

class calculator:

    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2


    def operation(self,op):
        if op=="+":
            print(f"addition:{add(int(self.n1),int(self.n2))}")

        elif op=="-":
            print(f"substraction:{substract(int(self.n1),int(self.n2))}")

        elif op=="*":
            print(f"multiply:{multi(int(self.n1),int(self.n2))}")

        elif op=="/":
            print(f"divide:{div(int(self.n1),int(self.n2))}")


    def add(self):
        return self.n1+self.n2

    def substract(self):
        return self.n1-self.n2

    def multi(self):
        return self.n1*self.n2

    def div(self):
        return self.n1/self.n2



if __name__=='__main__':
    solution=calculator(8,9)

    solution.operation("+")









