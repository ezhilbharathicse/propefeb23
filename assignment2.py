'''
#inline if statement for simple if conditions
B= 15
#A will be 12 if B is 10 else A will be 13
A = 12 if B==10 else 13
print(A)
print("B is ten" if B==10 else "B is 13")
'''
#ForEach Loop
'''
fruits = ['apples','oranges','banana','cherry']
for fruit in fruits:
    print(fruit)
 #For each loop to iterate through list along with index
for  index,fruit in enumerate(fruits):
     print(index,fruit)
'''
'''
#looping through members - using the range() method
#range(5)---> will generate list [0,1,2,3,4]
for i in range(5):
    print(i)
#range(5,8)--->will generate list [5,6,7]
#range(5,10,2)--->will generate list [5,7,9]
#while loop
'''
'''
counter = 5
while counter > 0:
    print("counter value is",counter)
    counter = counter-1
 '''
#controlling the loop
#using break and continue keyword
'''
j= 0
for i in range(5):
    j = j+2
    print('i=',i,'j=',j)
    if j==2:
        break
print("outside the loop")
'''
'''
j = 0
for i in range(5):
    j=j+2
    if j==6:#if j value is 6,just
        continue
    print('i=',i,'j=',j)
print("outside the loop")
'''
'''
#program to check if a number is prime or not#user input

num=int(input("enter a num"))
if num==1:
    print(num,"is not a prime number")
flag = False
if num ==1:
    print(num,"is not a prime number")
elif num> 1:
    for i in range(2, num):
        if(num%i)==0:
            flag = True
            break
    if flag:
            print(num,"is not a prime number")
    else:
            print(num,"is a prime number")
'''

#write a program to find even numbers upto user input using while loop
#eg userinput is 8 then 2,3,6,8
'''
A= int(input("enter the num"))
j= 2
while j <=A:
    print(j,end='')
    j+=2
'''
#using for Loop
'''
a=int(input("Enter the number: "))
for i in range(2,a+1,2):
    print(i,end='')
'''
'''
#Assignment:2
#Write a program to find the factorial of user input number.
#Given an integer n, print all integers less than or equal to n
#Given an integer,print the sum of all even integers less than or equal to n
#Given n, print the sum of all integers less than or equal to n which are divisible by #by 3 or 5
'''
'''
#Given an integer n, print all integers less than or equal to n
a=int(input("Enter the number:"))
j=3
while j<=a:
    print(j,end='')
    j+=1
'''
'''
#Write a program to find the factorial of user input number.
a=int(input("Enter the number:"))
factorial=1
if a==0:
 print("0 is a factorial")
else:
 for i in range(1,a+1):
    factorial=factorial*i
 print("The factorial is",factorial)
 '''
'''
#Given an integer,print the sum of all even integers less than or equal to n
'''
'''
sum=0
a=int(input("Enter the number:"))
for i in range(1,a+1):      
    if(i%2==0):
        sum=sum+i
        print(sum)
'''
'''
a=int(input("Enter the number: "))
sum=0
for i in range(2,a+1,2):
    sum=sum+i
print(sum,end=' ')
'''
'''
#Given n, print the sum of all integers less than or equal to n which are divisible by #by 3 or 5
'''
'''
a=int(input("Enter the value:"))

a=int(input("Enter the number:"))
sum=0
for i in range(1,a+1):
    if(i%3==0) | (i%5==0)):
        sum=sum+i
print(sum)
'''