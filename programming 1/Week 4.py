#for i in range(5):
#    print(i)
#
#
#print("-----")
#
#for i in range(3,31,3):
#    print(i)
#print("-----")
#
#for i in range(10,-1):
#    print(i)
#sum=0
#for i in range(0,21,2):
#    print("the even numbers are:", i)
#    sum=sum+i
#print("the sum of even numbers is:", sum)

#oddoreven=input("Do u want Even or Odd Numbers:")
#rval=int(input("Enter till what number u want to print the odd/even numbers:"))
#choice=0
#if oddoreven.lower()=="even":
#    choice=2
#else:
#    choice=1
#for i in range(1,rval+1,choice):
#    print(i)
#print("Thats all of your ",oddoreven,"numbers:",)
#print("-----")


#option=input("do u want to continue y/n:")
#while option=="y":
#    option=input("do u want to continue y/n:")

#print("you are out of the loop")

#minutes=0
#while minutes<60:
#   for i in range(minutes,minutes+1):
#        print("the minutes are:", minutes)
#    minutes+=1
#    print("you have completed an hour")



#con="y"
#while con=="y":
#    n_pplf=0
#    n_ppls=0
#    n_total=n_pplf+n_ppls
#    stop=0
#   choice=input(" are u an passenger y/n:")
#    if choice=="y":
#       p_class=input("enter the class of travel (first/second):")
#    if p_class=="first":
#        print("the ticket price is $150")
#        n_pplf+=1
#        fare=150
#    else:
#       print("the ticket price is $100")
#        n_ppls+=1
#        fare=100
#    p_age=int(input("enter the age of the passenger in number:"))


#    if p_age<=5 or p_age>=60:
#        fare=fare/2
#        print("the discounted fare is:",fare)
#    
#        if choice=="n":
#    
#            while stop<=5:
#                p_outf=int(input("enter the number of first class people leaving the train:"))
#               n_pplf-=p_outf
#                p_outsc=int(input("enter the number of second class people leaving the train:"))
#                n_ppls-=p_outsc
#                n_total=n_pplf+n_ppls
#            if n_total>50:
#                print("the train is full")
#                print("no passengers can board the train")
#                n_total=50
#            if n_total<50:
#                p_infc=int(input("enter the number of first class people boarding the train:"))
#                n_pplf+=p_infc
#                p_insc=int(input("enter the number of second class people boarding the train:"))
#                n_ppls+=p_insc
#            
#                n_total=n_pplf+n_ppls
#
 #   
#        
#        
#        
#        stop+=1
#        print("no of stops completed:", stop)
#        con=input("do u want to continue y/n:")
#        if con=="n":
#            break
          
#    if stop>5:
#        print("the train ride is over")

#n = int(input("Enter the number: "))
#for i in range(1, n):
#    print('*' * i)        


print("---MENU---")
print(" 1) Issue Ticket")
print(" 2) View Price Table")
print(" 3) Exit")
choice=int(input("Enter your choice (1-3): "))
while choice != 3:
    if choice == 1:
        vtype=input("Enter vehicle type (car/van/bike): ")
        if vtype.lower() == "car":                                                  #CAR PARKING
            dtype=int(input("Enter duration of parking in hours:"))
            if dtype>24 or dtype<=0:
                print("Invalid duration. Please enter a value between 1 and 24 hours.")
                dtype=int(input("Enter duration of parking in hours:"))
            dtime=input("Enter time of parking(peak/off-peak): ")
            if dtime!="peak" and dtime!="off-peak":
                print("Invalid time of parking. Please enter 'peak' or 'off-peak'.")
                dtime=input("Enter time of parking(peak/off-peak): ")
            if dtime=="peak":
                price=0.25*int(dtype)+2*int(dtype)
                print("The parking price is: $", price)
                total_price=price
            if dtime=="off-peak":
                price=2*int(dtype)
                print("The parking price is: $", price)
                total_price=price
            if dtype>5:
                discount=price*0.20
                total_price=price-discount
    
        elif vtype.lower() == "van":                                                    #VAN PARKING
            dtype=int(input("Enter duration of parking in hours:"))
            if dtype>24 or dtype<=0:
                print("Invalid duration. Please enter a value between 1 and 24 hours.")
                dtype=int(input("Enter duration of parking in hours:"))
            dtime=input("Enter time of parking(peak/off-peak): ")
            if dtime!="peak" and dtime!="off-peak":
                print("Invalid time of parking. Please enter 'peak' or 'off-peak'.")
                dtime=input("Enter time of parking(peak/off-peak): ")
            if dtime=="peak":
                price=0.25*int(dtype)+3*int(dtype)
                print("The parking price is: $", price)
                total_price=price
            if dtime=="off-peak":
                price=3*int(dtype)
                print("The parking price is: $", price)
                total_price=price
            if dtype>5:
                discount=price*0.20
                total_price=price-discount
                
        elif vtype.lower() == "bike":                                                   #BIKE PARKING
            dtype=int(input("Enter duration of parking in hours:"))
            if dtype>24 or dtype<=0:
                print("Invalid duration. Please enter a value between 1 and 24 hours.")
                dtype=int(input("Enter duration of parking in hours:"))
            dtime=input("Enter time of parking(peak/off-peak): ")
            if dtime!="peak" and dtime!="off-peak":
                print("Invalid time of parking. Please enter 'peak' or 'off-peak'.")
                dtime=input("Enter time of parking(peak/off-peak): ")
            if dtime=="peak":
                price=0.25*int(dtype)+1*int(dtype)
                print("The parking price is: $", price)
                total_price=price
            if dtime=="off-peak":
                price=1*int(dtype)
                print("The parking price is: $", price)
                total_price=price
            if dtype>5:
                discount=price*0.20
                total_price= price-discount
        if total_price>10:
                total_price=10
        print("The total parking price after discount is: $", total_price)
        print("The total duration of parking is :", dtype, "hours")
        print("Your time of parking is :", dtime)
        break
    
    elif choice == 2:
        print("Price Table:(non peak hours)")
        print("Vehicle  |   1h   2h   3h   4h   5h   6h   7h   8h")
        print("Car      |  $2   $4   $6   $8  $10  $10  $10  $10")
        print("Van      |  $3   $6   $9  $10  $10  $10  $10  $10")
        print("Bike     |  $1   $2   $3   $4   $5   $6   $7   $8")
        print("---------------------------------------------------")
        print("Price Table:(peak hours)")
        print("Vehicle  |   1h    2h    3h    4h      5h     6h     7h     8h")
        print("Car      |  2.50  5.00  7.50  10.00  10.00  10.00   10.00  10.00") 
        print("Van      |  3.25  6.50  9.75  10.00  10.00  10.00   10.00  10.00")
        print("Bike     |  1.25  2.50  3.75   5.00   6.00   7.00    8.00  10.00")
        break
        
else:
    print("Goodbye!")


        
