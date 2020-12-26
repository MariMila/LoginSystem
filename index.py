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
jan.iconbitmap("@icons/logo_heart.xbm")

# ====== Carregando Imagens
logo = PhotoImage(file="icons/logo_heart.png")

# ============ Widgets ==============
LeftFrame = Frame(jan, width=200, height=300, bg="#E8D1C2", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="#6C0C27", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="#E8D1C2")
LogoLabel.place(x=0, y=50)

UserLabel = Label(RightFrame, text="Username:", font=("Robot", 12), bg="#6C0C27", fg="#F9E9E7")
UserLabel.place(x=15, y=80)

UserEntry = ttk.Entry(RightFrame, width=25)
UserEntry.place(x=170, y=80)

PassLabel = Label(RightFrame, text="Password:", font=("Robot", 12), bg="#6C0C27", fg="#F9E9E7")
PassLabel.place(x=15, y=120)

PassEntry = ttk.Entry(RightFrame, width=25, show="*")
PassEntry.place(x=170, y=120)

# Botões
LoginButton = Button(RightFrame, text="Login", width=20, bg="#F9E9E7", font="Robot", activebackground="#E8D1C2",
                     activeforeground="#794A3D")
LoginButton.place(x=90, y=205)


def register():
    # Removendo Widgets do Login
    LoginButton.place(x=10000)
    RegisterButton.place(x=10000)
    UserLabel.place(x=15, y=95)
    UserEntry.place(x=170, y=95)
    PassLabel.place(x=15, y=135)
    PassEntry.place(x=170, y=135)
    # Inserindo Widgets de Cadastro
    nome_label = Label(RightFrame, text="Name:", font=("Robot", 12), bg="#6C0C27", fg="#F9E9E7")
    nome_label.place(x=15, y=15)

    nome_entry = ttk.Entry(RightFrame, width=25)
    nome_entry.place(x=170, y=15)

    email_label = Label(RightFrame, text="Email:", font=("Robot", 12), bg="#6C0C27", fg="#F9E9E7")
    email_label.place(x=15, y=55)

    email_entry = ttk.Entry(RightFrame, width=25)
    email_entry.place(x=170, y=55)

    confirm_label = Label(RightFrame, text="Retype Password:", font=("Robot", 12), bg="#6C0C27", fg="#F9E9E7")
    confirm_label.place(x=15, y=175)

    confirm_entry = ttk.Entry(RightFrame, width=25)
    confirm_entry.place(x=170, y=175)

    register_button = Button(RightFrame, text="Register", font="Robot", width=15, bg="#F9E9E7",
                             activebackground="#E8D1C2", activeforeground="#794A3D")
    register_button.place(x=200, y=240)

    def back():
        """Back to Login"""
        # Removendo Widgets de Cadastro
        nome_label.place(x=10000)
        nome_entry.place(x=10000)
        email_entry.place(x=10000)
        email_label.place(x=10000)
        back_button.place(x=10000)
        register_button.place(x=10000)
        confirm_label.place(x=10000)
        confirm_entry.place(x=10000)

        # Voltando as Configurações iniciais
        UserLabel.place(x=15, y=80)
        UserEntry.place(x=170, y=85)
        PassLabel.place(x=15, y=120)
        PassEntry.place(x=170, y=125)
        RegisterButton.place(x=140, y=255)
        LoginButton.place(x=90, y=205)

    back_button = Button(RightFrame, text="Back", font="Robot", width=15, bg="#794A3D", activebackground="#F9E9E7",
                         command=back)
    back_button.place(x=15, y=240)


RegisterButton = Button(RightFrame, text="Register", font="Robot", width=10, bg="#F9E9E7", activebackground="#E8D1C2",
                        command=register, activeforeground="#794A3D")
RegisterButton.place(x=140, y=255)

jan.mainloop()
