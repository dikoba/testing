import random

filename = open("DNA.txt", "w+")
counter = 0
total = 0

for i in range(100000):
	filename.write(random.choice('ATGC'))
filename.close()

contents = open("DNA.txt", "r")
for i in contents.read():
    total += 1
    if i == "G" or i == "C":
        counter += 1

gccontent = counter/total * 100

print("G/C content is " + str(gccontent) + "%")

contents.close()
