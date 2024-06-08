from tkinter import *

window = Tk()
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)


def miles_to_km():
    miles = float(miles_input.get())
    result = miles * 1.609344
    km_label.config(text=result)


label_1 = Label(text="is equal to", font=("aerial", 12, "bold"))
label_1.grid(column=1, row=2)
label_1.config(pady=20, padx=20)

label_2 = Label(text="Miles", font=("aerial", 12, "bold"))
label_2.grid(column=3, row=1)
label_2.config(pady=20, padx=20)

label_3 = Label(text="Km", font=("aerial", 12, "bold"))
label_3.grid(column=3, row=2)
label_3.config(pady=20, padx=20)

miles_input = Entry(width=20)
miles_input.grid(column=2, row=1)

km_label = Label(text="0", font=("aerial", 24, "bold"))
km_label.grid(column=2, row=2)

button = Button(text="Calculate", width=15, command=miles_to_km)
button.grid(column=2, row=3)

window.mainloop()
