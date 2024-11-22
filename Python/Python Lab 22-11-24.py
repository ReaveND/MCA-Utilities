#Q1.   Program to find sum of the digits of a given number.
#Q2.   Program to print Perfect Number.

#Q1.

'''n=int(input("Enter the number to check: "))
s=0

while(n!=0):
    r=n%10
    s=s+r
    n=n//10

print("Sum of the digits: ",s)'''

#Q2.

'''n=int(input("Enter the number: "))
s=0

for i in range(1,(n-1)):
    if(n%i==0):
        s=s+i
if(s==n):
    print("%d is a Perfect Number."%s)
else:
    print("%d is not a Perfect Number."%s)'''
        

#Q3.Calculate distance between two points where x1,y1 and x2,y2 are user input.
'''import math
x1,y1= [int(c) for c in input("Enter the points to check: ").split()]
x2,y2= [int(c) for c in input("Enter the points to check: ").split()]
v=math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("Distance:",v)'''


#Q4.Calculate formula of a triangle using Heron's formula.
'''import math
a,b,c= [int(c) for c in input("Enter the points to check: ").split()]
s=a+b+c/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The area of the Triangle is: ",area)'''

#Q5.Print the ASCII value of a character.

'''d=input("Enter the Character: ")
print("The ASCII value of",d," is: ", ord(d))'''

#Q6. Print a program to read a character in upper case and print it in lower case.

a=input("Enter the character: ")
print(a.upper())
print(a.lower())

#Q7. Write a program to print x^y

x,y=[int(c) for c in input("Enter the numbers: ").split()]

for i in range(b,b+1):
    p
