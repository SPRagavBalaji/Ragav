from tkinter import *
from tkinter import messagebox

# Game Logic

def create_board():
    return [" "]*9

def make_move(board,index,player):
    if board[index]==" ":
        board[index]=player
        return True
    return False

def check_winner(board):
    win_patterns=[
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in win_patterns:
        if board[a]==board[b]==board[c]!=" ":
            return board[a],(a,b,c)
    return None,None

def is_draw(board):
    return " " not in board

# GUI Layer 

root = Tk()
root.title("Tic Tac Toe")
current_player="X"
game_over=False
board=create_board()
buttons=[]

def update_title():
    if not game_over:
        root.title(f"Tic Tac Toe - {current_player}'s turn")
    else:
        root.title("Tic Tac Toe - Game Over")

def highlight_winning_line(indices):
    for i in indices:
        buttons[i].config(highlightbackground="light green")

def end_game(message):
    global game_over
    game_over=True
    for i in buttons:
        i.config(state=DISABLED)
    messagebox.showinfo("Tic Tac Toe",message)
    update_title()

def handle_button(index):
    global current_player,game_over
    if game_over:
        return
    if not make_move(board,index,current_player):
        messagebox.showerror("Tic Tac Toe","Cell already occupied!")

        return
    
    buttons[index].config(text=current_player)
    winner,win_indices=check_winner(board)
    if winner:
        highlight_winning_line(win_indices)
        end_game(f"{winner} wins!")
        return
    if is_draw(board):
        end_game("its a tie")
        return
    current_player="O" if current_player=='X' else 'X'
    update_title()

# Create buttons
for i in range(9):
    btn=Button(root,text=" ",width=6,height=3,bg="white",command=lambda idx=i:handle_button(idx))
    btn.grid(row=i//3,column=i%3)
    buttons.append(btn)

def newgame():
    global board,current_player,game_over
    board=create_board()
    current_player="X"
    game_over=False
    for btn in buttons:
        btn.config(text=" ",state=NORMAL,highlightbackground="white")
    update_title()
new_game_btn=Button(root,text="new game",command= newgame)
new_game_btn.grid(row=3,column=0,columnspan=3)

update_title()
root.mainloop()

