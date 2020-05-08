from tkinter import *
from tkinter import ttk

class JanelaInicial():
    def __init__(self, master=None):
        self.master = master
        self.criarWidgets()
    
    def criarWidgets(self):
        
        self.abas = ttk.Notebook(self.master)

        self.frmMensagem = Frame(self.master)

        self.racas = ttk.Frame(self.abas)
        self.classes = ttk.Frame(self.abas)
        self.deuses = ttk.Frame(self.abas)

        self.racas.grid()
        self.classes.grid()
        self.deuses.grid()

        self.abas.add(self.racas, text="Raças")
        self.abas.add(self.classes, text="Classes")
        self.abas.add(self.deuses, text="Deuses")

        
        self.lblSemideus = Label(self.racas, text="Semideus")
        self.lblFauno = Label(self.racas, text="Fauno")
        self.lblLegado = Label(self.racas, text="Legado")

        self.lblSemideus.grid()
        self.lblFauno.grid()
        self.lblLegado.grid()

        self.abas.grid(column=0, row=0)

        self.lblMensagem = Label(self.frmMensagem, text="Testando")
        self.frmMensagem.grid(column=1, row=0)
        self.lblMensagem.grid()
        
        self.lblSemideus.bind("<Enter>", lambda msgSemideuses: self.mensagemSemideuses())

    def mensagemSemideuses(self):
        self.lblMensagem["text"] = "Semideuses"

if __name__ == "__main__":
    root = Tk()
    root.iconbitmap("img/spqr-icon.ico")
    root.resizable(width=False, height=False)
    root.geometry("600x600")
    root.title("Gerenciador de Fichas")
    root["bg"] = "#330c50"
    
    programa = JanelaInicial(root)
    root.mainloop()