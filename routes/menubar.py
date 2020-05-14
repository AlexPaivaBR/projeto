def menus(self, master):

        menubar = Menu(self.master)
        menuUsuario = Menu(menubar, tearoff=0)
        menuUsuario.add_command(label="Login")
        menuUsuario.add_command(label="Cadastro")

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