from tkinter import *
from random import choice, randint, shuffle
from tkinter import messagebox
import pyperclip

FONT_NAME = "Courier"

BLUE = "#25236b"
LIGHT = "#C2C1E0"

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@', '=', '-', '_', '.', '^']

password_list = []


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    for char in range(randint(4,8)):
        password_list.append(choice(letters))
        password_list.append(choice(numbers))
        password_list.append(choice(symbols))


generate_password()


def shuffle_password():
    shuffle(password_list)
    rand_password = "".join(password_list)
    pyperclip.copy(rand_password)
    password_entry.insert(END, rand_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Empty fields not allowed.")

    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Please review your information.\nWebsite: {website} \nEmail: "
                                               f"{email} \nPassword: {password}\nWould "
                                               f"you like to save this information? ")
        if is_ok:
            with open("Sunshine", mode="a") as file:
                file.write(f"Website: {website} | Email: {email} | Password: {password}\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50, bg=BLUE)
window.title("Password Manager")

canvas = Canvas(width=200, height=200, highlightthickness=0, bg=BLUE)
canvas.grid(row=0, column=1)

lock_image = PhotoImage(file="blue_lock.png")
canvas.create_image(100, 100, image=lock_image)

website_label = Label(text="Website:", font=(FONT_NAME, 16, "bold"), bg=BLUE, fg=LIGHT)
website_label.grid(row=1, column=0)

website_entry = Entry(width=51, bg=LIGHT)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, padx=5)

email_label = Label(text="Email/Username:", font=(FONT_NAME, 16, "bold"), bg=BLUE, fg=LIGHT)
email_label.grid(row=2, column=0)

email_entry = Entry(width=51, bg=LIGHT)
email_entry.grid(row=2, column=1, columnspan=2, padx=5)

password_label = Label(text="Password:", font=(FONT_NAME, 16, "bold"), bg=BLUE, fg=LIGHT)
password_label.grid(row=3, column=0)

password_entry = Entry(width=31, bg=LIGHT)
password_entry.grid(row=3, column=1)

password_generator_button = Button(text="Generate Password", fg=BLUE, command=shuffle_password)
password_generator_button.grid(row=3, column=2, padx=5)

save_button = Button(text="Save", width=43, fg=BLUE, command=save)
save_button.grid(row=4, column=1, columnspan=3, padx=5, pady=3)

window.mainloop()
