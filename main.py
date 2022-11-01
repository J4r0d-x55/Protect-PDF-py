from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PyPDF2 import PdfFileWriter, PdfFileReader
import os

root = Tk()
root.title("Pdf Protect")
root.geometry("600x550+300+100")
root.resizable(False, False)


def browse():
    global filename
    filename = filedialog.askopenfile(initialdir=os.getcwd(), title="Selectionnez un fichier",
                                      filetype=(('PDF File', '*.pdf'), ('all files', '*.*')))
    entry1.insert(END, filename)


def Protect():
    mainfile = source.get()
    protectfile = target.get()
    code = password.get()

    if mainfile == "" and protectfile == "" and password.get() == "":
        messagebox.showerror("Données invalides", "Veuillez entrer des données valides")

    elif mainfile == "":
        messagebox.showerror("Données invalides", "Choisissez un fichier PDF")

    elif protectfile == "":
        messagebox.showerror("Données invalides", "Sélectionné un nom pour le fichier")

    elif password.get() == "":
        messagebox.showerror("Données invalides", "Entrez un mot de passe svp")

    else:
        try:
            out = PdfFileWriter()
            file = PdfFileReader(filename)
            num = file.numPages

            for idx in range(num):
                page = file.getPage(idx)
                out.addPage(page)

            out.encrypt(code)

            with open(protectfile, "wb") as f:
                out.write(f)


            source.set("")
            target.set("")
            password.set("")

            messagebox.showinfo("info", "Opération réalisée avec succès")
        except:
            messagebox.showerror("Données invalides", "Entrées invalides")


# Icone

image_icon = PhotoImage(file="y.png")
root.iconphoto(False, image_icon)

# Main

Top_image = PhotoImage(file="encrypt.png")
Label(root, image=Top_image).pack()

frame = Frame(root, width=580, height=290, bd=5, relief=GROOVE)
frame.place(x=10, y=220)

source = StringVar()
Label(frame, text="Votre fichier PDF : ", font="Terminal 10 bold", fg="#333").place(x=28, y=50)
entry1 = Entry(frame, width=30, textvariable=source, font="Terminal 15", bd=1)
entry1.place(x=150, y=48)

Button_icon = PhotoImage(file="folder1.png")
Button(frame, image=Button_icon, width=30, height=20, bg='#000', command=browse).place(x=500, y=45)

target = StringVar()
Label(frame, text="Renommez le PDF : ", font="Terminal 10 bold", fg="#333").place(x=38, y=100)
entry2 = Entry(frame, width=30, textvariable=target, font="Terminal 15", bd=1)
entry2.place(x=150, y=100)

password = StringVar()
Label(frame, text="Mot de passe : ", font="Terminal 10 bold", fg="#333").place(x=55, y=150)
entry3 = Entry(frame, width=30, textvariable=password, font="Terminal 15", bd=1)
entry3.place(x=150, y=150)

button_icon = PhotoImage(file="protect.png")
Protect = Button(root, compound=LEFT, image=button_icon, width=230, height=50, bg='#191970', fg='#000000',
                 font="Helvetica 14 bold", command=Protect)
Protect.pack(side=BOTTOM, pady=60)

root.mainloop()
