#working on string template class

from string import Template

temp=Template('$name scored $runs runs')
print(temp.substitute(name="Rohit",runs="50"))


from string import Template 
class Temp(Template):
   delimiter="#"
s=("There are #num equipments in #name lab")
t=Temp(s)
print(t.substitute(num="20",name="Physics"))


#BMI calculator 

w=float(input("Weight="))

h=float(input("Height="))

bmi=w/(h*h)

print("Your BMI is ",bmi)

if bmi<=18.5 :

print("You are underweight")

elif bmi<=25:

print("You are Healthy")

elif bmi<=29.9:

print("You are overweight")

else:

print("You are obese")



   

































