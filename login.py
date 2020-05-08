from tkinter import *


class Teste():
    def __init__(self, master=None):
        self.master = master
        self.lay = []

        Button(self.master, text="Click me,Create a sub-panel", command=self.create).pack()

    def create(self):

        self.top = Toplevel()
        self.lay.append(self.top)

        self.top.title("Main Panel")
        self.top.geometry('500x500+500+100')
        
        self.msg = Message(self.top, text="Show on Sub-panel",width=100)
        self.msg.pack()
        
        self.btn = Button(self.top,text='EXIT',command=self.exit_btn)
        self.btn.pack()

    def exit_btn(self):

            self.top.destroy()
            self.top.update()

if __name__ == '__main__':
    
    root = Tk()
    root.geometry('200x200+500+50')
    Teste(root)
    root.mainloop()