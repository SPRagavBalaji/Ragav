questions={"What is the largest internal organ in the human body? A)liver, B)heart, C)lungs, D)kidneys":"a",
           "What is the capital of France A)Paris,B)London,C)Berlin,D)Madrid":"a",
           "What is the largest planet in our solar system A)Saturn B)Jupiter C)Earth D)Mars":"b",
           "Who wrote 'Romeo and Juliet A)robert B)William C)Arthur D)Shakespeare":"d",
           "What is the chemical symbol for water A)HCL B)NaOH C)H2O D)Nacl":"c"}
score=0
for q,a in questions.items():
    print(q)
    ans=input("your ans please:")
    if ans.lower()==a.lower():
        print("you are correct")
        score+=1
        print("your score is",score,"u can walk away with the money or continue and have a chance to lose it all")
        choice=input("do u want to continue y/n:")
        if choice.lower()=="n":
            break
    else:
        print("oops wrong answer. the answer is", a,"Game is over")
        score=0
        break

if score==0:
    print("your score is",score)
    print("sorry u won nothing")

elif score<=2:
    print("your score is",score)
    print("congratulations! you won 10K")
elif score==3:
    print("your score is",score)
    print("congrats u won 50K")
elif score==4:
    print("your score is",score)
    print("congats u won 100K")
elif score==5:
    print("your score is",score)
    print("congrats u won 1 million dollars")

    