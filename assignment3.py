Assignment: 3
#write a function to check wether input string is palindrome.
#write a function to find the factorial of a number.
#Write a function to find fibnnoicc series.

''''
a=str(input("enter the word"))
def wordcheck(b):
    if b[0:]==b[::1]:
        print("b,is palindrome")
    else:
        print("not a palindrome")
        wordcheck(a)
      '''
'''
A=int(input("enter the number"))
def check(b):
    factorial=1
    for i in range(1,A+1):
        factorial=factorial*i
    return("factorial is",factorial)


print(check(A))
'''

'''
#write a function to find the fibonacci series of number

def fib(n):
    L=[0]#initialize first element with 0
    a=0
    b=1#a=0 b=1
    for i in range(n):
        c=a+b
        a=b
        b=c
        L.append(a)
    return L
print(fib(int(input("Enter the number:"))))
'''




