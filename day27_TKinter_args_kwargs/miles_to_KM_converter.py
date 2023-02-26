import tkinter

def convert():
    miles = float(user_input.get())
    km = miles*1.609
    label_answer.config(text=km)
    return km

# window (screen)
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Entry
user_input = tkinter.Entry(width=10)
user_input.grid(column=1, row=0)

# Button
button = tkinter.Button(text="Calculate", font=("Arial", 17), command=convert)
button.grid(column=1, row=2)

# Labels
label_miles = tkinter.Label(text="Miles", font=("Arial", 17))
label_miles.grid(column=2, row=0)

label_is_equal = tkinter.Label(text="is equal to:", font=("Arial", 17))
label_is_equal.grid(column=0, row=1)

label_Km = tkinter.Label(text="Km", font=("Arial", 17))
label_Km.grid(column=2, row=1)

label_answer = tkinter.Label(text=0, font=("Arial", 17))
label_answer.grid(column=1, row=1)




window.mainloop()

