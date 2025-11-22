import random

#dice = random.randint(1,6)
#dice2= random.randint(1,6)
#count=0
#while True:
#    if dice==6 and dice2==6:
#        print("the number on the first dice is:", dice)
#        print("the number on the dice is:", dice2)
#        print("u got it in",count,"rolls")
#        break
#    else:
#        dice = random.randint(1,6)
#        dice2= random.randint(1,6)
#        print("the number on the first dice is:", dice)
#        print("the number on the dice is:", dice2)
#        count+=1

#value= random.random()
#print("the random value is:", value)
#while True:
#    if value>1:
#        print(value)
#        break
#    else:
#        value= random.random()
#        print(value)


#fruits=["apple","banana","orange"]
#print(random.choice(fruits))

#coin = random.choice(["h","T"])
#print("the coin landed on:", coin)  

#count=0
#counth=0
#countt=0
#while count<10:
#    coin= random.choice(["H","T"])
#    print("the coin landed on:", coin)
#    if coin=="H":
#        counth+=1
#    if coin=="T":
#        countt+=1
#    count+=1
#rint("the number of heads is ", counth)
#print("the number of tails is ", countt)

#dice = random.randint(1,6)
#count=0
#while True:
#    if dice==6:
#        print("the number on the dice is:", dice)
#        print("it took",count,"rolls to get a 6")
#        break
#    else:
#        dice = random.randint(1,6)
#        print("the number on the dice is:",dice)
#        count+=1


#counth=0
#countt=0
#for i in range(0,1000):
#    coin= random.choice(["H","T"])
#    if coin=="H":
#        counth+=1
#    if coin=="T":
#        countt+=1
#total=countt+counth
#pofh= counth/total*100
#poft= countt/total*100
#print("no of h",counth,"probability of h",pofh)
#print("no of t",countt,"probability of t",poft)


def test():
    a=10
    b=20
    print(a+b)
def test2():
    a=10
    b=20
    return a+b
test()
print(test2())
