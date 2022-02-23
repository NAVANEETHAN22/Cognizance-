str=input("TO PRINT THE GIVEN PATTERN\n")
def triangle(a):
 b = a - 1
 for i in range(0, a):
     for j in range(0, b):
            print(end=" ")
     b = b - 1
     for j in range(0, i+1):
         print("* ", end="")
     print("\r")

a = 5
triangle(a)
