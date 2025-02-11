'''#wapp to find the sum of digits of given number.
n=int(input("Enter a number:"))
s=0
while(n>0):
     rem=n%10
     s=s+rem
     n=n//10
print("Sum of digits",s)

#wapp to check perfect number.
n=int(input("Enter a number:"))
s=0
for i in range(1,n):
    if(n%i==0):
        s=s+i
if(s==n):
    print("The number is a Perfect Number")
else:
    print("The number is not a Perfect Number")

#calculate a distance between two points where x1,y1 and x2,y2 are user input.
import math
x1,y1=[int(c) for c in input("Enter the vertices:").split()]
x2,y2=[int(c) for c in input("Enter the another vertices:").split()]
d=math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("Distance=",d)

#calculate the area of a triangle using herons formula.
import math
a,b,c=[int(c) for c in input("Enter the sides:").split()]
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The area of triangle is=",area)

#wapp to print a ASCII value of character.
c=input("Enter a character:")
print("The ASCII value of",c,"is=",ord(c))

#write a program to read a character in upper case and print it in lower case.
c=input("Enter a word:")
print(c.upper())
print(c.lower())'''

#Wap to find x^y
b,e=[int(c) for c in input("Enter two numbers:").split()]
r=1
for i in range(1,e+1):
    r=r*b
print("value of x^y is:",r)

