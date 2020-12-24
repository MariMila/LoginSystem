# importar as bíbliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Criar Janela
jan = Tk()
jan.title("Heart Systems - Acess Panel")
jan.geometry("600x300")
jan.configure(background="#F9E9E7")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.8)

# ====== Carregando Imagens
logo = PhotoImage(file="icons/logo_heart.png")

# ============ Widgets ==============
LeftFrame = Frame(jan, width=200, height=300, bg="#E8D1C2", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=395, bg="#6C0C27", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="#E8D1C2")
LogoLabel.place(x=0, y=50)

UserLabel = Label(RightFrame, text="Username:", font=("Robot", 20), bg="#6C0C27", fg="#F9E9E7")
UserLabel.place(x=15, y=80)

UserEntry = ttk.Entry(RightFrame, width=25)
UserEntry.place(x=165, y=89)

PassLabel = Label(RightFrame, text="Password:", font=("Robot", 20), bg="#6C0C27", fg="#F9E9E7")
PassLabel.place(x=15, y=120)

PassEntry = ttk.Entry(RightFrame, width=25)
PassEntry.place(x=165, y=129)

# Botões
LoginButton = ttk.Button(RightFrame, text="Login", width=30)
LoginButton.place(x=100, y=205)

RegisterButton = ttk.Button(RightFrame, text="Register", width=15)
RegisterButton.place(x=160, y=245)

jan.mainloop()
