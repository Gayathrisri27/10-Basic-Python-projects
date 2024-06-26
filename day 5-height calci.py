s_h=input().split()
for n in range(0,len(s_h)):
    s_h[n]=int(s_h[n])
t=0
for h in s_h:
    t+=h
print(f"total height={t}")
n=0
for s in s_h:
    n+=1
print(f"number of students={n}")
av=round(t/n)
print(f"average height={av}")
