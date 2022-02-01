list1=[1,2,3,4,5,6,7,8,9,10]

dictionary ={}

for i in list1:
    if list1.index(i) % 2 == 0:
        dictionary.update({i: list1[list1.index(i)+1]})
print(dictionary)

