f=open("1delhi.txt","r")
b=f.readlines()
c=0
for i in b:
    c=c+1
print(c)
f.close()