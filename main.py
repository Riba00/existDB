from eulexistdb import db

import Tkinter as tk

EXISTDB_SERVER_USER = 'admin'
EXISTDB_SERVER_PASSWORD = 'Admin12345'
EXISTDB_SERVER_URL = "http://localhost:8080/exist"
EXISTDB_ROOT_COLLECTION = "/MP03UF6"

db = db.ExistDB(server_url=EXISTDB_SERVER_URL, username='admin', password='Admin12345')


def ferQuery():
    try:
        resultText.delete('1.0','end')
        sortida = ""
        res = db.executeQuery(xPathText.get('1.0','end'))
        hits = db.getHits(res)
        for i in range(hits):
            sortida = sortida + str(db.retrieve(res, i)) + '\n'

        resultText.insert('1.0', sortida)
    except:
        resultText.insert('1.0', "Expressio incorrecta")

# WINDOW SETTINGS
window = tk.Tk()
window.title("Riba xPath")
window.geometry("500x800")




xPathLabel = tk.Label(master=window, text="xPath experssion: ", width="50")
xPathText = tk.Text(master=window, height="2", width="40")
queryButton = tk.Button(master=window, text="Consultar", command=ferQuery)
resultText = tk.Text(window, height="40", width="50")



# PACK
xPathLabel.pack()
xPathText.pack(pady="10")
queryButton.pack()
resultText.pack()

window.mainloop()
