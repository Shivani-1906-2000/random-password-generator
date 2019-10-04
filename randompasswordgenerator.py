import random
a=input("Enter your first name")
b=input("Enter your second name")
spe=["!","@","#","$","%","^","&","*"]
num=["1","2","3","4","5","6","7","8","9","0"]
x=a[1::2]
y=b[1::2]
i=1
z=""
if(len(a)<=len(b)):
 for j in range(len(x)):
   s=random.choice(spe)
   n=random.choice(num)
   z=z+a[i]+s+n+b[i]
   i=i+2
 print("your random password is ")
 print(z)
elif(len(a)>=len(b)):
    for j in range(len(y)):
       s=random.choice(spe)
       n=random.choice(num)
       z=z+a[i]+s+n+b[i]
       i=i+2
    print("your random password is ")
    print(z)
else:
    print("length of first name and last name should be equal")
    


           

    




