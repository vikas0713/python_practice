n=int(input("enter the input:"))
m = 3 * n
for i in range(1,n,2):
    print((i* ".|.").center(m,"-"))
print("welcome".center(m,"-"))
for i in range(n-2,-1,-2):
    print((i * ".|.").center(m,"-"))