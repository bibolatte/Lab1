#1
carname="Volvo"
print(carname)

#2
x=50
y=14
print(x+y)

#3
x=434
y=14
z=x-y
print(z)

#4
x, y, z = "orange", "banana", "apple"
print(x, y, z)

#5
x = y = z = "watermelon"
print(x)
print(y)
print(z)

#6
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("pyhton is " + x)