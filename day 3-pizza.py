print("welcome to pizza daily")
a=input()
b=input()
c=input()
bill=0
if a=="S":
   bill+=15
elif a=="M":
   bill+=20
else :
     bill+=35
if b=="Y":
    if a=="S":
       bill+=5
    elif a=="M":
       bill+=10
    else :
       bill+=20
else:
    bill+=0
if c=="Y":
    if a=="S":
       bill+=15
    elif a=="M":
       bill+=20
    else :
       bill+=30
else:
    bill+=0
print(f"Your final bill is:$ {bill}")
    
