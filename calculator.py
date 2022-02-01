def calculator(op,n1,n2):
    if op=="+":
        print(f"addition:{add(int(n1),int(n2))}")
    elif op=="-":
        print(f"subtraction:{subtraction(int(n1), int(n2))}")
    elif op=="*":
        print(f"multiplication:{multiply(int(n1), int(n2))}")
    elif op=="/":
        print(f"division:{division(int(n1), int(n2))}")


def add(n1,n2):
    return n1+n2
def subtraction(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def division(n1,n2):
>>>>>>> 8a2ad7bda395dd3945712e32846482c6110c2818
    return n1/n2


def get_input():
    op=input("enter the operator:")
    n1 = int(input("enter the first element:"))
    n2 = int(input("enter the second element:"))
<<<<<<< HEAD
    calculator(op, n1, n2)


get_input()
=======
    calculator(op,n1,n2)

get_input()


>>>>>>> 8a2ad7bda395dd3945712e32846482c6110c2818
