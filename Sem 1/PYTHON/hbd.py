Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

============== RESTART: C:/Users/rupak/OneDrive/Desktop/Python Notes 21-11-2024.py =============
Enter the number to check: 145
145 is not a Krishnamurthy Number.

============== RESTART: C:/Users/rupak/OneDrive/Desktop/Python Notes 21-11-2024.py =============
Enter the number to check: 145
145 is a Krishnamurthy Number.

============== RESTART: C:/Users/rupak/OneDrive/Desktop/Python Notes 21-11-2024.py =============
Enter the number to check: 154
154 is not a Krishnamurthy Number.

============== RESTART: C:\Users\rupak\OneDrive\Desktop\Python Notes 21-11-2024.py =============
Enter the number to check: 153
153 is not a Armstrong Number.

============== RESTART: C:\Users\rupak\OneDrive\Desktop\Python Notes 21-11-2024.py =============
Enter the number to check: 153
153 is a Armstrong Number.

============== RESTART: C:\Users\rupak\OneDrive\Desktop\Python Notes 21-11-2024.py =============
Enter the number to check: 154
154 is not a Armstrong Number.

============== RESTART: C:\Users\rupak\OneDrive\Desktop\Python Notes 21-11-2024.py =============
Enter the number to check: 121
121 is not a Palindrom Number.

============== RESTART: C:\Users\rupak\OneDrive\Desktop\Python Notes 21-11-2024.py =============
Enter the number to check: 121
121 is a Palindrome Number.

============== RESTART: C:\Users\rupak\OneDrive\Desktop\Python Notes 21-11-2024.py =============
Enter the number to check: 131
131 is a Palindrome Number.
ls=[a, 10, 25, -14, 2.5, "Hi", 10]
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    ls=[a, 10, 25, -14, 2.5, "Hi", 10]
NameError: name 'a' is not defined
ls=['A', 10, 25, -14, 2.5, "Hi", 10]
print(ls)
['A', 10, 25, -14, 2.5, 'Hi', 10]

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


ls.remove(50)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    ls.remove(50)
ValueError: list.remove(x): x not in list
ls
['A', 10, 25, 10, -14, 2.5, 'Hi', 10, 25]
>>> ls.remove(25)
>>> ls
['A', 10, 10, -14, 2.5, 'Hi', 10, 25]
>>> ls.remove[25]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    ls.remove[25]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> ls.remove(2.5)
>>> ls
['A', 10, 10, -14, 'Hi', 10, 25]
>>> 
>>> ls=[11,41,14,34,43,21]
>>> ls.sort()
>>> ls
[11, 14, 21, 34, 41, 43]
>>> 
>>> ls.sort(reverse=True)
>>> ls
[43, 41, 34, 21, 14, 11]
>>> 
>>> st=["abc", "bcd", 'cda', "dda"]
>>> st.sort()
>>> st
['abc', 'bcd', 'cda', 'dda']
