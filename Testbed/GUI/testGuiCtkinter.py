from customtkinter import *
from PIL import Image

#  https://www.youtube.com/watch?v=Miydkti_QVE 1 min 51

app = CTk()
app.geometry("500x400")

set_appearance_mode("light")

img = Image.open("assets/buttonIcon.png")

combobox = CTkComboBox(master=app, values=["one", "two", "three"], fg_color="#0093E7",
                       border_color="#FBAB7F", dropdown_fg_color="#0093E9")

label = CTkLabel(master=app, text="Some Text...", font=("Arial", 20), text_color="lightblue")

btn = CTkButton(master=app, text="Click Me", corner_radius=10, fg_color="#C850C0", hover_color="#4158D0",)

btnSecond = CTkButton(master=app, text="Secondary", corner_radius=10, fg_color="transparent", hover_color="#4158D0",
                border_color="#FFCC70", border_width=2, image=CTkImage(dark_image=img, light_image=img))

label.place(relx=0.5, rely=0.4, anchor="center")
btn.place(relx=0.5, rely=0.5, anchor="center")
btnSecond.place(relx=0.5, rely=0.6, anchor='center')
combobox.place(relx=0.5, rely=0.7, anchor='center')



app.mainloop()
