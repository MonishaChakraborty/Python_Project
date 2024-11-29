from tkinter import *
from random import randint, choice
import string

root = Tk()
root.title("Password generator")
root.iconbitmap('C:/Users/monis/Downloads/password.ico')
root.geometry("500x500")

my_password = chr(randint(33,126))

#Generate random strong password
def new_rand():
    pw_length = int(my_Entry.get())  # get the length of the password
    all_characters = string.ascii_letters + string.digits + string.punctuation
    my_password = ''.join(choice(all_characters) for _ in range(pw_length))
    pw_entry.delete(0, END)     # Clear our entry box
    pw_entry.insert(0, my_password)

    # output password to the screen
    pw_entry.insert(0, my_password)

def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())
    

# Label Frame
lf = LabelFrame(root, text="How many Character?", font=("Arial", 20))
lf.pack(pady=50)    # pady is used to add external padding along y-axis i.e. padding is number of pixels that create spaces between widgets

#Create Entry Box To designate number of Character
my_Entry= Entry(lf, font=("Helvetica", 16))
my_Entry.pack(pady=20, padx=20)

#Create Entry Box For Our Returned password
pw_entry = Entry(root, text='', font=("Helvetica",16),width=15)
pw_entry.pack(pady=20)

#Create a frame for our Buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

#Create our Buttons
my_button= Button(my_frame,text="Generate Strong Password", font=("Arial", 16), command=new_rand)
my_button.grid(row=0,column=0,padx=10)

clip_button = Button(my_frame, text="Copy to Clipboard", font=("Arial", 16), command=clipper)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()
