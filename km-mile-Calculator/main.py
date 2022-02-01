from tkinter import Entry, Label, Tk, Button
from tkinter.constants import END


def calculate():
    input = float(e_input.get())
    if l_title["text"] == "Miles":
        result = input * 1.609
    else:
        result = input / 1.609
    l_result["text"] = f"{result:0.2f}"


def change_covertion():
    e_input.delete(0, "end")
    l_result["text"] = "0"
    if l_title["text"] == "Miles":
        l_title["text"] = "Km"
        l_km_miles["text"] = "Miles"
    else:
        l_title["text"] = "Miles"
        l_km_miles["text"] = "Km"


window = Tk()
window.minsize(300, 100)
window.title("Km Calculator")
window.config(padx=20, pady=20)

e_input = Entry(width=20)
e_input.focus()
e_input.grid(column=1, row=0)

l_title = Label(text="Miles", font=("Arial", 18, "bold"))
l_title.grid(column=2, row=0)

l_igual = Label(text="is equal to ", font=("Arial", 18))
l_igual.grid(column=0, row=1)

l_result = Label(text="0", font=("Arial", 18))
l_result.grid(column=1, row=1)

l_km_miles = Label(text="Km", font=("Arial", 18))
l_km_miles.grid(column=2, row=1)

bnt_calc = Button(text="Calculate", command=calculate)
bnt_calc.grid(column=1, row=2)

bnt_change = Button(text="Km to Miles", command=change_covertion)
bnt_change.grid(column=0, row=0)

window.mainloop()
