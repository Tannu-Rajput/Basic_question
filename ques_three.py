# Please write a program that takes a list of numbers as input from the user and prints the largest number in the list that is divisible by 3.
n=[2, 3,4,5,6,7,8,9]
m=n[0]
for x in n:
    if x>m:
        m=x
if m%3==0:       
    print(m ,"is largest and divisible by 3") 
else:
    print("largest but not divisible by 3")    