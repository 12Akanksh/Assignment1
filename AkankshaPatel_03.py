#Work on slicing

List1=[1,2,"Python",33,"Java"]
print(List1[0:3])

print(List1[1:4])

print(List1[:2])

print(List1[2:])
#negative slicing 
print(List1[1:-2])       #start at 1,end at negative index(-3)

print(List1[-1:])

print(List1[:-1])

#slicing with step size 
print(List1[0:4:2])
print(List1[0:4:3])

print(List1[:1:-1])

print(List1[::-1])       #Display list in reverse order 

print(List1[-1:0:-1])

print(List1[0:5:1])

print(List1[-1:5:1])

_tuple1=(2,3,"two",4,5,6,"one",7,8,9)
print(_tuple1[0:8])
print(_tuple1[0:10:2])
print(_tuple1[6:-1])
print(_tuple1[1:-1:2])
print(_tuple1[0:-1:3])
print(_tuple1[::-4])

