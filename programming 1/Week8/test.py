from tkinter import*
from tkinter import messagebox
window= Tk()

#Naming
window.title("Tic Tac Toe")

count=0
command=True

#for new game
def newgame():
    global command , count
    for btn in (b1,b2,b3,b4,b5,b6,b7,b8,b9):
        btn.config(text="", bg="white", state=NORMAL)

#for Disable butn
def disablebutton():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

#check for win
def checkifwon():
    wins = [ (b1,b2,b3),(b4,b5,b6),(b7,b8,b9),
             (b1,b4,b7),(b2,b5,b8),(b3,b6,b9),
             (b1,b5,b9),(b3,b5,b7)
           ]

    for b,c,d in wins:
        if b["text"]== c["text"]== d["text"]!="" :
            winner=b["text"]
            b.config(bg="light green")
            c.config(bg="light green")
            d.config(bg="light green")
            messagebox.showinfo("winner",f"{winner} wins!")
            if count>=9:
                messagebox.showinfo("draw, the game is tied")
                count=0
            disablebutton()

def onclick(b):
    global count, command
    if b["text"]== "" and command is True:
        b["text"]="x"
        command = False
        count+=1
        checkifwon()
    elif b["text"]== "" and command is False:
        b["text"]="o"
        command = True
        count+=1
        checkifwon()
    else:
        messagebox.showerror("error, button already pressed")

#for creating buttons
b1=Button(window, text="", command=lambda: onclick(b1), width=6, height=3, bg="white")
b2=Button(window, text="", command=lambda: onclick(b2), width=6, height=3, bg="white")
b3=Button(window, text="", command=lambda: onclick(b3), width=6, height=3, bg="white")
b4=Button(window, text="", command=lambda: onclick(b4), width=6, height=3, bg="white")
b5=Button(window, text="", command=lambda: onclick(b5), width=6, height=3, bg="white")
b6=Button(window, text="", command=lambda: onclick(b6), width=6, height=3, bg="white")
b7=Button(window, text="", command=lambda: onclick(b7), width=6, height=3, bg="white")
b8=Button(window, text="", command=lambda: onclick(b8), width=6, height=3, bg="white")
b9=Button(window, text="", command=lambda: onclick(b9), width=6, height=3, bg="white")

ngb=Button(window, text="NEW GAME", command=newgame)

#for creating grid
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

ngb.grid(row=3,column=1)

window.mainloop()