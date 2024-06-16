# Please write a program that takes a list of integers as input from the user and returns a new list with all the duplicate values removed.
n=[10,2,4,2,3,5,4,5,6,7,4,2]
m=[]
for x in n :
    if x not in m:
        m.append(x)
print(m) 