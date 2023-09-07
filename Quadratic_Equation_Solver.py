import math
#Getting a,b,c from the Quadric equation(ax^2+bx+c=0)
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

## Determinant
det = (b * b - 4 * a * c)

### conditions for root
if det > 0:
    root1 = ((- b + math.sqrt(det))/2*a)
    root2 = ((- b - math.sqrt(det))/2*a)
    print(f"Real and Different roots: \n {root1} \n {root2}")
elif det == 0:
    root = (-b/(2*a))
    print("The root is: ", root)
else:
    print("The equation has no real roots.")


