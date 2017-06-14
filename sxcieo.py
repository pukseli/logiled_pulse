import time
file = open("näppäimet_map.csv", "r")
a = file.readlines()
file.close()


file = open("näppäimet.csv", "w")


for i in range(len(a)):
    b = a[i].replace("\n", "")
    b = b.replace(":",";")
    file.write(b + "\n")
file.close()

