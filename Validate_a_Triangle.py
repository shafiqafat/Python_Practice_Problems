print("""To Check The validation
      Type 's' for validation with edges
      Type 'a' for validation with angles
    """)
select = input("Enter Validation Type: ")

#For when the edges are given
if select == 's':
    print("Validating With edge")
    edge1 = int(input("Enter first edge: "))
    edge2 = int(input("Enter second edge: "))
    edge3 = int(input("Enter third edge: "))
    if (edge1 + edge2) >= edge3 and (edge2 + edge3) >= edge1 and (edge3 + edge1) >= edge2:
        print("Triangle is Valid!!!")
    else:
        print("Triangle is Invalid!!!")

#For when the angles are given
elif select == 'a':
    print("Validating With Angle")
    angle1 = int(input("Enter first Angle: "))
    angle2 = int(input("Enter second Angle: "))
    angle3 = int(input("Enter third Angle: "))
    if angle1 != 0 and angle2 != 0 and angle3 != 0 and (angle1 + angle2 + angle3) == 180:
        if (angle1 + angle2) >= angle3 or (angle2 + angle3) >= angle1 or (angle3 + angle1) >= angle2:
            print("Triangle is Valid!!!")
        else:
            print("Triangle is Invalid!!!")
    else:
       print("Triangle is Invalid!!!") 