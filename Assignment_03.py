#take default as r

f1=open("file_1.txt")

print(f1.read())

f1.close()

f1=open("file_1.txt","w")

f1.write("Wednesday \n")

f1=open("file_1.txt","r")

print(f1.read())

f1=open("file_1.txt","a")

print(f1.write("Weather is nice today"))

f1.close()

f1=open("file_1.txt")

print(f1.read())

#Creating a Calculator

def add():

    a=int(input("Enter the first number="))

    b=int(input("Enter the second number="))

    c=a+b

    print("add",a+b)

    with open('calfile.txt',"w") as f:

        f.write(f"{c} \n")

def sub():

   a=int(input("Enter the first number="))

   b=int(input("Enter the second number="))

   print("sub",a-b)

   with open("calfile.txt","a")as f:

       f.write(f"Subtraction of {a} and {b} = {a-b}\n")

def mul():

     a=int(input("Enter the first number ="))

     b=int(input("Enter second number ="))

     print("mul",a*b)

     with open('calfile.txt',"a")as f:

         f.write(f"Multiplication of {a} and {b} = {a*b} \n")

def div():

    a=int(input("Enter the first number="))  

    b=int(input("Enter the second number="))

    print("div",a/b)

    with open("calfile.txt","a")as f:

        f.write(f"Division of {a} and {b} = {a/b} \n)")

add()

sub()

mul()                                              

div()

