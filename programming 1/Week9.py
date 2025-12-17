import tkinter as tk

#root = tk.Tk()
#oot.geometry("400x300")

#root.grid_rowconfigure(0, weight=1)
#oot.grid_columnconfigure(0, weight=1)

#frame= tk.Frame(root, bg='lightgrey', width=200, height=100)
#frame.grid(row=0, column=0, sticky="nsew")


#label1 = tk.Label(frame, text="Label 1", bg='lightblue')
#label1.place(relx=0.5, rely=0.4, anchor='center')

#label2 = tk.Label(frame, text="Label 2", bg='lightblue')
#label2.place(relx=0.5, rely=0.6, anchor='center')



#root.mainloop()

#def show_second_screen():
#    frame1.pack_forget()
#    frame2.pack(fill='both', expand=True)

#def show_first_screen():
#    frame2.pack_forget()
#    frame1.pack(fill='both', expand=True)
#
#
#window=tk.Tk()
#window.geometry("400x300")


#frame1=tk.Frame(window)
#label1=tk.Label(frame1, text="This is the first screen", font=("Arial", 16))
#label1.pack(pady=20)
#button1=tk.Button(frame1, text="Go to Second Screen", command=show_second_screen)
#button1.pack()
#frame1.pack(fill="both", expand=True)

#frame2 = tk.Frame(window)
#label2= tk.Label(frame2, text="This is the second screen", font=("Arial", 16))
#label2.pack(pady=20)
#button2=tk.Button(frame2, text="Go to first  Screen", command=show_first_screen)
#button2.pack()
#entry = tk.Entry(frame2)
#entry.pack(pady=10)



#window.mainloop()


#root = tk.Tk()
#root.geometry("400x300")   



#FRAME 1
#frame1 = tk.Frame(root, bg='lightgrey')
#label1 = tk.Label(frame1, text="Login page", font=("Arial", 16))
#label1.place(relx=0.5, rely=0.2, anchor='center')
#label2 = tk.Label(frame1, text="Enter your username", font=("Arial", 16))
#label2.place(relx=0.5, rely=0.3, anchor='center')
#entry1 = tk.Entry(frame1)
#entry1.place(relx=0.8, rely=0.3, anchor='center')
#label3 = tk.Label(frame1, text="Enter your password", font=("Arial", 16))
#label3.place(relx=0.5, rely=0.4, anchor='center')
#entry2 = tk.Entry(frame1)
#entry2.place(relx=0.8, rely=0.4, anchor='center')
#frame1.pack(fill="both", expand=True)







#def show_input():
#    username = entry1.get()
#    password = entry2.get()
#   details_label.config(text=f"Username: {username}\nPassword: {password}")

#def show_second_screen():
#    frame1.pack_forget()
#    frame2.pack(fill='both', expand=True)


#button1 = tk.Button(frame1, text="Submit", command=show_second_screen)
#button1.place(relx=0.5, rely=0.5, anchor='center')

#FRAME 2
#frame2 = tk.Frame(root, bg='lightblue')         
#details_label = tk.Label(frame2, text="", font=("Arial", 12))
#details_label.place(relx=0.5, rely=0.3, anchor='center')

#button2 = tk.Button(frame2, text="Show details", command=show_input)
#button2.place(relx=0.5, rely=0.6, anchor='center')

def show_selection():
    selected= lst.get(tk.ACTIVE)
    txt.insert(tk.END,f"you selected: {selected}\n")
               
window= tk.Tk()

txt= tk.Text(window, height=30, width=5)
txt.pack()

lst= tk.Listbox(window)
lst.insert(1, "apple")
lst.insert(2, "banana")
lst.insert(3, "cherry")
lst.pack()

btn = tk.Button(window, text="show selection", command=show_selection)
btn.pack()



window.mainloop()




