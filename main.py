from tkinter import *

FONT_NAME = "Courier"

BLUE = "#25236b"
LIGHT = "#C2C1E0"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

password_generator_button = Button(text="Generate Password",  fg=BLUE)
password_generator_button.grid(row=3, column=2, padx=5)

save_button = Button(text="Save", width=43, fg=BLUE)
save_button.grid(row=4, column=1, columnspan=3, padx=5, pady=3)

window.mainloop()