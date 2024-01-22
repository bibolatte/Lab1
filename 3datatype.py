#1
x = str("Hello, PP2")
print(type(x))

#2
x = int(8)
print(type(x))

#3
x = float(4.65)
print(type(x))

#4
x = complex(6j)
print(type(x))

#5
x = list(("apple", "banana", "cherry"))
#or
x = ["apple", "banana, cherry"]

#6
x = tuple(("apple", "banana", "cherry"))
#or
x = ("apppe", "banana", "cherry")
print(type(x))

#7
x = range(6)
print(type(x))

#8
x = {"name" : "Dumbledore", "age" : 115}
print(type(x))
#or
x = dict(name="Dumbledore", age=115)
print(type(x))

#9
x = set(("apple", "banana", "cherry"))
x = {"apple", "banana", "cherry"}

#10
x = frozenset({"apple", "banana", "cherry"})

#11
x = False
x = bool(0)

#12
x = b"Hello"
x = bytes(5)

#13
x = bytearray(5)

#14
x = memoryview(bytes(5))

#15
x = None