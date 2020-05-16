from routes.janelas import *
from tkinter import *

if __name__ == "__main__":
    root = Tk()
    root.iconbitmap("img/spqr-icon.ico")
    root.title("< SPQR > Gerenciador de fichas")
    root.resizable(width=False, height=False)
    root.geometry("600x600+500+100")
    root["bg"] = "#330c50"
    
    programa = JanelaCriacao(root)
    root.mainloop()