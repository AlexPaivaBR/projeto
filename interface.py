from routes.usuarios import Usuarios
from routes.fichas import Fichas
from tkinter import *

class Janela():
    def __init__(self, master=None):
        
        self.master = master

        #Atributos de Login
        self.usuario = StringVar()
        self.senha = StringVar()

        #Atributos de Cadastro
        self.novoUsuario = StringVar()
        self.novaSenha = StringVar()

        #Atributos de Principal
        self.nome = StringVar()
        self.idade = IntVar()
        self.raca = StringVar()
        self.classe = StringVar()

        # Criando recursos extras
        self.fontePadrao = ("Arial", "12", "bold")
        self.fonteTitulo = ("Arial", "30", "bold")
        self.corFrente = "white"
        self.corFundo = "#2b2b2b"

        # Chamando o método "janelas()"
        self.menus(self.master)
        self.janelas(self.master)

#Criando MENU

    def menus(self, master):

        menubar = Menu(self.master)
        menuUsuario = Menu(menubar, tearoff=0)
        menuUsuario.add_command(label="Login", command=self.widgetsLogin)
        menuUsuario.add_command(label="Cadastro", command=self.widgetsCadastro)

        menuUsuario.add_separator()

        menuUsuario.add_command(label="Sair", command=self.master.quit)

        menubar.add_cascade(label="Usuário", menu=menuUsuario)
        
        menuEditar = Menu(menubar, tearoff=0)
        menuEditar.add_command(label="Criar Ficha")

        menuEditar.add_separator()

        menuEditar.add_command(label="Alterar Ficha")
        menuEditar.add_command(label="Deletar Ficha")

        menubar.add_cascade(label="Editar", menu=menuEditar)

        menuAjuda = Menu(menubar, tearoff=0)
        menuAjuda.add_command(label="Ajuda")
        menuAjuda.add_command(label="Sobre")

        menubar.add_cascade(label="Ajuda", menu=menuAjuda)

        self.master.config(menu=menubar)

#Criando FRAMES

    def janelas(self, master):
        # Criando Frames (Containers)
        self.janelaTitulo = Frame(master, bg=self.corFundo)
        self.janelaUsuario = Frame(master, bg=self.corFundo)
        self.janelaSenha = Frame(master, bg=self.corFundo)
        self.janelaBotao = Frame(master, bg=self.corFundo)
        self.janelaMensagem = Frame(master, bg=self.corFundo, borderwidth=2, relief="solid")

        # Empacontando Frames (Containers)
        self.janelaTitulo.pack(padx=20, pady=10)
        self.janelaUsuario.pack(padx=50, pady=10)
        self.janelaSenha.pack(padx=50, pady=10)
        self.janelaBotao.pack(padx=20, pady=10)
        self.janelaMensagem.pack(padx=20, pady=10)

        # Chamando o método "janelaInicial()"
        self.widgetsInicial()

#Criando WIDGETS

    def widgetsInicial(self):
        # Criando LBL do Título
        self.lblTitulo = Label(self.janelaTitulo, text="BEM-VINDO", font=self.fonteTitulo, fg=self.corFrente, bg=self.corFundo)

        # Criando BTN de Login
        self.btnLogin = Button(self.janelaBotao, text="Login", font=self.fontePadrao, relief="groove", width=10, height=1)
        self.btnLogin["command"] = self.widgetsLogin

        #Criando BTN de Cadastro
        self.btnCadastro = Button(self.janelaBotao, text="Cadastro", font=self.fontePadrao, relief="groove", width=10, height=1)
        self.btnCadastro["command"] = self.widgetsCadastro

        # Criando LBL de Mensagem
        self.lblMensagem = Label(self.janelaMensagem, font=self.fontePadrao, fg=self.corFrente, bg=self.corFundo, width=30, height=2)
        self.lblMensagem["text"] = "Escolha uma opção"

        # Empacontando LBL do Título e Mensagem
        self.lblTitulo.pack(anchor=CENTER)
        self.lblMensagem.pack(anchor=CENTER)

        # Empacontando BTN de Login e Cadastro
        self.btnLogin.pack(side=LEFT, padx=10)
        self.btnCadastro.pack(side=RIGHT, padx=10)

    def widgetsLogin(self):

        self.usuario.set('')
        self.senha.set('')

        # Desempacontando widgets de JanelaInicial()
        self.lblTitulo.pack_forget()
        self.btnLogin.pack_forget()
        self.btnCadastro.pack_forget()
        self.lblMensagem.pack_forget()

        # Criando LBL do Título
        self.lblLogin_Titulo = Label(self.janelaTitulo, text="LOGIN", font=self.fonteTitulo ,fg=self.corFrente, bg=self.corFundo)

        # Criando LBL do Usuário
        self.lblLogin_Usuario = Label(self.janelaUsuario, text="Login", font=self.fontePadrao ,fg=self.corFrente, bg=self.corFundo)

        # Criando ENT do Usuário
        self.entLogin_Usuario = Entry(self.janelaUsuario, textvariable=self.usuario, relief="solid" ,width=30)

        # Criando LBL da Senha
        self.lblLogin_Senha = Label(self.janelaSenha, text="Senha", font=self.fontePadrao, fg=self.corFrente, bg=self.corFundo)

        # Criando ENT da Senha
        self.entLogin_Senha = Entry(self.janelaSenha, textvariable=self.senha, show="*", relief="solid", width=30)

        # Criando BTN de Logar
        self.btnLogin_Logar = Button(self.janelaBotao, text="Logar", font=self.fontePadrao, relief="groove", width=10, height=1)
        self.btnLogin_Logar["command"] = self.eventoLogin

        # Criando BTN de Voltar
        self.btnLogin_Voltar = Button(self.janelaBotao, text="Voltar", font=self.fontePadrao, relief="groove" ,width=10, height=1)
        self.btnLogin_Voltar["command"] = self.voltarLogin

        # Criando LBL de Mensagem
        self.lblLogin_Mensagem = Label(self.janelaMensagem, font=self.fontePadrao, fg=self.corFrente, bg=self.corFundo, width=30, height=2)
        self.lblLogin_Mensagem["text"] = "Clique em Logar"

        # Empacontando LBL do Título
        self.lblLogin_Titulo.pack(anchor=CENTER)

        # Empacontando TXT e LBL do Usuário
        self.lblLogin_Usuario.pack(anchor=NW)
        self.entLogin_Usuario.pack(anchor=CENTER)

        # Empacontando TXT e LBL da Senha
        self.lblLogin_Senha.pack(anchor=NW)
        self.entLogin_Senha.pack(anchor=CENTER)

        # Empacontando BTN de Logar e Voltar
        self.btnLogin_Logar.pack(side=RIGHT, padx=10)
        self.btnLogin_Voltar.pack(side=LEFT, padx=10)

        # Empacontando LBL de Mensagem
        self.lblLogin_Mensagem.pack(anchor=CENTER)

    def widgetsCadastro(self):
        self.novoUsuario.set('')
        self.novaSenha.set('')

        # Desempacontando widgets de JanelaInicial
        self.lblTitulo.pack_forget()
        self.btnLogin.pack_forget()
        self.btnCadastro.pack_forget()
        self.lblMensagem.pack_forget()

        # Criando LBL do Título
        self.lblCadastro_Titulo = Label(self.janelaTitulo, text="CADASTRO", font=self.fonteTitulo, fg=self.corFrente, bg=self.corFundo)

        # Criando LBL do Usuário
        self.lblCadastro_Usuario = Label(self.janelaUsuario, text="Usuário", font=self.fontePadrao, fg=self.corFrente, bg=self.corFundo)

        # Criando ENT do Usuário
        self.entCadastro_Usuario = Entry(self.janelaUsuario, textvariable=self.novoUsuario, relief="solid", width=30)

        # Criando LBL da Senha
        self.lblCadastro_Senha = Label(self.janelaSenha, text="Senha", font=self.fontePadrao, fg=self.corFrente, bg=self.corFundo)

        # Criando ENT da Senha
        self.entCadastro_Senha = Entry(self.janelaSenha, textvariable=self.novaSenha, show="*", relief="solid", width=30)

        # Criando BTN de Logar
        self.btnCadastro_Criar = Button(self.janelaBotao, text="Cadastrar", font=self.fontePadrao, relief="groove", width=10, height=1)
        self.btnCadastro_Criar["command"] = self.eventoCadastro

        # Criando BTN de Voltar
        self.btnCadastro_Voltar = Button(self.janelaBotao, text="Voltar", font=self.fontePadrao, relief="groove", width=10, height=1)
        self.btnCadastro_Voltar["command"] = self.voltarCadastro

        # Criando LBL de Mensagem
        self.lblCadastro_Mensagem = Label(self.janelaMensagem, font=self.fontePadrao, fg=self.corFrente, bg=self.corFundo, width=30, height=2)
        self.lblCadastro_Mensagem["text"] = "Preencha o formulário\nDepois clique em Criar"

        # Empacontando LBL do Título
        self.lblCadastro_Titulo.pack(anchor=CENTER)

        # Empacontando TXT e LBL do Usuário
        self.lblCadastro_Usuario.pack(anchor=NW)
        self.entCadastro_Usuario.pack(anchor=CENTER)

        # Empacontando TXT e LBL da Senha
        self.lblCadastro_Senha.pack(anchor=NW)
        self.entCadastro_Senha.pack(anchor=CENTER)

        # Empacontando BTN de Logar e Voltar
        self.btnCadastro_Criar.pack(side=RIGHT, padx=10)
        self.btnCadastro_Voltar.pack(side=LEFT, padx=10)

        # Empacontando LBL de Mensagem
        self.lblCadastro_Mensagem.pack(anchor=CENTER)

    def widgetsPrincipal(self):
        # Desempacontando widgets de Login
        self.lblLogin_Titulo.pack_forget()
        self.lblLogin_Mensagem.pack_forget()
        self.lblLogin_Usuario.pack_forget()
        self.lblLogin_Senha.pack_forget()
        self.entLogin_Usuario.pack_forget()
        self.entLogin_Senha.pack_forget()
        self.btnLogin_Logar.pack_forget()
        self.btnLogin_Voltar.pack_forget()

        # Criando LBL do Título
        self.lblPrincipal_Titulo = Label(self.janelaTitulo, text="PRINCIPAL", font=self.fonteTitulo, fg=self.corFrente, bg=self.corFundo)

        # Criando BTN de Logar
        self.btnPrincipal_CriarFicha = Button(self.janelaBotao, text="Criar", font=self.fontePadrao, relief="groove", width=10, height=1)
        self.btnPrincipal_CriarFicha["command"] = self.widgetsCriarFicha

        # Criando BTN de Voltar
        self.btnPrincipal_AlterarFicha = Button(self.janelaBotao, text="Alterar", font=self.fontePadrao, relief="groove", width=10, height=1)
        self.btnPrincipal_AlterarFicha["command"] = self.widgetsAlterarFicha

        # Criando BTN de Voltar
        self.btnPrincipal_DeletarFicha = Button(self.janelaBotao, text="Deletar", font=self.fontePadrao, relief="groove", width=10, height=1)
        self.btnPrincipal_AlterarFicha["command"] = self.widgetsDeletarFicha

        # Criando LBL de Mensagem
        self.lblPrincipal_Mensagem = Label(self.janelaMensagem, font=self.fontePadrao, fg=self.corFrente, bg=self.corFundo, width=30, height=2)
        self.lblPrincipal_Mensagem["text"] = "Escolha uma opção"

        # Empacontando LBL do Título
        self.lblPrincipal_Titulo.pack(anchor=CENTER)

        # Empacontando BTN de Logar e Voltar
        self.btnPrincipal_CriarFicha.pack(side=LEFT, padx=10)
        self.btnPrincipal_AlterarFicha.pack(side=LEFT, padx=10)
        self.btnPrincipal_DeletarFicha.pack(side=RIGHT, padx=10)

        # Empacontando LBL de Mensagem
        self.lblPrincipal_Mensagem.pack(anchor=CENTER)

    def widgetsCriarFicha(self):

        # Desempacontando widgets de Principal
        self.lblPrincipal_Titulo.pack_forget()
        self.btnPrincipal_CriarFicha.pack_forget()
        self.btnPrincipal_AlterarFicha.pack_forget()
        self.btnPrincipal_DeletarFicha.pack_forget()
        self.lblPrincipal_Mensagem.pack_forget()
    
    def widgetsAlterarFicha(self):

        # Desempacontando widgets de Principal
        self.lblPrincipal_Titulo.pack_forget()
        self.btnPrincipal_CriarFicha.pack_forget()
        self.btnPrincipal_AlterarFicha.pack_forget()
        self.btnPrincipal_DeletarFicha.pack_forget()
        self.lblPrincipal_Mensagem.pack_forget()
    
    def widgetsDeletarFicha(self):

        # Desempacontando widgets de Principal
        self.lblPrincipal_Titulo.pack_forget()
        self.btnPrincipal_CriarFicha.pack_forget()
        self.btnPrincipal_AlterarFicha.pack_forget()
        self.btnPrincipal_DeletarFicha.pack_forget()
        self.lblPrincipal_Mensagem.pack_forget()

    def voltarLogin(self):

        self.btnLogin_Voltar.pack_forget()
        self.lblLogin_Titulo.pack_forget()

        # Desempacontando LBL e TXT do Usuário
        self.lblLogin_Usuario.pack_forget()
        self.entLogin_Usuario.pack_forget()

        # Desempacontando LBL e TXT da Senha
        self.lblLogin_Senha.pack_forget()
        self.entLogin_Senha.pack_forget()

        # Desempacontando BTN de Logar e Voltar
        self.btnLogin_Logar.pack_forget()
        self.btnLogin_Voltar.pack_forget()

        # Desempacontando LBL de Mensagem
        self.lblLogin_Mensagem.pack_forget()

        #Empacontando widgets de JanelaInicial()
        self.lblTitulo.pack(anchor=CENTER)
        self.btnLogin.pack(side=LEFT, padx=10)
        self.btnCadastro.pack(side=RIGHT, padx=10)
        self.lblMensagem.pack(anchor=CENTER)

    def voltarCadastro(self):

        # Desempacontando LBL do Título
        self.lblCadastro_Titulo.pack_forget()

        # Desempacontando LBL e TXT do Usuário
        self.lblCadastro_Usuario.pack_forget()
        self.entCadastro_Usuario.pack_forget()

        # Desempacontando LBL e TXT da Senha
        self.lblCadastro_Senha.pack_forget()
        self.entCadastro_Senha.pack_forget()

        # Desempacontando BTN de Logar e Voltar
        self.btnCadastro_Criar.pack_forget()
        self.btnCadastro_Voltar.pack_forget()

        # Desempacontando LBL de Mensagem
        self.lblCadastro_Mensagem.pack_forget()

        #Empacontando widgets de JanelaInicial()
        self.lblTitulo.pack(anchor=CENTER)
        self.btnLogin.pack(side=LEFT, padx=10)
        self.btnCadastro.pack(side=RIGHT, padx=10)
        self.lblMensagem.pack(anchor=CENTER)

#Criando EVENTOS

    def eventoLogin(self):

        login = Usuarios()

        usuario = self.usuario.get()
        senha = self.senha.get()

        usuario = usuario.lower()

        login.usuario = usuario
        login.senha = senha
        
        print("Evento de Login - OK")
        print(login.usuario)
        print(login.senha + "\n")

        verificando = login.autenticarUsuario()
        
        if verificando == True:
            self.widgetsPrincipal()

        else:
            self.lblLogin_Mensagem["text"] = verificando

    def eventoCadastro(self):
        
        cadastro = Usuarios()

        novoUsuario = self.novoUsuario.get()
        novaSenha = self.novaSenha.get()

        novoUsuario = novoUsuario.lower()

        cadastro.novoUsuario = novoUsuario
        cadastro.novaSenha = novaSenha

        print(cadastro.novoUsuario)
        print(cadastro.novaSenha)

        self.lblCadastro_Mensagem["text"] = cadastro.cadastrarUsuario()

    def eventoPrincipal(self):

        ficha = Fichas()

        nome = self.nome.get()
        idade = self.idade.get()
        raca = self.raca.get()
        classe = self.classe.get()

        ficha.nome = nome
        ficha.idade = idade
        ficha.raca = raca
        ficha.classe = classe

        print(ficha.nome)
        print(ficha.idade)
        print(ficha.raca)
        print(ficha.classe)

        #self.lblPrincipal_Mensagem["text"] = self.

if __name__ == "__main__":
    root = Tk()
    root.geometry("600x600")
    root.title("Gerenciador de Fichas")
    root["bg"] = "#2b2b2b"
    root.resizable(width=False, height=False)
    programa = Janela(root)
    root.mainloop()