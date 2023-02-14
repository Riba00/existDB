import Tkinter as tk

window = tk.Tk()
window.title("RIBA TREBALLADORS")
window.geometry("700x600")


def openInsertFrame():
    mainFrame.pack_forget()

    insertFrame.pack()
    insertLabelTitle.pack(pady=35)
    dniInsertLabel.pack()
    dniInsertEntry.pack()
    nomInsertLabel.pack()
    nomInsertEntry.pack()
    cognomInsertLabel.pack()
    cognomInsertEntry.pack()
    telefonInsertLabel.pack()
    telefonInsertEntry.pack()
    mailInsertLabel.pack()
    mailInsertEntry.pack()
    souInsertLabel.pack()
    souInsertEntry.pack()
    departamentInsertLabel.pack()
    departamentInsertEntry.pack()
    insertTreballadorButton.pack()
    backInsertToMainButton.pack()


def backInsertToMain():
    insertFrame.pack_forget()
    mainFrame.pack()


def insertTreballador():
    # TODO
    pass

def deleteTreballador():
     # TODO
    pass

def backDeleteToMain():
    deleteFrame.pack_forget()
    mainFrame.pack()

def openDeleteForm():
    mainFrame.pack_forget()

    deleteFrame.pack()
    deleteLabelTitle.pack()
    dniDeleteLabel.pack()
    dniDeleteEntry.pack()
    deleteTreballadorButton.pack()
    backDeleteToMainButton.pack()


def modifyTreballador():
     # TODO
    pass

def backModifyToMain():
    modifyFrame.pack_forget()
    mainFrame.pack()


def openModifyForm():
    mainFrame.pack_forget()

    modifyFrame.pack()
    modifyLabelTitle.pack()
    dniModifyLabel.pack()
    dniModifyEntry.pack()
    searchModifyTreballadorButton.pack()
    nomModifyLabel.pack()
    nomModifyEntry.pack()
    cognomModifyLabel.pack()
    cognomModifyEntry.pack()
    telefonModifyLabel.pack()
    telefonModifyEntry.pack()
    mailModifyLabel.pack()
    mailModifyEntry.pack()
    souModifyLabel.pack()
    souModifyEntry.pack()
    departamentModifyLabel.pack()
    departamentModifyEntry.pack()
    modifyTreballadorButton.pack()
    backModifyToMainButton.pack()


def exitForm():
    window.destroy()



# MAIN FORM
mainFrame = tk.Frame(window, padx=10, pady=50)
mainFrameLabelTitle = tk.Label(mainFrame, text="MENU PRINCIPAL", font="Helvetica 16 bold")
insertFormButton = tk.Button(mainFrame, text="INSERTAR TREBALLADOR", command=openInsertFrame)
deleteFormButton = tk.Button(mainFrame, text="ELIMINAR TREBALLADOR", command=openDeleteForm)
modifyFormButton = tk.Button(mainFrame, text="MODIFICAR TREBALLADOR", command=openModifyForm)
exitFormButton = tk.Button(mainFrame, text="SORTIR", command=exitForm)

mainFrame.pack()
mainFrameLabelTitle.pack()
insertFormButton.pack()
deleteFormButton.pack()
modifyFormButton.pack()
exitFormButton.pack()



# INSERT
insertFrame = tk.Frame(window, padx=10,pady=30)
insertLabelTitle = tk.Label(insertFrame, text="INSERTAR TREBALLADOR", font="Helvetica 16 bold")
dniInsertLabel = tk.Label(insertFrame, text="DNI")
dniInsertEntry = tk.Entry(insertFrame)
nomInsertLabel = tk.Label(insertFrame, text="Nom")
nomInsertEntry = tk.Entry(insertFrame)
cognomInsertLabel = tk.Label(insertFrame, text="Cognoms")
cognomInsertEntry = tk.Entry(insertFrame)
telefonInsertLabel = tk.Label(insertFrame, text="Telefon")
telefonInsertEntry = tk.Entry(insertFrame)
mailInsertLabel = tk.Label(insertFrame, text="Mail")
mailInsertEntry = tk.Entry(insertFrame)
souInsertLabel = tk.Label(insertFrame, text="Sou")
souInsertEntry = tk.Entry(insertFrame)
departamentInsertLabel = tk.Label(insertFrame, text="Departament")
departamentInsertEntry = tk.Entry(insertFrame)
insertTreballadorButton = tk.Button(insertFrame, text="INSERTAR TREBALLADOR", command=insertTreballador)
backInsertToMainButton = tk.Button(insertFrame, text="MENU PRINCIPAL", command=backInsertToMain)

# DELETE
deleteFrame = tk.Frame(window, padx=10, pady=30)
deleteLabelTitle = tk.Label(deleteFrame, text="ELIMINAR TREBALLADOR", font="Helvetica 16 bold")
dniDeleteLabel = tk.Label(deleteFrame, text="DNI")
dniDeleteEntry = tk.Entry(deleteFrame)
deleteTreballadorButton = tk.Button(deleteFrame, text="ELIMINAR TREBALLADOR", command=deleteTreballador)
backDeleteToMainButton = tk.Button(deleteFrame, text="MENU PRINCIPAL", command=backDeleteToMain)

# MODIFY
modifyFrame = tk.Frame(window, padx=10,pady=30)
modifyLabelTitle = tk.Label(modifyFrame, text="MODIFICAR TREBALLADOR", font="Helvetica 16 bold")
dniModifyLabel = tk.Label(modifyFrame, text="DNI")
dniModifyEntry = tk.Entry(modifyFrame)
searchModifyTreballadorButton = tk.Button(modifyFrame, text="BUSCAR", command=modifyTreballador)
nomModifyLabel = tk.Label(modifyFrame, text="Nom")
nomModifyEntry = tk.Entry(modifyFrame)
cognomModifyLabel = tk.Label(modifyFrame, text="Cognoms")
cognomModifyEntry = tk.Entry(modifyFrame)
telefonModifyLabel = tk.Label(modifyFrame, text="Telefon")
telefonModifyEntry = tk.Entry(modifyFrame)
mailModifyLabel = tk.Label(modifyFrame, text="Mail")
mailModifyEntry = tk.Entry(modifyFrame)
souModifyLabel = tk.Label(modifyFrame, text="Sou")
souModifyEntry = tk.Entry(modifyFrame)
departamentModifyLabel = tk.Label(modifyFrame, text="Departament")
departamentModifyEntry = tk.Entry(modifyFrame)
modifyTreballadorButton = tk.Button(modifyFrame, text="GUARDAR", command=modifyTreballador)
backModifyToMainButton = tk.Button(modifyFrame, text="MENU PRINCIPAL", command=backModifyToMain)

# DELETE
showTreballadorFrame = tk.Frame(window, padx=10, pady=30)
showTreballadorLabelTitle = tk.Label(deleteFrame, text="ELIMINAR TREBALLADOR", font="Helvetica 16 bold")
dniDeleteLabel = tk.Label(deleteFrame, text="DNI")
dniDeleteEntry = tk.Entry(deleteFrame)
deleteTreballadorButton = tk.Button(deleteFrame, text="ELIMINAR TREBALLADOR", command=deleteTreballador)
backDeleteToMainButton = tk.Button(deleteFrame, text="MENU PRINCIPAL", command=backDeleteToMain)

window.mainloop()
