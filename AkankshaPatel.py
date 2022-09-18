#Examples of List 

L1=[6,8,3,5,1]

print(L1)

#mixed data types 

L2=["Aka",110,20,"Sept",39.6]

print(L2)

L3=[2,9,"kiwi",88]

print(len(L3))       #returns length 

L4=[228,44,60,8,74]

print(min(L4))       #returns minimum element 

print(max(L4))       #returns maximum greatest element of the list

print(type(L4))      #returns type 

print(sorted(L4))    #sort the elements of list

#Examples of List 

L4= [67,11,84,228]

print(sum(L4))

L5=["Clothes",22,1100,"Car","Horse"]

#delete element 

del L5[2]      

print(L5)

L5[2]=2200    #update 

print(L5)

L6=["Clothes",22,1100,"Car","Horse"]

L6[4]="House"

print(L6)

#shuffle randomly 

import random

L7=[110,220,330,550,660]

random.shuffle(L7)

print(L7)

L8=[11,22,44,66,88,99]

L8.reverse()           #reverse the list 

print(L8)

L8.index(99)           #returns the index of reversed list

#Examples of tuple 

#Tuple is immutable 

#we can not add,delete, shuffle or reverse the tuple 

#+operator and *operator can be used 

T1=('a','e','i','o','u')

print(T1)

print(type(T1))              #returns type 

print(len(T1))               #returns length of the tuple 

print(max(T1))               #returns greatest element 

print(min(T1))               #returns minimum element 

print(T1.index('i'))

T2=(5,4,4,7,9,10)

print(sum(T2))               #returns sum of elements of tuple 

print(T2.index(9))           #returns index 

print(T2.count(4))           #returns number of occurance of element 

T3=("APPARENTLY")

print(T3.count('T'))         #number of occurance 

print(T3.count('P'))

T4=(110,550,660,440,333)

print(sorted(T4))            #returns sorted tuple 

T5=("Kiwi","Orange","Apple","Berry")

print(sorted(T5))

T6=(1,2,4,6,7,8)

print(T6+T2)                 #concatenate tuple 

print(T6*2)                  #repeatition operator 

print(T5*3)

#Examples of Dictionary 

D1={"Amit":"001","Amol":"002","Dev":"003"}

print(D1)

D1["Ferry"]="004"

print(D1)                     #add new element 

D1["Ferry"]="005"             #replace the old value 

print(D1)

print(D1["Amol"])             #display the value associated with the key  

del D1["Ferry"]               #deletes the key 

print(D1)

print(len(D1))                #returns length of Dictionary 

D2={"Mango":"Yellow","Jamun":"Black"}

print(len(D2))
