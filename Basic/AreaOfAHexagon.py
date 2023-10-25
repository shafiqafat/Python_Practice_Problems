import math
a = int(input("a: "))
def hexagon(a):
    return ((3 * math.sqrt(3) * (a * a)) / 2)
if __name__=="__main__":
    print("Area: ","{0:.4f}" . format (hexagon(a)))
