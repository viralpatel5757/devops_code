import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# using pandas to read CSV
try:
    french_word_df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_word_df = pandas.read_csv("data/french_words.csv")
    to_learn = original_word_df.to_dict(orient="records")
else:
    to_learn = french_word_df.to_dict(orient="records")  # [{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'}...]

def random_french_word_generator():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_image, image=card_front_image)
    flip_timer = window.after(3000, flip_card)  # after(delay in ms, function to call, *args)

# create function to flip the card
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_image, image=card_back_image)

# create function to remove known words from the dict
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    random_french_word_generator()


window = tkinter.Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)  # after(delay in ms, function to call, *args)

# Canvas
canvas = tkinter.Canvas(width=800, height=540, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = tkinter.PhotoImage(file="images/card_front.png")
card_back_image = tkinter.PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 270, image=card_front_image)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 30, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 40, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# Buttons
right_image = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_image, border=0, width=90, height=90, command=is_known)
right_button.grid(column=1, row=1)

wrong_image = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_image, border=0, width=90, height=90, command=random_french_word_generator)
wrong_button.grid(column=0, row=1)

random_french_word_generator()





window.mainloop()
