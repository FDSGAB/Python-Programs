import re


#programa lê um arquivo .txt e soma todos os números contidos nele

l=list()
s=input("Enter doc file in directory: ")
x = open(s)
for line in x:
    a=list()
    line=line.rstrip()
    a = re.findall('[0-9]+',line)
    if len(a)>=1:
        for element in a:
            l.append(int(element))
print(sum(l))

