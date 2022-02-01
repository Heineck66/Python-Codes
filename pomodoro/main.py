# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.2
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

turn = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    global turn
    turn = 0
    l_turn["text"] = ""
    canvas.itemconfig(timer_text, text="00:00")
    l_title.config(text="Timer", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    global turn
    turn += 1
    if turn % 2 == 1:
        seconds = work_sec
        l_title.config(text="Work", fg=GREEN)
    elif turn == 8:
        seconds = long_sec
        l_title.config(text="Break", fg=RED)
    elif turn % 2 == 0:
        seconds = short_sec
        l_title.config(text="Break", fg=PINK)

    # bring windows to front
    window.lift()
    window.attributes("-topmost", True)
    window.attributes("-topmost", False)

    countdown(seconds)
    if turn % 2 == 0 and turn < 8:
        l_turn["text"] += "✔"

    if turn == 8:
        reset_timer()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

import math


def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = int(count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

from tkinter import Button, Canvas, Label, PhotoImage, Tk

window = Tk()
window.title("Pomodoro")
window.config(padx=60, pady=10, bg=YELLOW)
window.geometry("400x400")
window.resizable(False, False)

l_title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
l_title.pack()

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
img = canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.pack()

bnt_start = Button(text="Start", command=start_timer)
bnt_start.place(x=20, y=300)

bnt_reset = Button(text="Reset", command=reset_timer)
bnt_reset.place(x=215, y=300)

l_turn = Label(fg=GREEN, bg=YELLOW, font=(22))
l_turn.place(x=100, y=340)


window.mainloop()
