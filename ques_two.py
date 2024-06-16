# Please write a program that takes a string as input from the user and prints whether the string is a palindrome or not.
name=input("Enter any string: ")
str=name
m=str[::-1]
if name==m:
    print("palindrome")
else:
    print("not")