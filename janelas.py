from routes.usuarios import Usuarios
from routes.estilo import Estilo
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import ttk

class JanelaFicha():
    def __init__(self, master=None):
        
        # Atributos
        self.master = master

        # Lista de estilo
        Estilo.__init__(self)

        self.criarWidgets()

    def criarWidgets(self):
        pass

    def iniciarProcedimento(self):
        pass

class JanelaDelecao():
    def __init__(self, master=None):
        
        # Atributos
        self.master = master

        # Lista de estilo
        Estilo.__init__(self)

        self.criarWidgets()

    def criarWidgets(self):
        pass

    def iniciarProcedimento(self):
        pass

class JanelaAlteracao():
    def __init__(self, master=None):
        
        # Atributos
        self.master = master

        # Lista de estilo
        Estilo.__init__(self)

        self.criarWidgets()

    def criarWidgets(self):
        pass

    def iniciarProcedimento(self):
        pass

class JanelaCriacao():
    def __init__(self, master=None):

        # Atributos
        self.master = master

        # Lista de estilo
        Estilo.__init__(self)

        self.criarWidgets()

    def criarWidgets(self):
        pass

    def iniciarProcedimento(self):
        pass

class JanelaPrincipal():
    def __init__(self, master=None):
        
        # Atributos
        self.master = master

        # Lista de estilo
        Estilo.__init__(self)

        self.criarWidgets()

    def criarWidgets(self):
        
        self.frmLogo = Frame(self.master, bg=self.corFundo)
        self.frmBarra = Frame(self.master, bg=self.corFundo)
        self.frmMensagem = Frame(self.master, bg=self.corFundo)

         # Criando IMG de Logo
        imgLogo = PhotoImage(file="img/spqr.png")
        self.lblLogo = Label(self.frmLogo, image=imgLogo, bg=self.corFundo)
        self.lblLogo.image = imgLogo

        self.btnCriacao = Button(self.frmBarra, text="Criar", cursor="hand2", width=10, height=1)
        self.btnCriacao["font"] = self.fontePadrao
        self.btnCriacao["relief"] = RIDGE
        self.btnCriacao["fg"] = self.corFundo
        self.btnCriacao["bg"] = self.corFrente
        self.btnCriacao["activeforeground"] = self.corFundo
        self.btnCriacao["activebackground"] = self.corFrente
        self.btnCriacao["command"] = self.irCriacao

        self.btnAlteracao = Button(self.frmBarra, text="Alterar", cursor="hand2", width=10, height=1)
        self.btnAlteracao["font"] = self.fontePadrao
        self.btnAlteracao["relief"] = RIDGE
        self.btnAlteracao["fg"] = self.corFundo
        self.btnAlteracao["bg"] = self.corFrente
        self.btnAlteracao["activeforeground"] = self.corFundo
        self.btnAlteracao["activebackground"] = self.corFrente
        self.btnAlteracao["command"] = self.irAlteracao

        self.btnDelecao = Button(self.frmBarra, text="Deletar", cursor="hand2", width=10, height=1)
        self.btnDelecao["font"] = self.fontePadrao
        self.btnDelecao["relief"] = RIDGE
        self.btnDelecao["fg"] = self.corFundo
        self.btnDelecao["bg"] = self.corFrente
        self.btnDelecao["activeforeground"] = self.corFundo
        self.btnDelecao["activebackground"] = self.corFrente
        self.btnDelecao["command"] = self.irDelecao

        self.lblMensagem = Label(self.frmMensagem, text="teste")
        self.lblMensagem["font"] = self.fontePadrao
        self.lblMensagem["justify"] = CENTER
        self.lblMensagem["fg"] = self.corFrente
        self.lblMensagem["bg"] = self.corFundo
        self.lblMensagem["activeforeground"] = self.corFrente
        self.lblMensagem["activebackground"] = self.corFundo

        # Empacotando widgets de FRM
        self.frmLogo.grid(column=0, row=0, padx=180, pady=10)
        self.frmBarra.grid(column=0, row=1, pady=10)
        self.frmMensagem.grid(column=0, row=2)

        self.lblLogo.grid(column=0, row=0)
        self.btnCriacao.grid(column=0, row=0, padx=5)
        self.btnAlteracao.grid(column=1, row=0, padx=5)
        self.btnDelecao.grid(column=2, row=0, padx=5)
        self.lblMensagem.grid()

        self.btnCriacao.bind("<Enter>", lambda msgCriar: self.mensagemCriacao())
        self.btnAlteracao.bind("<Enter>", lambda msgAlterar: self.mensagemAlteracao())
        self.btnDelecao.bind("<Enter>", lambda msgDeletar: self.mensagemDelecao())

    def mensagemCriacao(self):

        self.lblMensagem["text"] = "Clique para criar uma ficha"

    def mensagemAlteracao(self):

        self.lblMensagem["text"] = "Clique para alterar uma ficha"

    def mensagemDelecao(self):

        self.lblMensagem["text"] = "Clique para deletar uma ficha"


    def irCriacao(self):
        
        self.limparJanela()

        # Chamando a class JanelaCriacao
        criacao = JanelaCriacao()

    def irAlteracao(self):

        self.limparJanela()

        # Chamando a class JanelaCriacao
        criacao = JanelaCriacao()

    def irDelecao(self):
        
        self.limparJanela()
        
        delecao = JanelaDelecao()

    def irHistorico(self):
        pass

    def limparJanela(self):

        # Desempacotando widgets de FRM
        self.frmLogo.grid_forget()
        self.frmBarra.grid_forget()
        self.frmMensagem.grid_forget()

        # Desempacontando widgets de LBL e BTN
        self.lblLogo.grid_forget()
        self.btnCriacao.grid_forget()
        self.btnAlteracao.grid_forget()
        self.btnDelecao.grid_forget()
        self.lblMensagem.grid_forget()

class JanelaAjuda():
    def __init__(self, master=None):
        
        # Atributos
        self.master = master

        # Lista de estilo
        Estilo.__init__(self)

        self.criarWidgets()
    
    def criarWidgets(self):
        pass

class JanelaSobre():
    def __init__(self, master=None):

        # Atributos
        self.master = master

        # Lista de estilo
        Estilo.__init__(self)

        self.criarWidgets()

    def criarWidgets(self):

        self.barra = Frame(self.master)
        self.barra.grid(column=0)
        
        self.btnHistoria = Button(self.barra)
        self.btnRacas = Button(self.barra)
        self.btnClasses = Button(self.barra)

        self.btnHistoria.grid(column=0)
        self.btnRacas.grid(column=1)
        self.btnClasses.grid(column=2)

    def iniciarProcedimento(self):
        pass

class JanelaCadastro():
    def __init__(self):
        
        # Atributos
        self.cadastro = Toplevel()
        self.janela = []
        self.usuario = StringVar()
        self.senha = StringVar()
        self.senha2 = StringVar()

        # Lista de estilo
        Estilo.__init__(self)

        # Modificação
        self.janela.append(self.cadastro)

        self.configurarJanela()

    def configurarJanela(self):

        self.cadastro.iconbitmap("img/spqr-icon.ico")
        self.cadastro.resizable(width=False, height=False)
        self.cadastro.protocol('WM_DELETE_WINDOW', self.sairCadastro)
        self.cadastro.title("< SPQR > Gerenciador de Fichas")
        self.cadastro.geometry("300x300+650+200")
        self.cadastro["bg"] = "#330c50"

        self.criarWidgets()

    def criarWidgets(self):
        
        self.lblUsuario = Label(self.cadastro, text="Usuário")
        self.lblUsuario["font"] = self.fontePadrao
        self.lblUsuario["fg"] = self.corFrente
        self.lblUsuario["bg"] = self.corFundo

        # Criando ENT do Usuário
        self.entUsuario = Entry(self.cadastro, textvariable=self.usuario, width=20)
        self.entUsuario["relief"] = RIDGE
        self.entUsuario["justify"] = CENTER

        # Criando ENT da Senha 1
        self.lblSenha1 = Label(self.cadastro, text="Senha")
        self.lblSenha1["font"] = self.fontePadrao
        self.lblSenha1["fg"] = self.corFrente
        self.lblSenha1["bg"] = self.corFundo

        self.entSenha1 = Entry(self.cadastro, textvariable=self.senha, show="*", width=20)
        self.entSenha1["relief"] = RIDGE
        self.entSenha1["justify"] = CENTER

        # Criando ENT da Senha 2
        self.lblSenha2 = Label(self.cadastro, text="Repita a Senha")
        self.lblSenha2["font"] = self.fontePadrao
        self.lblSenha2["fg"] = self.corFrente
        self.lblSenha2["bg"] = self.corFundo

        self.entSenha2 = Entry(self.cadastro, textvariable=self.senha2, show="*", width=20)
        self.entSenha2["relief"] = RIDGE
        self.entSenha2["justify"] = CENTER

        # Criando BTN de Logar
        self.btnCadastro = Button(self.cadastro, text="Cadastro", cursor="hand2", width=10, height=1)
        self.btnCadastro["font"] = self.fontePadrao
        self.btnCadastro["relief"] = RIDGE
        self.btnCadastro["fg"] = self.corFundo
        self.btnCadastro["bg"] = self.corFrente
        self.btnCadastro["activeforeground"] = self.corFundo
        self.btnCadastro["activebackground"] = self.corFrente
        self.btnCadastro["command"] = self.cadastrarUsuario

        self.lblMensagem = Label(self.cadastro, text="Preencha o formulário")
        self.lblMensagem["font"] = self.fontePadrao
        self.lblMensagem["fg"] = self.corFrente
        self.lblMensagem["bg"] = self.corFundo
        self.lblMensagem["activeforeground"] = self.corFrente
        self.lblMensagem["activebackground"] = self.corFundo

        self.lblUsuario.grid(column=0, row=0, pady=10, padx=120)
        self.entUsuario.grid(column=0, row=1)
        self.lblSenha1.grid(column=0, row=2, pady=10)
        self.entSenha1.grid(column=0, row=3, padx=20)
        self.lblSenha2.grid(column=0, row=4, pady=10)
        self.entSenha2.grid(column=0, row=5, padx=20)
        self.btnCadastro.grid(column=0, row=6, pady=20)
        self.lblMensagem.grid(column=0, row=7)

    def sairCadastro(self):
        self.cadastro.destroy()
        self.cadastro.update()
    
    def cadastrarUsuario(self):
        
        cadastro = Usuarios()

        novoUsuario = self.usuario.get()
        novaSenha = self.senha.get()
        confirmaSenha = self.senha2.get()

        novoUsuario = novoUsuario.lower()

        if novaSenha != confirmaSenha:
            self.lblMensagem["text"] = "Senha incorreta!"

        else:

            cadastro.usuario = novoUsuario
            cadastro.senha = novaSenha

            print(cadastro.usuario)
            print(cadastro.senha)

            retorno = cadastro.cadastrarUsuario()

            if retorno != "Conta criada!":

                self.lblMensagem["text"] = retorno

            else:
                messagebox.showwarning("Cadastro", retorno)

class JanelaLogin():
    def __init__(self, master=None):

        # Atributos
        self.master = master
        self.usuario = StringVar()
        self.senha = StringVar()

        # Lista de estilo
        Estilo.__init__(self)

        # Chamando métodos
        self.criarWidgets() # Chamando widgets

    def criarWidgets(self):

        # Criando Frames
        self.frmLogo = Frame(self.master, bg=self.corFundo)
        self.frmLogin = Frame(self.master, bd=5, relief=RIDGE, bg=self.corContainer)
        self.frmBarra = Frame(self.master, bg=self.corFundo)

        # Criando IMG de Logo
        imgLogo = PhotoImage(file="img/spqr.png")
        self.lblLogo = Label(self.frmLogo, image=imgLogo, bg=self.corFundo)
        self.lblLogo.image = imgLogo

        # Criando IMG de Usuário
        imgUsuario = PhotoImage(file="img/user-icon2.png")
        self.lblUsuario = Label(self.frmLogin, image=imgUsuario, bg=self.corContainer)
        self.lblUsuario.image = imgUsuario

        # Criando ENT de Usuário
        self.entUsuario = Entry(self.frmLogin, bd=5, textvariable=self.usuario, width=10)
        self.entUsuario["font"] = self.fonteEntry
        self.entUsuario["relief"] = RIDGE
        self.entUsuario["justify"] = CENTER

        # Criando IMG de Senha
        imgSenha = PhotoImage(file="img/password-icon2.png")
        self.lblSenha = Label(self.frmLogin, image=imgSenha, bg=self.corContainer)
        self.lblSenha.image = imgSenha

        # Criando ENT de Senha
        self.entSenha = Entry(self.frmLogin, bd=5, textvariable=self.senha, show="*", width=10)
        self.entSenha["font"] = self.fonteEntry
        self.entSenha["relief"] = RIDGE
        self.entSenha["justify"] = CENTER

        # Criando BTN de Login
        self.btnLogin = Button(self.frmLogin, bd=5, text="LOGIN", cursor="hand2", width=20, height=2)
        self.btnLogin["font"] = self.fontePadrao
        self.btnLogin["relief"] = RIDGE
        self.btnLogin["fg"] = self.corFrente
        self.btnLogin["bg"] = self.corFundo
        self.btnLogin["activeforeground"] = self.corFrente
        self.btnLogin["activebackground"] = self.corFundo
        self.btnLogin["command"] = self.logarUsuario

        # Criando BTN de Cadastrar
        self.lblMensagem = Label(self.frmLogin, text="Cadastre-se", cursor="hand2")
        self.lblMensagem["font"] = self.fontePadrao
        self.lblMensagem["fg"] = self.corFundo
        self.lblMensagem["bg"] = self.corContainer
        self.lblMensagem["activeforeground"] = self.corFundo
        self.lblMensagem["activebackground"] = self.corContainer

        # Criando LBL de Voltar
        self.lblVoltar = Label(self.frmBarra, text="Voltar ao início", cursor="hand2")
        self.lblVoltar["font"] = self.fontePadrao
        self.lblVoltar["fg"] = self.corFrente
        self.lblVoltar["bg"] = self.corFundo

        # Criando LBL de Divisor
        self.lblDivisor1 = Label(self.frmLogin, text="    ", bg=self.corContainer)
        self.lblDivisor2 = Label(self.frmLogin, text="    ", bg=self.corContainer)
        self.lblDivisor3 = Label(self.frmLogin, text="    ", bg=self.corContainer)
        self.lblDivisor4 = Label(self.frmLogin, text="    ", bg=self.corContainer)
        
        # Empacotando Frames
        self.frmLogo.grid(column=0, row=0)
        self.frmLogin.grid(column=0, row=1, padx=170)
        self.frmBarra.grid(column=0, row=2)

        # Empacotando widgets de Usuário
        self.lblLogo.grid()
        self.lblUsuario.grid(column=1, row=1, sticky=W, pady=5)
        self.entUsuario.grid(column=1, row=1, sticky=E)

        # Empacotando widgets de Senha
        self.lblSenha.grid(column=1, row=2, sticky=W, pady=5)
        self.entSenha.grid(column=1, row=2, stick=E)
        self.btnLogin.grid(column=1, row=4, pady=10)
        self.lblMensagem.grid(column=1, row=5, pady=5)
        self.lblVoltar.grid(column=0, row=0, pady=115)

        self.lblMensagem.bind("<Button-1>", lambda ir: self.irCadastro())
        self.lblVoltar.bind("<Button-1>", lambda voltar: self.voltarInicio())

        self.lblDivisor1.grid(column=0, row=0)
        self.lblDivisor2.grid(column=2, row=0)
        self.lblDivisor3.grid(column=2, row=5)
        self.lblDivisor4.grid(column=0, row=5)

    def logarUsuario(self):

        login = Usuarios()

        usuario = self.usuario.get()
        senha = self.senha.get()

        usuario = usuario.lower()

        login.usuario = usuario
        login.senha = senha
        
        print("Evento de Login - OK")
        print(login.usuario)
        print(login.senha + "\n")

        retorno = login.autenticarUsuario()
        
        if retorno == True:
            self.irPrincipal()

        else:
            messagebox.showwarning("Login", retorno)  

    def irCadastro(self):

        cadastro = JanelaCadastro()

    def irPrincipal(self):
        
        # Desempacotando Frames
        self.frmLogo.grid_forget()
        self.frmLogin.grid_forget()
        self.frmBarra.grid_forget()

        # Desempacotando widgets de Usuário
        self.lblLogo.grid_forget()
        self.lblUsuario.grid_forget()
        self.entUsuario.grid_forget()

        # Desempacotando widgets de Senha
        self.lblSenha.grid_forget()
        self.entSenha.grid_forget()
        self.btnLogin.grid_forget()
        self.lblMensagem.grid_forget()
        self.lblVoltar.grid_forget()

        # Desempacotando widgets de Divisores
        self.lblDivisor1.grid_forget()
        self.lblDivisor2.grid_forget()
        self.lblDivisor3.grid_forget()
        self.lblDivisor4.grid_forget()

        principal = JanelaPrincipal()

    def voltarInicio(self):

        self.frmLogo.grid_forget()
        self.frmLogin.grid_forget()
        self.frmBarra.grid_forget()

        self.lblLogo.grid_forget()
        self.lblUsuario.grid_forget()
        self.entUsuario.grid_forget()
        self.lblSenha.grid_forget()
        self.entSenha.grid_forget()
        self.btnLogin.grid_forget()
        self.lblMensagem.grid_forget()
        self.lblVoltar.grid_forget()

        self.lblDivisor1.grid_forget()
        self.lblDivisor2.grid_forget()
        self.lblDivisor3.grid_forget()
        self.lblDivisor4.grid_forget()

        inicio = JanelaInicial()

class JanelaInicial():
    def __init__(self, master=None):
        
        # Atributos
        self.master = master

        # Lista de estilo
        Estilo.__init__(self)
        
        self.criarWidgets()

    def criarWidgets(self):

        # Criando frames
        self.frmLogo = Frame(self.master, bg=self.corFundo)
        self.frmDescricao = Frame(self.master, bg=self.corFundo)
        self.frmBarra = Frame(self.master, bg=self.corFundo)
        self.frmMensagem = Frame(self.master, bg=self.corFundo)

        # Criando IMG de Logo
        imgLogo = PhotoImage(file="img/spqr.png")
        self.lblLogo = Label(self.frmLogo, image=imgLogo, bg=self.corFundo)
        self.lblLogo.image = imgLogo

        # Criando LBL de Título
        self.lblTitulo = Label(self.frmDescricao)
        self.lblTitulo["font"] = self.fontePadrao
        self.lblTitulo["fg"] = self.corFrente
        self.lblTitulo["bg"] = self.corFundo
        self.lblTitulo["text"] = "ACAMPAMENTO JÚPITER"

        # Criando LBL de Descrição
        self.lblDescricao = Label(self.frmDescricao)
        self.lblDescricao["font"] = ("Arial", "12")
        self.lblDescricao["fg"] = self.corFrente
        self.lblDescricao["bg"] = self.corFundo
        self.lblDescricao["text"] = "Sistema de Gerenciamento de Fichas"

        # Criando BTN de Login
        self.btnLogin = Button(self.frmBarra, text="Login", cursor="hand2", width=10, height=1)
        self.btnLogin["font"] = self.fontePadrao
        self.btnLogin["relief"] = RIDGE
        self.btnLogin["fg"] = self.corFundo
        self.btnLogin["bg"] = self.corFrente
        self.btnLogin["activeforeground"] = self.corFundo
        self.btnLogin["activebackground"] = self.corFrente
        self.btnLogin["command"] = self.irLogin

        # Criando BTN de Cadastro
        self.btnCadastro = Button(self.frmBarra, text="Cadastro", cursor="hand2", width=10, height=1)
        self.btnCadastro["font"] = self.fontePadrao
        self.btnCadastro["relief"] = RIDGE
        self.btnCadastro["fg"] = self.corFundo
        self.btnCadastro["bg"] = self.corFrente
        self.btnCadastro["activeforeground"] = self.corFundo
        self.btnCadastro["activebackground"] = self.corFrente
        self.btnCadastro["command"] = self.irCadastro

        # Criando BTN de Sobre
        self.btnSobre = Button(self.frmBarra, text="Sobre", cursor="hand2", state=DISABLED, width=10, height=1)
        self.btnSobre["font"] = self.fontePadrao
        self.btnSobre["relief"] = RIDGE
        self.btnSobre["fg"] = self.corFundo
        self.btnSobre["bg"] = self.corFrente
        self.btnSobre["activeforeground"] = self.corFundo
        self.btnSobre["activebackground"] = self.corFrente
        self.btnSobre["command"] = self.irSobre

        # Criando BTN de Ajuda
        self.btnAjuda = Button(self.frmBarra, text="Ajuda", cursor="hand2", state=DISABLED, width=10, height=1)
        self.btnAjuda["font"] = self.fontePadrao
        self.btnAjuda["relief"] = RIDGE
        self.btnAjuda["fg"] = self.corFundo
        self.btnAjuda["bg"] = self.corFrente
        self.btnAjuda["activeforeground"] = self.corFundo
        self.btnAjuda["activebackground"] = self.corFrente
        self.btnAjuda["command"] = self.irAjuda

        # Criando BTN de Cadastrar
        self.lblMensagem = Label(self.frmMensagem, text="Selecione uma opção")
        self.lblMensagem["font"] = self.fontePadrao
        self.lblMensagem["justify"] = CENTER
        self.lblMensagem["fg"] = self.corFrente
        self.lblMensagem["bg"] = self.corFundo
        self.lblMensagem["activeforeground"] = self.corFrente
        self.lblMensagem["activebackground"] = self.corFundo

        # Empacotando widgets de FRM
        self.frmLogo.grid(column=0, row=0, padx=180, pady=10)
        self.frmDescricao.grid(column=0, row=1, pady=10)
        self.frmBarra.grid(column=0, row=2, pady=10)
        self.frmMensagem.grid(column=0, row=3)

        # Empacontando widgets de LBL
        self.lblLogo.grid()
        self.lblTitulo.grid()
        self.lblDescricao.grid()
        self.lblMensagem.grid()

        # Empacotando widgets de BTN
        self.btnLogin.grid(column=0, row=0, padx=5, pady=5)
        self.btnCadastro.grid(column=1, row=0, padx=5, pady=5)
        self.btnSobre.grid(column=0, row=1, padx=5, pady=5)
        self.btnAjuda.grid(column=1, row=1, padx=5, pady=5)

        self.btnLogin.bind("<Enter>", lambda msgLogin: self.mensagemLogin())
        self.btnCadastro.bind("<Enter>", lambda msgCadastro: self.mensagemCadastro())
        self.btnSobre.bind("<Enter>", lambda msgSobre: self.mensagemSobre())
        self.btnAjuda.bind("<Enter>", lambda msgAjuda: self.mensagemAjuda())

    def mensagemLogin(self):
        self.lblMensagem["text"] = "Clique para conectar-se com aplicativo"

    def mensagemCadastro(self):
        self.lblMensagem["text"] = "Clique para registrar uma conta"

    def mensagemSobre(self):
        self.lblMensagem["text"] = "Informações sobre o jogo"

    def mensagemAjuda(self):
        self.lblMensagem["text"] = "Guia de ajuda"

    def irLogin(self):

        self.frmLogo.grid_forget()
        self.frmDescricao.grid_forget()
        self.frmBarra.grid_forget()
        self.lblTitulo.grid_forget()
        self.lblLogo.grid_forget()
        self.lblDescricao.grid_forget()
        self.btnSobre.grid_forget()
        self.btnAjuda.grid_forget()
        self.lblMensagem.grid_forget()

        login = JanelaLogin()

    def irCadastro(self):

        cadastro = JanelaCadastro()

    def irSobre(self):
        
        self.frmLogo.grid_forget()
        self.frmDescricao.grid_forget()
        self.frmBarra.grid_forget()
        self.lblTitulo.grid_forget()
        self.lblLogo.grid_forget()
        self.lblDescricao.grid_forget()
        self.btnSobre.grid_forget()
        self.btnAjuda.grid_forget()
        self.lblMensagem.grid_forget()

        sobre = JanelaSobre()

    def irAjuda(self):

        self.frmLogo.grid_forget()
        self.frmDescricao.grid_forget()
        self.frmBarra.grid_forget()
        self.lblTitulo.grid_forget()
        self.lblLogo.grid_forget()
        self.lblDescricao.grid_forget()
        self.btnSobre.grid_forget()
        self.btnAjuda.grid_forget()
        self.lblMensagem.grid_forget()

        ajuda = JanelaAjuda()

if __name__ == "__main__":
    root = Tk()
    root.iconbitmap("img/spqr-icon.ico")
    root.title("< SPQR > Gerenciador de fichas")
    root.resizable(width=False, height=False)
    root.geometry("600x600+500+100")
    root["bg"] = "#330c50"
    
    programa = JanelaInicial(root)
    root.mainloop()