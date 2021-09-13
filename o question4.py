f=open("que main.text","r")
s=f.readlines()
for i in s:
    if "delhi" in i:
        a=open("qdelhi.text","a")
        a.write(i)
        print(a)
    elif "shimla" in i:
        b=open("qshimla.txt","a")
        b.write(i)
        print(b)
    else:
        c=open("qOthers.txt","a")
        c.write(i)
        print(c)
