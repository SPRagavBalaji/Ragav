#length=int(input("Enter length: "))
#breadth=int(input("Enter breadth: "))
#height= int(input("Enter height: "))
#volume= length*breadth*height
#print("The volume of the fishtank  is:", volume)


#radius=int(input("Enter radius: "))
#radiussquared= radius*radius
#print("The area of the circle is:", 3.14*radiussquared)

#milk=float(1.50)
#bread=float(2.00)
#cheese=float(2.50)
#imilk=int(input("Enter number of milk cartons: "))
#ibread=int(input("Enter number of loaves of bread: "))
#icheese=int(input("Enter number of cheese packets:"))
#total=milk*imilk+bread*ibread+cheese*icheese
#print("the total cost of you groceries is:$", total)

#num=int(input("Enter a number: "))
#if num>0:
#    print("The Number is positive")
#elif num==0:
#    print("the number is zero")
#else:
#    print("The Number is negative ")


#tbill=float(input("Enter the total bill amount: "))
#if tbill>=200:
#   discount= 20.0
#if tbill>=100 and tbill<200:
#   discount= 10.0
#if tbill<100:
#   discount= 0.0
#disc=discount/100
#nbill= tbill-(tbill*disc)
#print("The bill amount after discount is:$", nbill)



#uname="admin"
#upass="1234"
#gname=input("Enter your username: ")
#gpass=input("Enter your password: ")
#if gname==uname and gpass==upass:
#    print("access granted")
#else:
#    print("access denied")


#speed=int(input("Enter the speed of the vehicle in km/h: "))
#if speed<60:
#    print("No points")
#if speed>60:
#  points= speed-60
#  points= points//5
#  print("your penalty points are ",points)
#    if points>12:
#        print("License suspended")




#temp=int(input("Enter the temperature: "))
#dtype= str(input("enter how the day is(sunny/rainy/windy): "))
#if not temp>0 and temp<40:
#    print("the temp must be in range")
#else:
#    if temp>=0 and temp<=15:
#        if dtype=="sunny":
#            print("a bit cold but still a beautiful day")
#        if dtype=="rainy":
#            print("Dont forget your umbrella and an jacket")
#        if dtype=="windy":
#           print("A coat will be a good idea maybe even a scarf")
#   if temp>=15 and temp<=45:
#        if dtype=="sunny":
#            print("Pretty hot out there dont forget your sunscreen")
#        if dtype=="rainy":
#            print("Spring rain? Dont bother with an umbrella just enjoy it")
#        if dtype=="windy":
#            print("Get your Board Surfs up!!")


#day=str(input("Enter day(mon,tue,etc.): "))
#match day: 
#    case "monday":
##        print("1st day")
#    case "tuesday":
#        print("2nd day")
#    case "wednesday":
#        print("3rd day")
#    case "thursday":
#        print("4th day")
#    case "friday":
#        print("5th day")
#    case "saturday":
#        print("6th day")
#    case "sunday":
#        print("7th day")
    


#print("options:","1.New Game","2.Load Game","3.Options","4.Exit",sep="\n")
#choice=int(input("Enter your choice: "))
#match choice:
#    case 1:
#        print("Starting a New Game")
#    case 2:
#        print("Loading Game")
#    case 3:
#        print("Opening Options now")
#    case 4: 
#        print("exiting the game")
#if choice==3:
#    print("game settings/n","audio settings/n","exit settings")
    

#light=str(input("Enter the traffic light color(red,yellow,green): "))
#if light=="red":
 #   print("stop")
#elif light=="yellow":
#    print("get ready")
#elif light=="green":
#    print("go")
#lse:
#    print("invalid color")



import random
num=random.randint(1,3)
gchoice= num
print("options:","1.Rock","2.Paper","3.Scissors",sep="\n")
choice=int(input("Enter your choice: "))
if choice==1 and gchoice==1:
    print("tie")
    print("computer chose rock")
elif choice==1 and gchoice==2:
    print("you lose")
    print("computer chose paper")
elif choice==1 and gchoice==3:
    print("you win")
    print("computer chose scissors")

if choice==2 and gchoice==1:
    print("you win")
    print("computer chose rock")
elif choice==2 and gchoice==2:
    print("tie")
    print("computer chose paper")
elif choice==2 and gchoice==3:
    print("you lose")
    print("computer chose scissors")

if choice==3 and gchoice==1:
    print("you lose")
    print("computer chose rock")
elif choice==3 and gchoice==2:
    print("you win")
    print("computer chose paper")
elif choice==3 and gchoice==3:      
    print("tie")
    print("computer chose scissors")

print("Done")      
