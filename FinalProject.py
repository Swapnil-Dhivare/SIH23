from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
from tkinter import messagebox
from user_data_config import *


def clear_window():
    # Destroy or remove all widgets from the window
    for widget in root.winfo_children():
        widget.destroy()


def login(username, password):
    user_list = [x.get('username') for x in user_data]
    if username in user_list:
        user_id = user_list.index(username)
        if password == user_data[user_id].get('password'):
            return True
        else:
            return False
    else:
        return False


def authenticate():
    global valid
    username = username_entry.get()
    password = password_entry.get()

    if login(username, password):
        messagebox.showinfo("Authentication", "Login successful")
        clear_window()
        show_main_screen()
        # Add code here to open the main application window or perform other actions
    else:
        messagebox.showerror("Authentication Error", "Invalid username or password")


def change(text="type", src="English", dest="Hindi"):
    try:
        trans = Translator()
        trans1 = trans.translate(text, src=src, dest=dest)
        return trans1.text
    
    except Exception as e:
        print("Error:", e)
        return None
    


def show_main_screen():
    lab_txt = Label(root, text="Translator - Geek Byte", font=("Time New Roman", 20, "bold"), bg="bisque")
    lab_txt.place(x=100, y=41, height=50, width=300)

    frame = Frame(root).pack(side=BOTTOM)

    lab_txt = Label(root, text="Text:", font=("Time New Roman", 15), bg="bisque")
    lab_txt.place(x=100, y=100, height=20, width=300)

    Sor_txt = Text(frame, font=("Time New Roman", 20), wrap=WORD)
    Sor_txt.place(x=10, y=130, height=150, width=480)

    list_text = list(LANGUAGES.values())

    comb_sor = ttk.Combobox(frame, value=list_text)
    comb_sor.place(x=10, y=300, height=40, width=150)
    comb_sor.set("english")

    def data():
        s = comb_sor.get()
        d = comb_dest.get()
        masg = Sor_txt.get(1.0, END)
        textget = change(text=masg, src=s, dest=d)
        if textget is not None:
            dest_txt.delete(1.0, END)
            dest_txt.insert(END, textget)
        else:
            # Handle the case where translation is None
            dest_txt.delete(1.0, END)
            dest_txt.insert(END, "Translation not available")

    button_change = Button(frame, text="Translate", relief=RAISED, command=data,bg="dimgray",fg="white")
    button_change.place(x=170, y=300, height=40, width=150)

    comb_dest = ttk.Combobox(frame, value=list_text)
    comb_dest.place(x=330, y=300, height=40, width=150)
    comb_dest.set("hindi")

    lab_txt = Label(root, text="Translated Text:", font=("Time New Roman", 15), bg="bisque")
    lab_txt.place(x=100, y=360, height=20, width=300)

    dest_txt = Text(frame, font=("Time New Roman", 20), wrap=WORD)
    dest_txt.place(x=10, y=400, height=150, width=480)


root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg="bisque")

username_label = Label(root, text="Username:")
username_label.pack()
username_label.place(relx=0.5,rely=0.4,anchor=CENTER)
username_entry = Entry(root)
username_entry.pack()
username_entry.place(relx=0.5,rely=0.45,anchor=CENTER)

password_label = Label(root, text="Password:")
password_label.pack()
password_label.place(relx=0.5,rely=0.5,anchor=CENTER)
password_entry = Entry(root, show="*")  # Mask the password
password_entry.pack()
password_entry.place(relx=0.5,rely=0.55,anchor=CENTER)

login_button = Button(root, text="Login", command=authenticate)
login_button.pack()
login_button.place(relx=0.5,rely=0.6,anchor=CENTER)


root.mainloop()
