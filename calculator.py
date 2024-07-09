print("chose an number from below to calculate")
print(" add=1 \n sub=2\n mul=3\n div=4\n")
i=int(input("Enter the number:"))
if(i==1):
    x=int(input("the value of x :"))
    y=int(input("the value of y :"))
    print("The value of",x,"+",y,"is:",x+y)
elif(i==2):
     x=int(input("the value of x :"))
     y=int(input("the value of y :"))
     print("The value of",x,"-",y,"is:",x-y)
elif(i==3):
     x=int(input("the value of x :"))
     y=int(input("the value of y :"))
     print("The value of",x,"*",y,"is:",x*y)
elif(i==4):
     x=int(input("the value of x :"))
     y=int(input("the value of y :"))
     print("The value of",x,"/",y,"is:",x/y)
