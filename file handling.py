import random

data = open("data.txt","w")
for i in range(10):
     num=random.randit(1,100)
     data.write(str(num)+",")
data.close

data=open 