from routes.usuarios import Usuarios
from tkinter import *
from tkinter import messagebox

class JanelaFicha():
    def __init__(self, master=None):
        pass

    def criarFrames(self):
        pass

    def criarWidgets(self):
        pass

    def iniciarProcedimento(self):
        pass

class JanelaDelecao():
    def __init__(self, master=None):
        pass

    def criarFrames(self):
        pass

    def criarWidgets(self):
        pass

    def iniciarProcedimento(self):
        pass

class JanelaAlteracao():
    def __init__(self, master=None):
        pass

    def criarFrames(self):
        pass

    def criarWidgets(self):
        pass

    def iniciarProcedimento(self):
        pass

class JanelaCriacao():
    def __init__(self, master=None):
        pass

    def criarFrames(self):
        pass

    def criarWidgets(self):
        pass

    def iniciarProcedimento(self):
        pass

class JanelaPrincipal():
    def __init__(self, master=None):
        pass

    def criarFrames(self):
        pass

    def criarWidgets(self):
        pass

    def iniciarProcedimento(self):
        pass

class JanelaCadastro(Toplevel):
    def __init__(self, master=None):
        pass

    def criarFrames(self, master):
        pass

    def criarWidgets(self):
        pass

    def iniciarProcedimento(self):
        pass

class JanelaLogin(Toplevel):
    def __init__(self, master=None):

        # Atributos
        self.usuario = StringVar()
        self.senha = StringVar()

        # Varíaveis de apoio
        self.fontePadrao = ("Arial", "12", "bold")
        self.fonteEntry = ("Arial", "20")
        self.corFundo = "#8B0000"
        self.corContainer = "#DCDCDC"

        # Chamando métodos
        self.criarFrames(master) # Chamando Frames para __init__

    def criarFrames(self, master):
        
        # Criando Frames (Containers)
        self.frmDivisor = Frame(master, width=100, height=100, bg=self.corFundo)
        self.frmLogin = Frame(master, bd=3, relief="groove", bg=self.corContainer)

        # Empacotando Frames
        self.frmDivisor.grid(column=0, row=1)
        self.frmLogin.grid(column=1, row=5)

        # Chamando métodos
        self.criarWidgets() # Chamando Widgets para Frames

    def criarWidgets(self):

        # Criando ENT do Usuário
        self.entUsuario = Entry(self.frmLogin, textvariable=self.usuario, width=20)
        self.entUsuario["font"] = self.fonteEntry
        self.entUsuario["relief"] = "solid"
        self.entUsuario["justify"] = CENTER

        # Criando ENT da Senha
        self.entSenha = Entry(self.frmLogin, textvariable=self.senha, show="*", width=20)
        self.entSenha["font"] = self.fonteEntry
        self.entSenha["relief"] = "solid"
        self.entSenha["justify"] = CENTER

        # Criando BTN de Logar
        self.btnLogin = Button(self.frmLogin, text="L O G I N", width=20, height=2)
        self.btnLogin["font"] = self.fontePadrao
        self.btnLogin["relief"] = "solid"
        self.btnLogin["fg"] = "white"
        self.btnLogin["bg"] = self.corFundo
        self.btnLogin["activeforeground"] = "white"
        self.btnLogin["activebackground"] = self.corFundo
        self.btnLogin["command"] = self.iniciarProcedimento

        # Criando LBL de Divisor
        self.lblDivisor1 = Label(self.frmLogin, text="    ", bg=self.corContainer)
        self.lblDivisor2 = Label(self.frmLogin, text="    ", bg=self.corContainer)
        self.lblDivisor3 = Label(self.frmLogin, text="    ", bg=self.corContainer)
        self.lblDivisor4 = Label(self.frmLogin, text="    ", bg=self.corContainer)
        self.lblDivisor5 = Label(self.frmLogin, bg=self.corContainer)
        
        self.entUsuario.grid(column=1, row=1)
        self.entSenha.grid(column=1, row=2)
        self.btnLogin.grid(column=1, row=4)

        self.lblDivisor1.grid(column=0, row=0)
        self.lblDivisor2.grid(column=2, row=0)
        self.lblDivisor3.grid(column=2, row=5)
        self.lblDivisor4.grid(column=0, row=5)
        self.lblDivisor5.grid(column=1, row=3)

    def iniciarProcedimento(self):

        login = Usuarios()

        usuario = self.usuario.get()
        senha = self.senha.get()

        usuario = usuario.lower()

        login.usuario = usuario
        login.senha = senha
        
        print("Evento de Login - OK")
        print(login.usuario)
        print(login.senha + "\n")

        verificacao = login.autenticarUsuario()
        
        if verificacao == True:
            pass

        else:
            messagebox.showwarning("Login", verificacao)

class JanelaInicial():
    def __init__(self, master=None):
        
        self.master = master

        # Varíaveis de apoio
        self.fontePadrao = ("Arial", "12", "bold")
        self.fonteEntry = ("Arial", "20")
        self.corFundo = "#8B0000"
        self.corContainer = "#DCDCDC"

        self.criarFrames()

    def criarFrames(self):
        
        # Criando Frames (Containers)
        self.frmInicial = Frame(self.master, bd=3, relief="groove", bg=self.corContainer)

        # Empacotando Frames
        self.frmInicial.grid(column=1, row=5, padx=150, pady=150)

        # Chamando métodos
        self.criarWidgets() # Chamando Widgets para Frames

    def criarWidgets(self):

        # Criando BTN de Login
        self.btnLogin = Button(self.frmInicial, text="L O G I N", width=20, height=2)
        self.btnLogin["font"] = self.fontePadrao
        self.btnLogin["relief"] = "solid"
        self.btnLogin["fg"] = "white"
        self.btnLogin["bg"] = self.corFundo
        self.btnLogin["activeforeground"] = "white"
        self.btnLogin["activebackground"] = self.corFundo
        #self.btnLogin["command"] = self.iniciarProcedimento() 

        # Criando BTN de Login
        self.btnCadastro = Button(self.frmInicial, text="C A D A S T R O", width=20, height=2)
        self.btnCadastro["font"] = self.fontePadrao
        self.btnCadastro["relief"] = "solid"
        self.btnCadastro["fg"] = "white"
        self.btnCadastro["bg"] = self.corFundo
        self.btnCadastro["activeforeground"] = "white"
        self.btnCadastro["activebackground"] = self.corFundo
        #self.btnCadastro["command"] = self.iniciarProcedimento()

        self.btnSair = Button(self.frmInicial, text="S A I R", width=10, height=2)
        self.btnSair["font"] = self.fontePadrao
        self.btnSair["relief"] = "solid"
        self.btnSair["fg"] = "white"
        self.btnSair["bg"] = self.corFundo
        self.btnSair["activeforeground"] = "white"
        self.btnSair["activebackground"] = self.corFundo
        self.btnSair["command"] = lambda: exit()
        
        # Criando LBL de Divisor
        self.lblDivisor1 = Label(self.frmInicial, text="    ", bg=self.corContainer)
        self.lblDivisor2 = Label(self.frmInicial, text="    ", bg=self.corContainer)
        self.lblDivisor3 = Label(self.frmInicial, text="    ", bg=self.corContainer)
        self.lblDivisor4 = Label(self.frmInicial, text="    ", bg=self.corContainer)
        self.lblDivisor5 = Label(self.frmInicial, bg=self.corContainer)

        self.btnLogin.grid(column=1, row=1)
        self.btnCadastro.grid(column=1, row=2)
        self.btnSair.grid(column=1, row=4)

        self.lblDivisor1.grid(column=0, row=0)
        self.lblDivisor2.grid(column=2, row=0)
        self.lblDivisor3.grid(column=2, row=5)
        self.lblDivisor4.grid(column=0, row=5)
        self.lblDivisor5.grid(column=1, row=3)

    def iniciarProcedimento(self):
        
        self.login = JanelaLogin()
        self.cadastro = JanelaCadastro()

if __name__ == "__main__":
    root = Tk()
    root.resizable(width=False, height=False)
    root.geometry("600x600")
    root.title("Gerenciador de Fichas")
    root["bg"] = "#8B0000"
    
    programa = JanelaInicial(root)
    root.mainloop()