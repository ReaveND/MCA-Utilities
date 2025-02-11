## 25-11-2024

#WAP to create a list with first N natural numbers.
'''
ls=[x for x in range(1,11)]
print(ls)

# WAP to create a list with the numbers that are present in ls1 but not in ls2.

ls1=[1,2,3,4,5]
ls2=[4,5,6,7,8]
ls3=[x for x in ls1 if x not in ls2]
print(ls3)
'''

'''ls1=[1,2,3]
ls2=[4,5,6]
ls3=ls1+ls2

print(ls3)

ls4=ls2-ls1 # This will give error.

ls5=ls1*ls2 # This will give error.
'''


''' LAB ASSIGNMENT

1. Create a list with the numbers 1-20 and display the even and the odd numbers
and store the even and the odd numbers separately into different lists.


2. WAP ls1=[1,2,3,4,5] ls2=[4,5,6,7,8] to display the numbers that are common in both ls1 and ls2.

'''

'''st="Hello World"
st1=st.split()

print(st1) # Output= ['Hello', 'World']

print(st1[1])
print(st1[1][2])'''

# List within List.

#ls= [[1,2,3],[4,5,6],[7,8,9]]

# WAP to take a word as input and remove the duplicate letters from the word.

'''st="kolkata"
for i in st:
    print(i, end=" ")

ls=[]
for i in st:
    if i not in ls:
        ls.append(i)
print(ls, end=" ")'''

# WAP to take a word as input and check the occurence of each letter in the word.

'''ls="RupakSarkar"
for i in ls:
    c=0
    c=ls.count(i)
    print("%s is present %d times."%(i,c))'''

#   TUPLE -

''' A tuple is a sequence type of data structure which is ordered, indexed and heterogenous in nature.
Its contents are immutable. It also allows duplicate values. We can create a tuple using (). We cannot add any new
elements in a tuple. We cannot delete any elements in a tuple. We cannot modify existing values of a tuple'''

#tp=(10, 20, -30, "C", 4.5)
#print(tp[2])


#tp=(12,21,13,31,14,41)
#sorted(tp)
# Output - [12, 13, 14, 21, 31, 41]

# List within a Tuple.

# Tuple inside a List.
#ls=[1,(2,3,4),5]
#ls[1]   #Accesses the Tuple.

#   SET:

''' A set is a collection of unique elements that is unordered and unindexed in nature.
We can declare set using {}.Duplicate values are automatically removed from a set.'''

'''st=set()    #To declare an empty set.
st={1,2,3,4,"hi"}
print(st)
st.add()    #To add new value to the set.
st.update{[]}   #To add multiple values in the set.
st.remove() #To delete elements from a set.
st.pop()    #Always shows the first element of the set.
st.clear()  #Totally deletes the contents of the set.

st="kolkata"
st1=set(st)
st1  #Will print the values removing duplicates.'''


'''st1={1,2,3,4,5}
st2={4,5,6,7,8}
st3=st1.union(st2)
print("The Union of the sets are: ",st3)
st4=st1.intersection(st2)
print("The Intersection of the sets are: ",st4)
st5=st1.symmetric_difference(st2)
print("The Symmetric difference is: ",st5)

For Loop:
st={1,2,3}
for i in st:
print(i)
'''

#   DICTIONARY

''' A dictionary is a data structure available in python that stores the data in {key:value} pair.'''

#dt={}   #Empty Dictionary
'''dt={"Oishik":10,"Sayan":13, "Dip":14}
print(dt)
print(dt.values()) #Prints only Values.
print(dt.items())  #Prints in pairs separately.'''

#For Loop -

'''for i in dt:
    print(i) #Prints only the key.

for i in dt:
    print(dt[i]) #Prints with the values.'''

'''st="kolkata"
frq={}
for i in st:
    if i in frq:
        frq[i]+=1
    else:
        frq[i]=1

print(frq)'''
'''
#Q. WAP to find the highest frequency letters/characters.

dt={'A':10, 'S':20, 'C':30}
print(dt['A'])'''


'''Q.1. st = input("Enter the word to check: ")
freq = []
for i in st:
    for c in freq:
        if c[0]==i:
            c[1]+=1  
            break
    else:
        freq.append([i,1])

print("Letter frequencies:",freq)'''


def selection_sort(array):  
        length = len(array)  
        for i in range(length-1):  
            minIndex = i  
            for j in range(i+1, length):  
                if array[j]<array[minIndex]:  
                    minIndex = j  
            array[i], array[minIndex] = array[minIndex], array[i]  
        return array      
array = [72,4,10,38,2]  
print("The sorted array is: ", selection_sort(array))
