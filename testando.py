from routes.estilo import Estilo

from tkinter import *
from tkinter import ttk

class JanelaInicial():
    def __init__(self, master=None):
        self.master = master

        Estilo.__init__(self)

        self.criarWidgets()
    
    def criarWidgets(self):
        
        self.abas = ttk.Notebook(self.master)

        self.frmMensagem = Frame(self.master)

        self.frmRacas = ttk.Frame(self.abas)
        self.frmClasses = ttk.Frame(self.abas)
        self.frmDeuses = ttk.Frame(self.abas)

        self.frmRacas.grid()
        self.frmClasses.grid()
        self.frmDeuses.grid()

        self.abas.add(self.frmRacas, text="Raças")
        self.abas.add(self.frmClasses, text="Classes")
        self.abas.add(self.frmDeuses, text="Deuses")

        self.lblSemideus = Label(self.frmRacas, text="Semideus", cursor="question_arrow")
        self.lblLegado = Label(self.frmRacas, text="Legado", cursor="question_arrow")

        self.lblJupiter = Label(self.frmDeuses, text="Júpiter")
        self.lblMarte = Label(self.frmDeuses, text="Marte")
        self.lblNetuno = Label(self.frmDeuses, text="Netuno")

        self.lblSemideus.grid()
        self.lblLegado.grid()

        self.lblJupiter.grid()
        self.lblMarte.grid()
        self.lblNetuno.grid()

        self.abas.grid(column=0, row=0)

        self.lblMensagem = Label(self.frmMensagem, text="Testando", fg=self.corFrente, bg=self.corFundo)

        self.frmMensagem.grid(column=1, row=1)
        self.lblMensagem.grid()
        
        self.lblSemideus.bind("<Enter>", lambda msgSemideus: self.mensagem("Semideus é uma raça com origem no cruzamento de um Deus com um Humano"))
        self.lblLegado.bind("<Enter>", lambda msgLegado: self.mensagem("Legado é uma raça com origem no cruzamento de um Semideus com um Humano"))

    def mensagem(self, msg):

        self.lblMensagem["text"] = msg

if __name__ == "__main__":
    root = Tk()
    root.iconbitmap("img/spqr-icon.ico")
    root.resizable(width=False, height=False)
    root.geometry("600x600")
    root.title("Gerenciador de Fichas")
    root["bg"] = "#330c50"
    
    programa = JanelaInicial(root)
    root.mainloop()