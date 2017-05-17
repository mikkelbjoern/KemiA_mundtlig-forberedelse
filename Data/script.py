import os

titles = open("Overskrifter.txt","r")

i = 1
for line in titles:
    name = str(i) + ") "+ line[:-1] 
    print(name)
    os.system('MKDIR "' + name + '"')
    i+= 1
