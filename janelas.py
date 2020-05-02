from routes.usuarios import Usuarios
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage

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

class JanelaCadastro():
    def __init__(self, master=None):

        # Atributos
        self.novoUsuario = StringVar()
        self.novaSenha = StringVar()

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
        self.entNovoUsuario = Entry(self.frmLogin, textvariable=self.novoUsuario, width=20)
        self.entNovoUsuario["font"] = self.fonteEntry
        self.entNovoUsuario["relief"] = "solid"
        self.entNovoUsuario["justify"] = CENTER

        # Criando ENT da Senha
        self.entNovaSenha = Entry(self.frmLogin, textvariable=self.novaSenha, show="*", width=20)
        self.entNovaSenha["font"] = self.fonteEntry
        self.entNovaSenha["relief"] = "solid"
        self.entNovaSenha["justify"] = CENTER

        # Criando BTN de Logar
        self.btnCadastro = Button(self.frmLogin, text="L O G I N", width=20, height=2)
        self.btnCadastro["font"] = self.fontePadrao
        self.btnCadastro["relief"] = "solid"
        self.btnCadastro["fg"] = "white"
        self.btnCadastro["bg"] = self.corFundo
        self.btnCadastro["activeforeground"] = "white"
        self.btnCadastro["activebackground"] = self.corFundo
        self.btnCadastro["command"] = self.iniciarProcedimento

        # Criando LBL de Divisor
        self.lblDivisor1 = Label(self.frmLogin, text="    ", bg=self.corContainer)
        self.lblDivisor2 = Label(self.frmLogin, text="    ", bg=self.corContainer)
        self.lblDivisor3 = Label(self.frmLogin, text="    ", bg=self.corContainer)
        self.lblDivisor4 = Label(self.frmLogin, text="    ", bg=self.corContainer)
        self.lblDivisor5 = Label(self.frmLogin, bg=self.corContainer)
        
        self.entNovoUsuario.grid(column=1, row=1)
        self.entNovaSenha.grid(column=1, row=2)
        self.btnCadastro.grid(column=1, row=4)

        self.lblDivisor1.grid(column=0, row=0)
        self.lblDivisor2.grid(column=2, row=0)
        self.lblDivisor3.grid(column=2, row=5)
        self.lblDivisor4.grid(column=0, row=5)
        self.lblDivisor5.grid(column=1, row=3)

    def iniciarProcedimento(self):
        pass

class JanelaLogin():
    def __init__(self, master=None):

        # Atributos
        self.master = master
        self.usuario = StringVar()
        self.senha = StringVar()

        # Varíaveis de apoio
        self.fontePadrao = ("Arial", "12", "bold")
        self.fonteEntry = ("Arial", "20")
        self.corFrente = "white"
        self.corFundo = "#54FF9F"
        self.corContainer = "#DCDCDC"

        # Chamando métodos
        self.criarFrames() # Chamando Frames para __init__

    def criarFrames(self):
        
        # Criando Frames (Containers)
        self.frmLogin = Frame(self.master, bd=5, relief=GROOVE, bg=self.corContainer)
        self.frmBotoes = Frame(self.master, bd=5, relief=GROOVE, bg=self.corContainer)

        # Empacotando Frames
        self.frmLogin.grid(column=1, row=5, padx=170)
        self.frmBotoes.grid(column=1, row=6)

        # Chamando métodos
        self.criarWidgets() # Chamando Widgets para Frames

    def criarWidgets(self):

        # Criando IMG do Usuário

        imgUsuario = PhotoImage(file="img/user-icon2.png")
        self.lblUsuario = Label(self.frmLogin, image=imgUsuario, bg=self.corContainer)
        self.lblUsuario.image = imgUsuario

        # Criando ENT do Usuário
        self.entUsuario = Entry(self.frmLogin, textvariable=self.usuario, width=10)
        self.entUsuario["font"] = self.fonteEntry
        self.entUsuario["relief"] = SOLID
        self.entUsuario["justify"] = CENTER

        # Criando IMG da Senha

        imgSenha = PhotoImage(file="img/password-icon2.png")
        self.lblSenha = Label(self.frmLogin, image=imgSenha, bg=self.corContainer)
        self.lblSenha.image = imgSenha

        # Criando ENT da Senha
        self.entSenha = Entry(self.frmLogin, textvariable=self.senha, show="*", width=10)
        self.entSenha["font"] = self.fonteEntry
        self.entSenha["relief"] = SOLID
        self.entSenha["justify"] = CENTER

        # Criando BTN de Logar
        self.btnLogin = Button(self.frmLogin, text="L O G I N", width=20, height=2)
        self.btnLogin["font"] = self.fontePadrao
        self.btnLogin["relief"] = RAISED
        self.btnLogin["fg"] = self.corFrente
        self.btnLogin["bg"] = self.corFundo
        self.btnLogin["activeforeground"] = self.corFrente
        self.btnLogin["activebackground"] = self.corFundo
        self.btnLogin["command"] = self.iniciarProcedimento

        self.lblCadastrar = Label(self.frmLogin, text="Cadastrar", cursor="hand2")
        self.lblCadastrar["font"] = self.fontePadrao
        self.lblCadastrar["bg"] = self.corContainer
        self.lblCadastrar["command"] = self.irCadastro

        # Criando BTN de Voltar

        self.btnVoltar = Button(self.frmBotoes, text="Voltar", width=10, height=1)
        self.btnVoltar["font"] = self.fontePadrao
        self.btnVoltar["relief"] = GROOVE
        self.btnVoltar["fg"] = self.corFrente
        self.btnVoltar["bg"] = self.corFundo
        self.btnVoltar["activeforeground"] = self.corFrente
        self.btnVoltar["activebackground"] = self.corFundo
        self.btnVoltar["command"] = self.voltarJanela

        self.btnCadastrar = Button(self.frmBotoes, text="Cadastrar", width=10, height=1)
        self.btnCadastrar["font"] = self.fontePadrao
        self.btnCadastrar["relief"] = GROOVE
        self.btnCadastrar["fg"] = self.corFrente
        self.btnCadastrar["bg"] = self.corFundo
        self.btnCadastrar["activeforeground"] = self.corFrente
        self.btnCadastrar["activebackground"] = self.corFundo
        self.btnCadastrar["command"] = self.irCadastro

        # Criando LBL de Divisor
        self.lblDivisor1 = Label(self.frmLogin, text="    ", bg=self.corContainer)
        self.lblDivisor2 = Label(self.frmLogin, text="    ", bg=self.corContainer)
        self.lblDivisor3 = Label(self.frmLogin, text="    ", bg=self.corContainer)
        self.lblDivisor4 = Label(self.frmLogin, text="    ", bg=self.corContainer)
        
        self.lblUsuario.grid(column=1, row=1, sticky=W, pady=5)
        self.entUsuario.grid(column=1, row=1, sticky=E)
        self.lblSenha.grid(column=1, row=2, sticky=W, pady=5)
        self.entSenha.grid(column=1, row=2, stick=E)
        self.btnLogin.grid(column=1, row=4, pady=10)
        self.btnVoltar.grid(column=0, row=0, padx=6, pady=5)
        self.btnCadastrar.grid(column=1, row=0, padx=6, pady=5)

        self.lblDivisor1.grid(column=0, row=0)
        self.lblDivisor2.grid(column=2, row=0)
        self.lblDivisor3.grid(column=2, row=5)
        self.lblDivisor4.grid(column=0, row=5)

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
            principal = JanelaPrincipal()

        else:
            messagebox.showwarning("Login", verificacao)

    def voltarJanela(self):

        self.frmLogin.grid_forget()

        self.lblUsuario.grid_forget()
        self.entUsuario.grid_forget()
        self.lblSenha.grid_forget()
        self.entSenha.grid_forget()
        self.btnLogin.grid_forget()
        self.btnVoltar.grid_forget()
        self.btnCadastrar.grid_forget()

        self.lblDivisor1.grid_forget()
        self.lblDivisor2.grid_forget()
        self.lblDivisor3.grid_forget()
        self.lblDivisor4.grid_forget()

        inicial = JanelaInicial()

    def irCadastro(self):
        
        self.frmLogin.grid_forget()

        self.lblUsuario.grid_forget()
        self.entUsuario.grid_forget()
        self.lblSenha.grid_forget()
        self.entSenha.grid_forget()
        self.btnLogin.grid_forget()
        self.btnVoltar.grid_forget()
        self.btnCadastrar.grid_forget()

        self.lblDivisor1.grid_forget()
        self.lblDivisor2.grid_forget()
        self.lblDivisor3.grid_forget()
        self.lblDivisor4.grid_forget()

        cadastro = JanelaCadastro()

class JanelaInicial():
    def __init__(self, master=None):
        
        self.master = master

        # Varíaveis de apoio
        self.fontePadrao = ("Arial", "12", "bold")
        self.fonteEntry = ("Arial", "20")
        self.corFundo = "#54FF9F"
        self.corContainer = "#DCDCDC"

        self.criarFrames()

    def criarFrames(self):
        
        # Criando Frames (Containers)
        self.frmInicial = Frame(self.master, bd=3, relief=GROOVE, bg=self.corContainer)

        # Empacotando Frames
        self.frmInicial.grid(column=1, row=5, padx=170, pady=150)

        # Chamando métodos
        self.criarWidgets() # Chamando Widgets para Frames

    def criarWidgets(self):

        # Criando BTN de Login
        self.btnLogin = Button(self.frmInicial, text="L O G I N", width=20, height=2)
        self.btnLogin["font"] = self.fontePadrao
        self.btnLogin["relief"] = SOLID
        self.btnLogin["fg"] = "white"
        self.btnLogin["bg"] = self.corFundo
        self.btnLogin["activeforeground"] = "white"
        self.btnLogin["activebackground"] = self.corFundo
        self.btnLogin["command"] = self.mudarLogin
        
        # Criando BTN de Login
        self.btnCadastro = Button(self.frmInicial, text="C A D A S T R O", width=20, height=2)
        self.btnCadastro["font"] = self.fontePadrao
        self.btnCadastro["relief"] = SOLID
        self.btnCadastro["fg"] = "white"
        self.btnCadastro["bg"] = self.corFundo
        self.btnCadastro["activeforeground"] = "white"
        self.btnCadastro["activebackground"] = self.corFundo
        self.btnCadastro["command"] = self.mudarCadastro

        self.btnSair = Button(self.frmInicial, text="S A I R", width=10, height=1)
        self.btnSair["font"] = self.fontePadrao
        self.btnSair["relief"] = RAISED
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

        self.btnLogin.grid(column=1, row=1, pady=5)
        self.btnCadastro.grid(column=1, row=2)
        self.btnSair.grid(column=1, row=4)

        self.lblDivisor1.grid(column=0, row=0)
        self.lblDivisor2.grid(column=2, row=0)
        self.lblDivisor3.grid(column=2, row=5)
        self.lblDivisor4.grid(column=0, row=5)
        self.lblDivisor5.grid(column=1, row=3)

    def iniciarProcedimento(self):
        pass

    def mudarLogin(self):

        # Desempacotando Widgets da Janela Inicial
        self.frmInicial.grid_forget()
        self.btnLogin.grid_forget()
        self.btnCadastro.grid_forget()
        self.btnSair.grid_forget()

        self.lblDivisor1.grid_forget()
        self.lblDivisor2.grid_forget()
        self.lblDivisor3.grid_forget()
        self.lblDivisor4.grid_forget()
        self.lblDivisor5.grid_forget()

        login = JanelaLogin()

    def mudarCadastro(self):

        # Desempacotando Widgets da Janela Inicial
        self.frmInicial.grid_forget()
        self.btnLogin.grid_forget()
        self.btnCadastro.grid_forget()
        self.btnSair.grid_forget()

        self.lblDivisor1.grid_forget()
        self.lblDivisor2.grid_forget()
        self.lblDivisor3.grid_forget()
        self.lblDivisor4.grid_forget()
        self.lblDivisor5.grid_forget()

        cadastro = JanelaCadastro()

if __name__ == "__main__":
    root = Tk()
    root.resizable(width=False, height=False)
    root.geometry("600x600")
    root.title("Gerenciador de Fichas")
    root["bg"] = "#54FF9F"
    
    programa = JanelaInicial(root)
    root.mainloop()