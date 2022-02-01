FONT_LANG = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")
BACKGROUND_COLOR = "#B1DDC6"

from tkinter import Button, Tk, PhotoImage, Canvas
import random
from tkinter.constants import ACTIVE
import pandas

words_fr = []
words_en = []
word_right_count = []

try:
    df_words = pandas.read_csv("./data/saved_words.csv")
    print("got saved words")

except FileNotFoundError:
    df_words = pandas.read_csv("./data/french_words.csv")
    print("got default words")

# words = df_words.to_dict(orient="records")

for key, row in df_words.iterrows():
    words_fr.append(row.French)
    words_en.append(row.English)
    word_right_count.append(row.Count_Right)


class CardsMng:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
        self.front_card_img = PhotoImage(file="./images/card_front.png")
        self.back_card_img = PhotoImage(file="./images/card_back.png")
        self.right_img = PhotoImage(file="./images/right.png")
        self.wrong_img = PhotoImage(file="./images/wrong.png")
        self.actual_card = 0
        self.card = self.create_card()

        self.create_right_button()
        self.create_wrong_button()

    def create_right_button(self):
        self.right_bnt = Button(image=self.right_img, highlightthickness=0, command=self.remove_word)
        self.right_bnt.grid(row=1, column=1)

    def create_wrong_button(self):
        self.wrong_bnt = Button(image=self.wrong_img, highlightthickness=0, command=self.next_card)
        self.wrong_bnt.grid(row=1, column=0)

    def remove_word(self):

        word_right_count[self.actual_card] += 1

        if word_right_count[self.actual_card] > 1:
            words_fr.pop(self.actual_card)
            words_en.pop(self.actual_card)
            word_right_count.pop(self.actual_card)

        save_data()

        self.next_card()

    def next_card(self):
        self.actual_card = random.randrange(len(words_fr))

        card_canvas = self.card["front"][0]
        card_word = self.card["front"][1]

        card_canvas.itemconfig(card_word, text=f"{words_fr[self.actual_card]}")

        card_canvas = self.card["back"][0]
        card_word = self.card["back"][1]

        card_canvas.itemconfig(card_word, text=f"{words_en[self.actual_card]}")

    def create_card(self):
        self.actual_card = random.randrange(len(words_fr))

        back = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
        back.create_image(400, 260, image=self.back_card_img)
        back.create_text(400, 150, text="English", font=FONT_LANG)
        text_back = back.create_text(400, 263, text=f"{words_en[self.actual_card]}", font=FONT_WORD)
        back.grid(row=0, column=0, columnspan=2)
        back.bind("<Button-1>", lambda event: turn_card(front, back, "back"))

        front = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
        front.create_image(400, 260, image=self.front_card_img)
        front.create_text(400, 150, text="French", font=FONT_LANG)
        text_front = front.create_text(400, 263, text=f"{words_fr[self.actual_card]}", font=FONT_WORD)
        front.grid(row=0, column=0, columnspan=2)
        front.bind("<Button-1>", lambda event: turn_card(front, back, "front"))

        return {"front": [front, text_front], "back": [back, text_back]}


def turn_card(front, back, side):
    if side == "back":
        back.grid_remove()
        front.grid(row=0, column=0, columnspan=2)
    else:
        front.grid_remove()
        back.grid(row=0, column=0, columnspan=2)


def save_data():
    data = pandas.DataFrame({"French": words_fr, "English": words_en, "Count_Right": word_right_count})
    data.to_csv("./data/saved_words.csv", index=False)
