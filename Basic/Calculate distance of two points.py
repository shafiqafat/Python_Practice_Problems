import math
x1 = int(input("x1: "))
x2 = int(input("x2: "))
y1 = int(input("x1: "))
y2 = int(input("x2: "))

distance = math.sqrt(math.pow(x2 - x1, 2) +
                math.pow(y2 - y1, 2) * 1.0)


print("Distance: ",distance)
