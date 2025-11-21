#def greet(name):
#    print("Hello",name)
#
#greet("ragav")
#
#print("outside function")

#global x
#x=10
#
#def f():
#   
#    return x
#    
#print(f(),x)

#def greet(name):
#   print(f"hello, {name}!")
#
#iname= input("Enter your name: ")
#greet(iname)

#def greet(name):
#    return f"Hello, {name}1"
#
#message = greet("Ragav")
#print(message)
#print(message.upper())


#def add(a,b):
#    return a+b
#
#ans=add(3,5)
#print("sum is",ans)


#def is_even(n):
#    """Returns True if n is even, False otherwise."""

#    return n%2==0
#print(is_even .__doc__)

#def add_two_numbers(a,b):
#    return a+b
#x= int(input("Enter first number: "))
#y= int(input("Enter second number: "))
#print("The sum is:", add_two_numbers(x,y))


#def isprime(n):
#    if n<2:
#        return False
#    d=2
#    while d*d<=n:
#        if n%d==0:
#            return False
#        d+=1
#    return True
#for k in range(1,21):
#    print(k,"prime?",isprime(k))
# ______________________________________________________________
# Simple car simulator: engine is a boolean, speed is an int.


#speed = 0
#engine = False
#
#def StartEngine(engine_started):
#    if not engine_started:
#        engine_started = True
##        print("Engine started")
#        return engine_started
#    else:
#        print("Engine already started")
#        return engine_started
#
#def accelerate(engine_started, speed):
#    if engine_started:
#        speed += 10
#        print("Accelerating. Speed is now", speed)
#        return speed
#    else:
#        print("Start the engine first")
#        return speed

#def breaks(engine_started, speed):
#    if engine_started:
#       if speed > 0:
#            speed = max(0, speed - 10)
#            print("Brakes applied. Speed is now", speed)
#        else:
#            print("Car is already stationary")
#        return speed
#    else:
#        print("Start the engine first")
#        return speed
#
#def display_speed(speed):
#    print("Current speed is", speed)


#print("1. Start Engine")
#print("2. Accelerate")
#print("3. Apply Brakes")
#print("4. Display Speed")
#print("5. Exit")
#choice = 0
#while choice==0:
#    choice = int(input("Enter your choice: "))
#    if choice == 1:
#        engine = StartEngine(engine)
#        choice = 0
#    elif choice == 2:
#        speed = accelerate(engine, speed)
#        choice = 0
##    elif choice == 3:
 #       speed = breaks(engine, speed)
 #       choice = 0
 #   elif choice == 4:
 #       display_speed(speed)
 #       choice = 0
#    elif choice == 5:
#        print("Exiting...")
#    else:
#        print("Invalid choice. Please try again.")




#def display_menu():
#    print("Menu:")
#    print("1) Burger - $15")
#    print("2) Fries - $8")
#    print("3) Soda - $2")
#    print("4) Nuggets - $14")

#def place_order():
  #  order = []
  #  total = 0
  #  while True:
  #      item = input("Enter the item you want to order (or 'done' to finish): ")
  #      if item.lower() == 'done':
  #          break
  #      order.append(item)
  #      if item.lower() == 'burger':
  #         total += 15
  #      elif item.lower() == 'fries':
  #          total += 8
  #      elif item.lower() == 'soda':
  #          total += 2
  #      elif item.lower() == 'nuggets':
  #          total += 14
 #       print(f"Added {item} to your order")
 #   return order,total
    


#print("Welcome to Fast Food restaurant")
#print("1) Place Order")
#print("2) View Menu")
#print("3) Exit")
#choice=0
#while choice==0:
#    choice=int(input("Enter your choice (1-3): "))
#    if choice == 1:
#        order,total=place_order()
#        print("Your order:", order)
#        print("Total amount due: $", total)
#        choice=0
#    elif choice == 2:
 #       display_menu()
#        choice=0
#   elif choice == 3:#
#        print("Exiting...")



#def add(a,b):
#    return a+b
#def subtract(a,b):
#    return a-b
#def multiply(a,b):
#    return a*b
#def divide(a,b):
#    return a/b
#def exponentiate(a,b):
#    return a**b





#print("Welcome to Calculator APP")
#print("1)Addition")
#print("2) Subtraction")
#print("3) Multiplication")
#print("4) Division")
#print("5) Exponentiation")
#print("6) Exit")
#choice=0
#while choice==0:
#   choice=int(input("Enter your choice (1-6): "))
#   if choice==1:
#        x=int(input("enter the first number:"))
#        y=int(input("enter the second number:"))
#        print("The sum is:", add(x,y))
#        choice=0
#   elif choice==2:
#        x=int(input("enter the first number:"))
#        y=int(input("enter the second numberL"))
#        print("The difference is:", subtract(x,y))
#        choice=0
#   elif choice==3:
#        x=int(input("enter the first number:"))
#        y=int(input("enter the second numberL"))
#        print("The product is:", multiply(x,y))
#        choice=0
#   elif choice==4:
#        x=int(input("enter the first number:"))
#        y=int(input("enter the second numberL"))
#        print("The quotient is:", divide(x,y))
#        choice=0
#   elif choice==5:
#        x=int(input("enter the first number:"))
##        y=int(input("enter the second numberL"))
 #       print("The result is:", exponentiate(x,y))
#        choice=0
##   elif choice==6:
 #       print("Exiting...")



goal = 0

def start_workout():
    global goal
    try:
        goal = float(input("Enter your fitness goal for today (in calories): "))
    except ValueError:
        print("Invalid input for goal. Please enter a number.")
        return
    print("What machine are you using? (treadmill/elliptical/stationary bike): ")
    mtype = input().lower()
    if mtype == "treadmill":
        try:
            duration = float(input("Enter duration of workout on treadmill (in minutes): "))
        except ValueError:
            print("Invalid input for duration.")
            return
        calories = duration * 1.5
        print("You have burned approx", calories, "calories on the treadmill.")
    elif mtype == "elliptical":
        try:
            duration = float(input("Enter duration of workout on elliptical (in minutes): "))
        except ValueError:
            print("Invalid input for duration.")
            return
        calories = duration * 2.5
        print("You have burned approx", calories, "calories on the elliptical.")
    elif mtype == "stationary bike":
        try:
            duration = float(input("Enter duration of workout on bike (in minutes): "))
        except ValueError:
            print("Invalid input for duration.")
            return
        calories = duration * 1
        print("You have burned approx", calories, "calories on the bike.")
    else:
        print("Invalid machine type.")
        return
    if calories >= goal:
        print("Congratulations! You broke your goal today")
    else:
        print("Still not at your goal,", goal - calories, "left")


def goaltday():
    global goal
    if goal == 0:
        print("No goal has been set today.")
        try:
            sgoal = float(input("Enter your goal for today: "))
            goal = sgoal
        except ValueError:
            print("Invalid input for goal.")
            return
    print("Today's goal is", goal)
    return goal


def menu():
    print("\nWelcome to the fitness program app")
    print("1) Start Workout")
    print("2) View Goal for today")
    print("3) Exit")

while True:
    menu()
    try:
        choice = int(input("Enter your choice (1-3): "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if choice == 1:
        start_workout()
    elif choice == 2:
        goaltday()
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
