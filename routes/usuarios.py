from database.banco import Cadastrados

class Usuarios(object):
    def __init__(self, usuario = "", senha = "", novoUsuario = "", novaSenha = ""):
        self.usuario = usuario
        self.senha = senha
        self.novoUsuario = novoUsuario
        self.novaSenha = novaSenha
    
    def cadastrarUsuario(self):
        
        banco = Cadastrados()
        c = banco.conexao.cursor()

        novoUsuario = self.novoUsuario
        novaSenha = self.novaSenha

        print("Criando cadastro...")
        print("Novo usuário: {}".format(novoUsuario))
        print("Nova senha: {}".format(novaSenha))

        localizarUsuario = ('SELECT * FROM usuarios WHERE usuario = ?')
        c.execute(localizarUsuario, [(novoUsuario)])

        print("Localizando usuário existente...")
        verificarCadastro = c.fetchall()

        try:
            if verificarCadastro:
                print("Usuário localizado!")
                return "Usuário já existe!"
            
            elif novoUsuario == "" and novaSenha == "":
                return "Preencha o formulário"
            
            elif novoUsuario == "":
                return "Insira um usuário"
            
            elif novaSenha == "":
                return "Insira uma senha"

            else:
                inserir = ('INSERT INTO usuarios(usuario, senha) VALUES (?, ?)')
                c.execute(inserir, [(novoUsuario), (novaSenha)])

                banco.conexao.commit()
                
                print("Usuário criado!")
                return "Conta criada!"
        except:
            return "Error"

        banco.conexao.commit()
        c.close()

    def autenticarUsuario(self):
        
        banco = Cadastrados()
        c = banco.conexao.cursor()

        usuario = self.usuario
        senha = self.senha

        print("Autenticando usuário...")
        print("Usuario: {}".format(usuario))
        print("Senha: {}\n".format(senha))

        localizarUsuario = ('SELECT * FROM usuarios WHERE usuario = ? and senha = ?')
        c.execute(localizarUsuario, [(usuario), (senha)])
        
        print("Localizando usuário existente...")
        
        verificarUsuario = c.fetchall()
        print(verificarUsuario)

        try:
            if verificarUsuario:
                print("Verificado com sucesso!")
                return True

            elif usuario == "" and senha == "":
                return "Preencha o formulário"
            
            elif usuario == "":
                return "Insira um usuário"
            
            elif senha == "":
                return "Insira uma senha"

            else:
                return "Usuário não encontrado."

        except:
            return "Error"