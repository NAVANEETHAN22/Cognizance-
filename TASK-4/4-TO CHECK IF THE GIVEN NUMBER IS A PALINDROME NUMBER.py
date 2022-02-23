str=input("A PROGRAM TO CHECK IF THE GIVEN NUMBER IS A PALINDROME NUMBER\n")
a=int(input("ENTER THE NUMBER:"))
temp=a
rev=0
while(a>0):
    b=a%10
    rev=rev*10+b
    a=a//10
if(temp==rev):
    print("TRUE")
else:
    print("FALSE")
