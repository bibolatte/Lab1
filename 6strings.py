#docstrings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello, World!"
print(a[4]) #it's "o"

for x in "banana":
  print(x) #outputs separately

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.") #checks the words

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

b = "Hello, World!"
print(b[2:9]) #outputs from 2 until 8 includingly

b = "Hello, World!"
print(b[:5]) #outputs until 4th position

b = "Hello, World!"
print(b[2:]) #outputs from second pos.

b = "Hello, World!"
print(b[-5:-2]) #outputs from -5 until -2(not includingly)

a = "Hello, World!"
print(a.upper()) #Converts to UPPER LETTERS
print(a.lower()) #Converts to lower letter

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" without space

a = "Hello, World!"
print(a.replace("H", "M")) #атына заты сай

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

a = "Hello, World!"
b = a.split("o")
print(b) #here splits by the symbol

a = "Hello"
b = "World"
c = a + " " + b
print(c) #it's clear

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age)) #outputs exactly with {}

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#to highlight "" we need to write like this:
txt = "We are the so-called \"Vikings\" from the north."

txt = "\110\145\154\154\157"
print(txt) #ASCII

