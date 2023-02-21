from eulexistdb import db

import Tkinter as tk

EXISTDB_SERVER_USER = 'admin'
EXISTDB_SERVER_PASSWORD = 'Admin12345'
EXISTDB_SERVER_URL = "http://localhost:8080/exist"
EXISTDB_ROOT_COLLECTION = "/MP03UF6"

db = db.ExistDB(server_url=EXISTDB_SERVER_URL, username='admin', password='Admin12345')

window = tk.Tk()
window.title("RIBA TREBALLADORS")
window.geometry("700x600")


def selectQuery(query):
    try:
        sortida = ""
        res = db.executeQuery(query)
        hits = db.getHits(res)
        for i in range(hits):
            sortida = sortida + str(db.retrieve(res, i)) + '\n'
        return sortida
    except:
        return "Expressio incorrecta"


def ferQuery(query):
    try:
        db.executeQuery(query)
        return True
    except:
        return False


def existsDni(dni):
    dnis = []
    try:
        res = db.executeQuery("""for $dni in //treballador/dni
                                    return $dni/text()""")
        hits = db.getHits(res)
        for i in range(hits):
            dnis.append(str(db.retrieve(res, i)))
        if dni in dnis:
            return True
        else:
            return False
    except:
        pass


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
    statusInsertTreballadorLabel.pack()
    backInsertToMainButton.pack()


def backInsertToMain():
    dniInsertEntry.delete(0, tk.END)
    nomInsertEntry.delete(0, tk.END)
    cognomInsertEntry.delete(0, tk.END)
    telefonInsertEntry.delete(0, tk.END)
    mailInsertEntry.delete(0, tk.END)
    souInsertEntry.delete(0, tk.END)
    departamentInsertEntry.delete(0, tk.END)
    statusInsertTreballadorLabel.config(text="")

    insertFrame.pack_forget()
    mainFrame.pack()


def insertTreballador():
    try:
        departament = departamentInsertEntry.get()
        dni = dniInsertEntry.get()
        nom = nomInsertEntry.get()
        cognom = cognomInsertEntry.get()
        telefon = int(telefonInsertEntry.get())
        mail = mailInsertEntry.get()
        sou = float(souInsertEntry.get())

        if departament == "":
            raise Exception
        elif dni == "":
            raise Exception
        elif nom == "":
            raise Exception
        elif cognom == "":
            raise Exception
        elif telefon == "":
            raise Exception
        elif mail == "":
            raise Exception
        elif sou == "":
            raise Exception

        if existsDni(dni):
            statusInsertTreballadorLabel.config(text="DNI ja llistat")
        else:
            insertQuery = """update insert 
                            <treballador>\n
                                <departament>""" + str(departament) + """</departament>\n
                                <dni>""" + str(dni) + """</dni>\n
                                <nom>""" + nom + """</nom>\n
                                <cognom>""" + cognom + """</cognom>\n
                                <telefon>""" + str(telefon) + """</telefon>\n
                                <mail>""" + mail + """</mail>\n
                                <sou>""" + str(sou) + """</sou>\n
                                </treballador>\n 
                            into /personal"""
            if ferQuery(insertQuery):
                statusInsertTreballadorLabel.config(text="Treballador insertat correctament")
                dniInsertEntry.delete(0, tk.END)
                nomInsertEntry.delete(0, tk.END)
                cognomInsertEntry.delete(0, tk.END)
                telefonInsertEntry.delete(0, tk.END)
                mailInsertEntry.delete(0, tk.END)
                souInsertEntry.delete(0, tk.END)
                departamentInsertEntry.delete(0, tk.END)

            else:
                statusInsertTreballadorLabel.config(text="Alguna cosa ha fallat")
    except:
        statusInsertTreballadorLabel.config(text="Alguna dada es incorrecta")


def deleteTreballador():
    dni = dniDeleteEntry.get()

    if existsDni(dni):
        deleteQuery = """update delete //treballador[dni='""" + dni + """']"""

        if ferQuery(deleteQuery):
            statusDeleteTreballadorLabel.config(text="Treballador eliminat correctament")
            dniDeleteEntry.delete(0, tk.END)
    else:
        statusDeleteTreballadorLabel.config(text="DNI incorrecte")


def backDeleteToMain():
    statusDeleteTreballadorLabel.config(text="")
    deleteFrame.pack_forget()

    mainFrame.pack()


def openDeleteForm():
    mainFrame.pack_forget()

    deleteFrame.pack()
    deleteLabelTitle.pack()
    dniDeleteLabel.pack()
    dniDeleteEntry.pack()
    deleteTreballadorButton.pack()
    statusDeleteTreballadorLabel.pack()
    backDeleteToMainButton.pack()


def searchModifyTreballador():
    dniMofifySearch = dniModifyEntry.get()

    departamentModifyEntry.delete(0, tk.END)
    nomModifyEntry.delete(0, tk.END)
    cognomModifyEntry.delete(0, tk.END)
    telefonModifyEntry.delete(0, tk.END)
    mailModifyEntry.delete(0, tk.END)
    souModifyEntry.delete(0, tk.END)

    if existsDni(dniMofifySearch):
        departament = selectQuery("""for $treballador in //treballador
                                    where $treballador/dni='""" + dniMofifySearch + """'
                                    return $treballador/departament/text()""")
        nom = selectQuery("""for $treballador in //treballador
                                    where $treballador/dni='""" + dniMofifySearch + """'
                                    return $treballador/nom/text()""")
        cognom = selectQuery("""for $treballador in //treballador
                                    where $treballador/dni='""" + dniMofifySearch + """'
                                    return $treballador/cognom/text()""")
        telefon = selectQuery("""for $treballador in //treballador
                                    where $treballador/dni='""" + dniMofifySearch + """'
                                    return $treballador/telefon/text()""")
        mail = selectQuery("""for $treballador in //treballador
                                    where $treballador/dni='""" + dniMofifySearch + """'
                                    return $treballador/mail/text()""")
        sou = selectQuery("""for $treballador in //treballador
                                    where $treballador/dni='""" + dniMofifySearch + """'
                                    return $treballador/sou/text()""")
        departamentModifyEntry.insert(0, departament[:-1])
        nomModifyEntry.insert(0, nom[:-1])
        cognomModifyEntry.insert(0, cognom[:-1])
        telefonModifyEntry.insert(0, telefon[:-1])
        mailModifyEntry.insert(0, mail[:-1])
        souModifyEntry.insert(0, sou[:-1])
    else:
        statusSearchModifyLabel.config(text="DNI no llistat")


def modifyTreballador():
    departament = departamentModifyEntry.get()
    nom = nomModifyEntry.get()
    cognom = cognomModifyEntry.get()
    telefon = int(telefonModifyEntry.get())
    mail = mailModifyEntry.get()
    sou = float(souModifyEntry.get())
    modifyQuery = """update replace //treballador[dni='"""+dniModifyEntry.get()+"""']
                    with <treballador>
                            <departament>"""+departament+"""</departament>
                            <dni>"""+dniModifyEntry.get()+"""</dni>
                            <nom>"""+nom+"""</nom>
                            <cognom>"""+cognom+"""</cognom>
                            <telefon>"""+str(telefon)+"""</telefon>
                            <mail>"""+mail+"""</mail>
                            <sou>"""+str(sou)+"""</sou>
                          </treballador>"""
    if ferQuery(modifyQuery):
        statusModifyLabel.config(text="Treballador modificat correctament")

        dniModifyEntry.delete(0, tk.END)
        departamentModifyEntry.delete(0, tk.END)
        nomModifyEntry.delete(0, tk.END)
        cognomModifyEntry.delete(0, tk.END)
        telefonModifyEntry.delete(0, tk.END)
        mailModifyEntry.delete(0, tk.END)
        souModifyEntry.delete(0, tk.END)
    else:
        statusModifyLabel.config(text="Alguna cosa ha fallat")

def backModifyToMain():
    departamentModifyEntry.delete(0, tk.END)
    nomModifyEntry.delete(0, tk.END)
    cognomModifyEntry.delete(0, tk.END)
    telefonModifyEntry.delete(0, tk.END)
    mailModifyEntry.delete(0, tk.END)
    souModifyEntry.delete(0, tk.END)
    dniModifyEntry.delete(0, tk.END)
    statusModifyLabel.config(text="")
    statusSearchModifyLabel.config(text="")

    modifyFrame.pack_forget()
    mainFrame.pack()


def openModifyForm():
    mainFrame.pack_forget()

    modifyFrame.pack()
    modifyLabelTitle.pack()
    dniModifyLabel.pack()
    dniModifyEntry.pack()
    statusSearchModifyLabel.pack()
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
    statusModifyLabel.pack()
    backModifyToMainButton.pack()


def showTreballador():
    dni = dniShowEntry.get()
    showQuery = """for $treballador in //treballador
                    where $treballador/dni = '""" + dni + """'
                    return $treballador"""
    output = selectQuery(showQuery)

    resultShowText.delete('1.0', tk.END)
    resultShowText.insert('1.0', output)


def backShowToMain():
    showTreballadorFrame.pack_forget()
    dniShowEntry.delete(0, tk.END)
    resultShowText.delete('1.0', tk.END)
    mainFrame.pack()


def openShowForm():
    mainFrame.pack_forget()

    showTreballadorFrame.pack()
    showTreballadorLabelTitle.pack()
    dniShowLabel.pack()
    dniShowEntry.pack()
    searchShowTreballadorButton.pack()
    resultShowText.pack()
    backShowToMainButton.pack()


def showAllTreballadors():
    output = selectQuery("//treballador")
    resultShowAllText.delete('1.0', tk.END)
    resultShowAllText.insert('1.0', output)


def backShowAllToMain():
    showAllTreballadorsFrame.pack_forget()
    mainFrame.pack()


def openShowAllForm():
    mainFrame.pack_forget()

    resultShowAllText.delete('1.0', tk.END)

    showAllTreballadorsFrame.pack()
    showAllTreballadorsLabelTitle.pack()
    searchShowAllTreballadorsButton.pack()
    resultShowAllText.pack()
    backShowAllToMainButton.pack()


def assignSalaryToDepartment():
    # TODO
    try:
        departmentAssign = departmentAssignSalaryEntry.get()
        quantityAssign = float(quantityAssignSalaryEntry.get())

        asignQuery = """update replace //treballador[departament='""" + departmentAssign + """']/sou/text()
                        with '""" + str(quantityAssign) + """'"""
        if ferQuery(asignQuery):
            statusAssignSalaryToDepartmentLabel.config(text="Sou assignat correctament")

            departmentAssignSalaryEntry.delete(0, tk.END)
            quantityAssignSalaryEntry.delete(0, tk.END)
        else:
            statusAssignSalaryToDepartmentLabel.config(text="Alguna cosa ha fallat")
    except:
        statusAssignSalaryToDepartmentLabel.config(text="Alguna dada es incorrecta")


def backAssignSalaryToDepartmentToMain():
    assignSalaryToDepartmentFrame.pack_forget()
    departmentAssignSalaryEntry.delete(0, tk.END)
    quantityAssignSalaryEntry.delete(0, tk.END)
    mainFrame.pack()


def openAssignSalaryToDepartmentForm():
    mainFrame.pack_forget()

    assignSalaryToDepartmentFrame.pack()
    assignSalaryToDepartmentLabelTitle.pack()
    departmentAssignSalaryLabel.pack()
    departmentAssignSalaryEntry.pack()
    quantityAssignSalaryLabel.pack()
    quantityAssignSalaryEntry.pack()
    assignSalaryToDepartmentButton.pack()
    statusAssignSalaryToDepartmentLabel.pack()
    backAssignSalaryToDepartmentToMainButton.pack()


def increaseSalaryToDepartment():
    try:
        departamentIncrease = departmentIncreaseSalaryEntry.get()
        quantityIncrease = float(quantityIncreaseSalaryEntry.get())
        increareQuery = """for $treballador in //treballador
                            let $sou:=$treballador/sou
                            where $treballador/departament='"""+departamentIncrease+"""'
                            return (
                                update value $sou
                                with $sou+"""+str(quantityIncrease)+"""
                            )"""
        if ferQuery(increareQuery):
            statusIncreaseSalaryToDepartmentLabel.config(text="Sou augmentat correctament")
            departmentIncreaseSalaryEntry.delete(0, tk.END)
            quantityIncreaseSalaryEntry.delete(0, tk.END)
    except:
        statusIncreaseSalaryToDepartmentLabel.config(text="Alguna dada es incorrecta")

    pass


def backIncreaseSalaryToDepartmentToMain():
    increaseSalaryToDepartmentFrame.pack_forget()
    departmentIncreaseSalaryEntry.delete(0, tk.END)
    quantityIncreaseSalaryEntry.delete(0, tk.END)

    statusIncreaseSalaryToDepartmentLabel.config(text="")

    mainFrame.pack()


def openIncreaseSalaryToDepartmentForm():
    mainFrame.pack_forget()

    increaseSalaryToDepartmentFrame.pack()
    increaseSalaryToDepartmentLabelTitle.pack()
    departmentIncreaseSalaryLabel.pack()
    departmentIncreaseSalaryEntry.pack()
    quantityIncreaseSalaryLabel.pack()
    quantityIncreaseSalaryEntry.pack()
    increaseSalaryToDepartmentButton.pack()
    statusIncreaseSalaryToDepartmentLabel.pack()
    backIncreaseSalaryToDepartmentToMainButton.pack()


def exitForm():
    window.destroy()


# MAIN FORM
mainFrame = tk.Frame(window, padx=10, pady=50)
mainFrameLabelTitle = tk.Label(mainFrame, text="MENU PRINCIPAL", font="Helvetica 16 bold")
insertFormButton = tk.Button(mainFrame, text="INSERTAR TREBALLADOR", command=openInsertFrame)
deleteFormButton = tk.Button(mainFrame, text="ELIMINAR TREBALLADOR", command=openDeleteForm)
modifyFormButton = tk.Button(mainFrame, text="MODIFICAR TREBALLADOR", command=openModifyForm)
showFormButton = tk.Button(mainFrame, text="BUSCAR TREBALLADOR", command=openShowForm)
showAllFormButton = tk.Button(mainFrame, text="LLISTAR TREBALLADORS", command=openShowAllForm)
assignSalaryToDepartmentFormButton = tk.Button(mainFrame, text="ASSIGNAR SOU A UN DEPARTAMENT",
                                               command=openAssignSalaryToDepartmentForm)
increaseSalaryToDepartmentFormButton = tk.Button(mainFrame, text="AUGMENTAR SOU D'UN DEPARTAMENT",
                                                 command=openIncreaseSalaryToDepartmentForm)
exitFormButton = tk.Button(mainFrame, text="SORTIR", command=exitForm)

mainFrame.pack()
mainFrameLabelTitle.pack()
insertFormButton.pack()
deleteFormButton.pack()
modifyFormButton.pack()
showFormButton.pack()
showAllFormButton.pack()
assignSalaryToDepartmentFormButton.pack()
increaseSalaryToDepartmentFormButton.pack()
exitFormButton.pack()

# INSERT
insertFrame = tk.Frame(window, padx=10, pady=30)
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
statusInsertTreballadorLabel = tk.Label(insertFrame, text="")
backInsertToMainButton = tk.Button(insertFrame, text="MENU PRINCIPAL", command=backInsertToMain)

# DELETE
deleteFrame = tk.Frame(window, padx=10, pady=30)
deleteLabelTitle = tk.Label(deleteFrame, text="ELIMINAR TREBALLADOR", font="Helvetica 16 bold")
dniDeleteLabel = tk.Label(deleteFrame, text="DNI")
dniDeleteEntry = tk.Entry(deleteFrame)
deleteTreballadorButton = tk.Button(deleteFrame, text="ELIMINAR TREBALLADOR", command=deleteTreballador)
statusDeleteTreballadorLabel = tk.Label(deleteFrame, text="")
backDeleteToMainButton = tk.Button(deleteFrame, text="MENU PRINCIPAL", command=backDeleteToMain)

# MODIFY
modifyFrame = tk.Frame(window, padx=10, pady=30)
modifyLabelTitle = tk.Label(modifyFrame, text="MODIFICAR TREBALLADOR", font="Helvetica 16 bold")
dniModifyLabel = tk.Label(modifyFrame, text="DNI")
dniModifyEntry = tk.Entry(modifyFrame)
statusSearchModifyLabel = tk.Label(modifyFrame, text="")
searchModifyTreballadorButton = tk.Button(modifyFrame, text="BUSCAR", command=searchModifyTreballador)
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
statusModifyLabel = tk.Label(modifyFrame, text="")
backModifyToMainButton = tk.Button(modifyFrame, text="MENU PRINCIPAL", command=backModifyToMain)

# SHOW
showTreballadorFrame = tk.Frame(window, padx=10, pady=30)
showTreballadorLabelTitle = tk.Label(showTreballadorFrame, text="BUSCAR TREBALLADOR", font="Helvetica 16 bold")
dniShowLabel = tk.Label(showTreballadorFrame, text="DNI")
dniShowEntry = tk.Entry(showTreballadorFrame)
searchShowTreballadorButton = tk.Button(showTreballadorFrame, text="BUSCAR", command=showTreballador)
resultShowText = tk.Text(showTreballadorFrame, height="20", width="50")
backShowToMainButton = tk.Button(showTreballadorFrame, text="MENU PRINCIPAL", command=backShowToMain)

# SHOW ALL
showAllTreballadorsFrame = tk.Frame(window, padx=10, pady=30)
showAllTreballadorsLabelTitle = tk.Label(showAllTreballadorsFrame, text="LLISTA TREBALLADORS", font="Helvetica 16 bold")
searchShowAllTreballadorsButton = tk.Button(showAllTreballadorsFrame, text="LLISTAR", command=showAllTreballadors)
resultShowAllText = tk.Text(showAllTreballadorsFrame, height="20", width="50")
backShowAllToMainButton = tk.Button(showAllTreballadorsFrame, text="MENU PRINCIPAL", command=backShowAllToMain)

# ASSIGN SALARY TO DEPARTMENT
assignSalaryToDepartmentFrame = tk.Frame(window, padx=10, pady=30)
assignSalaryToDepartmentLabelTitle = tk.Label(assignSalaryToDepartmentFrame, text="ASSIGNAR SOU A UN DEPARTAMENT",
                                              font="Helvetica 16 bold")
departmentAssignSalaryLabel = tk.Label(assignSalaryToDepartmentFrame, text="DEPARTAMENT")
departmentAssignSalaryEntry = tk.Entry(assignSalaryToDepartmentFrame)
quantityAssignSalaryLabel = tk.Label(assignSalaryToDepartmentFrame, text="QUANTITAT")
quantityAssignSalaryEntry = tk.Entry(assignSalaryToDepartmentFrame)
assignSalaryToDepartmentButton = tk.Button(assignSalaryToDepartmentFrame, text="ASSIGNAR",
                                           command=assignSalaryToDepartment)
statusAssignSalaryToDepartmentLabel = tk.Label(assignSalaryToDepartmentFrame, text="")
backAssignSalaryToDepartmentToMainButton = tk.Button(assignSalaryToDepartmentFrame, text="MENU PRINCIPAL",
                                                     command=backAssignSalaryToDepartmentToMain)

# INCREASE SALARY TO DEPARTMENT
increaseSalaryToDepartmentFrame = tk.Frame(window, padx=10, pady=30)
increaseSalaryToDepartmentLabelTitle = tk.Label(increaseSalaryToDepartmentFrame, text="AUGMENTAR SOU A UN DEPARTAMENT",
                                                font="Helvetica 16 bold")
departmentIncreaseSalaryLabel = tk.Label(increaseSalaryToDepartmentFrame, text="DEPARTAMENT")
departmentIncreaseSalaryEntry = tk.Entry(increaseSalaryToDepartmentFrame)
quantityIncreaseSalaryLabel = tk.Label(increaseSalaryToDepartmentFrame, text="QUANTITAT")
quantityIncreaseSalaryEntry = tk.Entry(increaseSalaryToDepartmentFrame)
increaseSalaryToDepartmentButton = tk.Button(increaseSalaryToDepartmentFrame, text="AUGMENTAR",
                                             command=increaseSalaryToDepartment)
statusIncreaseSalaryToDepartmentLabel = tk.Label(increaseSalaryToDepartmentFrame, text="")
backIncreaseSalaryToDepartmentToMainButton = tk.Button(increaseSalaryToDepartmentFrame, text="MENU PRINCIPAL",
                                                       command=backIncreaseSalaryToDepartmentToMain)

window.mainloop()
