x = int(input())
y = int(input())
z = int(input())

if x == y and z == y:
    print(3)
elif x == y or y == z or x == z:
    print(2)
else:
    print(0)
