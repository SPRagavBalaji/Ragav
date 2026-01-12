from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")

count = 0
clicked = True

# New Game button 

def new_game():
    global clicked, count
    clicked = True
    count = 0

    # reset all buttons
    for btn in (b1, b2, b3, b4, b5, b6, b7, b8, b9):
        btn.config(text=" ", state=NORMAL, bg="white", highlightbackground="white")


# To check if won
def checkifwon():
    # all 8 winning triplets (using your button names)
    wins = [
        (b1, b2, b3),
        (b4, b5, b6),
        (b7, b8, b9),
        (b1, b4, b7),
        (b2, b5, b8),
        (b3, b6, b9),
        (b1, b5, b9),
        (b3, b5, b7),
    ]

    for line in wins:
        b, c, d = line
        if b["text"] == c["text"] == d["text"] != " ":
            winner = b["text"]

            # highlight the winning pattern
            b.config(highlightbackground="light green")
            c.config(highlightbackground="light green")
            d.config(highlightbackground="light green")

            messagebox.showinfo("Tic Tac Toe", f"{winner} wins!")
            disable_buttons()
            return

    # draw check stays the same
    if count == 9:
        messagebox.showinfo("Tic Tac Toe", "It's a tie!")
        disable_buttons()
    # check draw
    if count == 9:
        messagebox.showinfo("Tic Tac Toe", "It's a tie!")
        disable_buttons()

def disable_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

# Buttons Clicked
def b_click(b):
    global clicked, count
    if b['text'] == " " and clicked is True:
        b['text'] = "X"
        clicked = False
        count += 1
        checkifwon()
    elif b['text'] == " " and clicked is False:
        b['text'] = "0"
        clicked = True
        count += 1
        checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe", "Button is already occupied \n Please choose another box")

# Building Buttons
b1 = Button(root, text=" ", width=6, height=3, bg="white", font=('Helvetica', 24), command=lambda: b_click(b1))
b2 = Button(root, text=" ", width=6, height=3, bg="white", font=('Helvetica', 24), command=lambda: b_click(b2))
b3 = Button(root, text=" ", width=6, height=3, bg="white", font=('Helvetica', 24), command=lambda: b_click(b3))

b4 = Button(root, text=" ", width=6, height=3, bg="white", font=('Helvetica', 24), command=lambda: b_click(b4))
b5 = Button(root, text=" ", width=6, height=3, bg="white", font=('Helvetica', 24), command=lambda: b_click(b5))
b6 = Button(root, text=" ", width=6, height=3, bg="white", font=('Helvetica', 24), command=lambda: b_click(b6))

b7 = Button(root, text=" ", width=6, height=3, bg="white",  command=lambda: b_click(b7))
b8 = Button(root, text=" ", width=6, height=3, bg="white",  command=lambda: b_click(b8))
b9 = Button(root, text=" ", width=6, height=3, bg="white",  command=lambda: b_click(b9))

# Grid the buttons
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)


# New Game Button

new_game_btn = Button(root, text="New Game", font=('Helvetica', 14),
                      command=new_game)
new_game_btn.grid(row=3, column=0, columnspan=3, sticky="nsew")


root.mainloop()
