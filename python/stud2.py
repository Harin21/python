sfile=open("stud.txt","r")
ofile=open("odd.txt","w")
efile=open("even.txt","w")
content=sfile.readlines()
print ('the contents of the file are')
print(content)
for i in range (len(content)):
    if (i%2==0):
       efile.write(content[i])
    else:
       ofile.write(content[i])
