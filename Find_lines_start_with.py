fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if line.startswith('From '):
        x=line.split()
        print(x[1])
        count=count+1
print("There were", count, "lines in the file with From as the first word")