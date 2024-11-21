#Q. Write a program to check a number is Krishnamurthy or not.

#n=145
#n=1!+4!+5!

'''def factorial(n):                       # Function to change Factorial.
    fact=1
    for i in range(1,(n+1)):
        fact=fact*i
    return fact

if __name__== "__main__":       # Main Function.
    n=int(input("Enter the number to check: "))
    s=0
    temp=n
    while(n!=0):
        r=n%10    # To extract single digit from the input.
        s=s+factorial(r)
        n=n//10   # For factorial division.
    if(s==temp):
        print("%d is a Krishnamurthy Number."%temp)
    else:
        print("%d is not a Krishnamurthy Number."%temp)'''


#Q. Write a python program to check whether a number is Armstrong or not.

#n=153
#Count total number of digits present in the number=3
#if 1**3 + 5**3 + 3**3.

'''n=int(input("Enter the number to check: "))
temp=n
cnt=0
s=0
while(n!=0):
    cnt=cnt+1
    n=n//10
n=temp

while(n!=0):
    r=n%10
    s=s+r**cnt
    n=n//10

if(temp==s):
    print("%d is a Armstrong Number."%temp)
else:
    print("%d is not a Armstrong Number."%temp)'''


#Q. Write a python program to check whether a number is Palindrome or not.

n=int(input("Enter the number to check: "))
temp=n
s=0
while(n!=0):
    r=n%10
    s=s*10+r
    n=n//10

if(temp==s):
    print("%d is a Palindrome Number."%temp)
else:
    print("%d is not a Palindrome Number."%temp)


#Q. WAP to print whether a number is Perfect or not.


'''
The most popular data structure is called Sequence. In Sequence we have 4 different types of datatype.
1. List
2. Tupple
3. Set
4. Dictionary

            LIST

List is a collection of heterogenous datatypes, which is ordered and mutable in nature.
List allows duplicate values and in Python we can write list using '[ ]'. Mutable means that we can change the values of the List.
Ordered means that the list is indexed.

Example -

ls=['A', 10, 25, -14, 2.5, "Hi", 10]
print(ls)

Addition of Elements in a List:

1. Append (): This function can be used to add a new element at the end of the list.
2. Insert: This function can be used to add a new element in a list at a specific index of the list.

ls.append(25)
ls
['A', 10, 25, -14, 2.5, 'Hi', 10, 25]

ls.insert(3, 10)
ls
['A', 10, 25, 10, -14, 2.5, 'Hi', 10, 25]

l=len(ls)
l
9

c=ls.count(10)
c
3

for i in ls:
    print(i)
A
10
25
10
-14
2.5
Hi
10
25

st='python'
for i in st:
    print(i)

    
p
y
t
h
o
n

3. Remove: This function can be used to delete a specific number from the list.

4. Del: We can use Del to delete a number from list from a specific index.

    Sort:

ls=[11,41,14,34,43,21]
ls.sort()
ls
[11, 14, 21, 34, 41, 43]

ls.sort(reverse=True)
ls
[43, 41, 34, 21, 14, 11]

