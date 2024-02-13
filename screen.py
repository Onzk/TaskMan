from CTkTable import *
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")
default_font = ("Century Gothic", 36, "bold")

app = customtkinter.CTk(fg_color="black")
app.geometry("1280x720")
app.after(0, lambda: app.state("zoomed"))
app.title("TaskMan")

label = customtkinter.CTkLabel(
    app, text="Dashboard", fg_color="transparent", font=default_font, text_color="green"
)

label.place(x=16, y=16)
value = [[1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5]]

frame = customtkinter.CTkFrame(app)
frame.pack(expand=True, fill="both", padx=20, pady=100)

table = CTkTable(master=frame, row=5, column=5, values=value)
table.pack(expand=True, fill="both", padx=20, pady=20)

app.mainloop()
