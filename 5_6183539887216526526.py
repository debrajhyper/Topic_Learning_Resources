from tkinter import messagebox, Label, Button, FALSE, Tk, Entry


username = ("1")
password = ("1")


def try_login():
    print("Trying to login...")
    if username_guess.get() == username and password == password_guess.get():
        
        messagebox.showinfo("-- COMPLETE --", "You Have Now Logged In.", icon="info")
    else:
        messagebox.showinfo("-- ERROR --", "Please enter valid infomation!", icon="warning")


#Gui 
window = Tk()
window.resizable(width=FALSE, height=FALSE)
window.title("Log-In")
window.geometry("200x150")

#username & password entry boxes
username_text = Label(window, text="username:")
username_guess = Entry(window)
password_text = Label(window, text="password:")
password_guess = Entry(window, show="*")

#attempt to login button
attempt_login = Button(text="submit", command=try_login)


username_text.pack()
username_guess.pack()
password_text.pack()
password_guess.pack()
attempt_login.pack()
#Main Starter
window.mainloop()
