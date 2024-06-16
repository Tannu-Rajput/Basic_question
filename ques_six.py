# Please write a Python program that takes a list of numbers as input from the user and prints the sum of all the even/odd numbers in list.

n=[1,2,3,4,5,6,7,8,9,10]
even=0
odd=0
for x in n:
    if x%2==0:
        even+=x
    else:
        odd+=x
print("sum of even number",even)
print("Sum od odd number",odd)