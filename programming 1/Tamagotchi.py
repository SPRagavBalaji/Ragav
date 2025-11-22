
hunger=50
happy=50
energy=50
#MENU
def menu():      
            print(" Welcome to the game tamagotchi")
            print("1) Feed your tamagotchi")
            print("2) Play with your tamagotchi")
            print("3) Put your tamagotchi to sleep")
            print("4) Show stats of tamagotchi")
            print("5) Reset Game")
            print("5) Exit")


def gamestart():
    
    def feed():
        global hunger, happy
        if hunger>0:
            hunger-=10
            happy+=5
            print("You fed your tamagotchi.")
            print(hunger)
        if hunger==0:
            print("Your tamagotchi has starved game over.Reset the game to play again.")
            
        menu()
        choice=int(input("Enter your choice : "))

    def play():
         global happy, energy
         if energy>0:
            happy+=15
            energy-=10
            print("You played with your tamagotchi.")
         if energy==0:
            print("Your tamagotchi collapes without energy. Game over. Reset the game to play again.")
         
    
    def sleep():
            global energy, hunger
            energy+=20
            hunger+=10
            print("Your tamagotchi is sleeping.")
            
    
    def reset():
        global hunger, happy, energy
        hunger=50
        happy=50
        energy=50
        print("Game has been reset.")
        
    choice=int(input("Enter your choice : "))
    while choice != 6:
        if choice==1:
            feed()
            menu()
            choice=int(input("Enter your choice : "))  
        elif choice==2:
            play()
            menu()
            choice=int(input("Enter your choice: "))
        elif choice==3:
            sleep()
            menu()
            choice=int(input("Enter your choice: "))
        elif choice==4:  # Showing stats
            global hunger, happy, energy
            print("Tamagotchi Stats:")
            print("Hunger:", hunger)
            print("Happiness:", happy)
            print("Energy:", energy)
            menu()
            choice=int(input("Enter your choice : "))
        elif choice==5:
            reset()
            menu()
            choice=int(input("Enter your choice : "))
        elif choice==6:
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            choice=int(input("Enter your choice : "))


menu()
gamestart()
