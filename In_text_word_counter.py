name = input("Enter file:")
handle = open(name)
dick=dict()
lst=list()
for line in handle:
    line=line.rstrip()
    if line.startswith('From '):
        a=line.split()
        lst.append(a[1])
for e in lst:
    dick[e]=dick.get(e,0)+1
bige=None
bigc=None
for k,v in dick.items():
    if bigc==None or bigc<v:
        bige=k
        bigc=v
print(bige,bigc)