import tkinter  # here tkinter module will bring all the classes with it but not another module which lies in it
from tkinter import messagebox  # here messagebox is another module inside tkinter
import random
import pyperclip  # to copy password once it is generated.
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symboles = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symboles + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # to copy password once it is generated.
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    new_data = {
        website_entry.get(): {
            "email": email_entry.get(),
            "password": password_entry.get()
        }
    }

    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0 or len(email_entry.get()) == 0:
        messagebox.showerror(title="Oops", message="Please do not leave any fields empty !!")

    else:
        try:
            with open("data.json", mode="r") as data_file:
                # reading the old data
                data = json.load(data_file)
                # updating the old data to new data
                data.update(new_data)

        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            with open("data.json", mode="w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')

# ---------------------------- Search Password ---------------------------#
def find_password():
    website = website_entry.get()  # we will use this as key to look for password
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)  # it is in dictionary formate
            password = data[website]["password"]
            email = data[website]["email"]
    except KeyError:
        messagebox.showerror(title="OOPS", message="website not found !!")
    except FileNotFoundError:
        messagebox.showerror(title="OOPS", message="password storage file has not been created yet")
    else:
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        pyperclip.copy(password)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
lock_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry
website_entry = tkinter.Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()  # to have starting position of curser in this entry box.

email_entry = tkinter.Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "viralpatel5757@gmail.com")  # pre-populate the email

password_entry = tkinter.Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = tkinter.Button(text="Generate Password",  command=generate_password)
generate_password_button.grid(column=2, row=3)

save_password_button = tkinter.Button(text="Add Password", width=36, command=save_password)
save_password_button.grid(column=1, row=4, columnspan=2)

search_button = tkinter.Button(text="Search", command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()



