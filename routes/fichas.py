from database.banco import Ficheiro

class Fichas(object):
    def __init__(self, nome = "", idade = 0, raca = "", classe = "", usuario = "", senha = ""):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.classe = classe
        self.usuario = usuario
        self.senha = senha
    
    def criarFicha(self):

        banco = Ficheiro()

        c = banco.conexao.cursor()
        
        try:

            if self.nome == "" and self.idade == "" and self.raca == "" and self.classe == "":
                return "Preencha o formulário"
            
            elif self.nome == "":
                return "Insira um nome"
            
            elif self.idade == "":
                return "Insira uma idade"
            
            elif self.raca == "":
                return "Selecione uma raça"
            
            elif self.classe == "":
                return "Selecione uma classe"

            else:
                inserindo = ('INSERT INTO fichas(nome, idade, raca, classe) VALUES (?, ?, ?, ?)')
                c.execute(inserir, [(self.nome), (self.idade), (self.raca), (self.classe)])

                banco.conexao.commit()
                
                return "Ficha criada!"
                c.close()
                
        except:
            return "ERROR"

        banco.conexao.commit()
        c.close()
        
    def alterarFicha(self):
        pass

    def deletarFicha(self):
        pass

    def selecionarFicha(self):
        pass