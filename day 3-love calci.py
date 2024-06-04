print("welcome to love calculator")
n1=input()
n2=input()
c_names=n1+n2
l_names=c_names.lower()

t=l_names.count("t")
r=l_names.count("r")
u=l_names.count("u")
e=l_names.count("e")
f_di=t+r+u+e
l=l_names.count("l")
o=l_names.count("o")
v=l_names.count("v")
e=l_names.count("e")
s_di=l+o+v+e
score=int(str(f_di)+str(s_di))
if(score<10) or (score>90):
    print(f"your score is {score}")
if(score>=40) or (score<=50):
    print(f"your score is {score}")
else:
    print(f"your score is {score}")
