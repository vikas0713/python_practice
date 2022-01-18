def calculator(op,n1,n2):
    if op=="+":
        print(f"addition:{add(int(n1),int(n2))}")
    elif op=="-":
        print(f"substraction:{substract(int(n1), int(n2))}")
    elif op =="*":
        print(f"multiplication:{multi(int(n1), int(n2))}")
    elif op =="/":
        print(f"division:{div(int(n1), int(n2))}")

def add(n1,n2):
    return n1+n2
def substract(n1,n2):
    return n1 -n2
def multi(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2


def get_input():
    op=input("enter the operator:")
    n1 = int(input("enter the first element:"))
    n2 = int(input("enter the second element:"))
    calculator(op, n1, n2)

get_input()