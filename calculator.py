print("1.add")
print("2.sub")
print("3.mul")
print("4.div")

choice=int(raw_input("Enter your choice "))

num1=int(input("num1 is:"))
num2=int(input("num2 is:"))
if(choice==1):
  print(num1+num2)
elif(choice==2):
  print(num1-num2) 
elif(choice==3):
  print(num1*num2)
elif(choice==4):
  if(num2==0):
    print("Infinity")
  else:
    print(num1/num2)
