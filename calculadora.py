from tkinter import *

class window:

    def __init__(self,master):

        self.master = master
        self.master.resizable(width=0, height=0)
        self.master.title("Calculadora")
        self.master.attributes('-alpha',0.93)
        self.master['bg']="#B8BBBB"               

        self.mostrar = StringVar()
        self.resul_mues = StringVar()

        def mostrar_mostrar(num):

            if self.mostrar.get() =="Error " or self.mostrar.get()=="0" or self.mostrar.get()=="0.0" or self.mostrar.get()=="Desbordamiento":
                    self.mostrar.set("")
            
            self.mostrar_1 = self.mostrar.get()+ str(num)
            if len(self.mostrar_1) >30:
                self.mostrar.set("Desbordamiento")
            else:
                self.mostrar.set(self.mostrar.get()+ str(num))
        
        def resultado(event):
            
            try:
                self.total = str(eval(self.mostrar.get()))
                self.redondeado = "{:,.2f}".format(float(self.total))
                self.resul_mues.set(self.redondeado)
                self.mostrar.set("")
                    
            except:
                self.mostrar.set("Error ") 

        def clean():

            self.mostrar.set("")
            self.resul_mues.set("")              

        def borrar_uno():

            self.borrar_one = str(self.mostrar.get())
            self.nuevo = self.borrar_one[:-1]
            self.mostrar.set(self.nuevo)
            self.resul_mues.set("")            
        
        self.label_muestra = Entry(self.master, font = "Helvetica 15 bold", fg="#ffffff",bg="#A1A6A6",bd=0,justify="center", textvariable=self.mostrar)
        self.label_muestra.grid(row=0, column=0, columnspan=4, padx=5,ipady=10, sticky="SNEW")

        self.result_muest = Label(self.master, font = "Helvetica 20 bold", fg="#ffffff",bg="#A1A6A6",bd=0, anchor="e", textvariable=self.resul_mues)
        self.result_muest.grid(row=1, column=0,columnspan=4,padx=5, ipady=8, sticky="SNEW")

        self.btn_parent = Button(self.master, text=" ( ", fg="#fff", bg="#151616", width="11", height="3", command = lambda: mostrar_mostrar("("))
        self.btn_elev = Button(self.master, text="DEL", fg="#fff", bg="#151616", width="11", height="3", command = borrar_uno)
        self.btn_parente = Button(self.master, text=" ) ", fg="#fff", bg="#151616", width="11", height="3", command = lambda: mostrar_mostrar(")"))
        self.btn_div = Button(self.master, text=" / ", fg="#fff", bg="#151616", width="11", height="3", command = lambda: mostrar_mostrar("/"))

        self.btn_parent.grid(row=2, column=0, padx=2, pady=5, sticky="SNEW")
        self.btn_elev.grid(row=2, column=1, padx=2, pady=5, sticky="SNEW")
        self.btn_parente.grid(row=2, column=2, padx=2, pady=5, sticky="SNEW")
        self.btn_div.grid(row=2, column=3, padx=2, pady=5, sticky="SNEW")

        self.btn_7 = Button(self.master, text="7", fg="#fff", bg="#000000", width="11", height="3", command = lambda: mostrar_mostrar(7))
        self.btn_8 = Button(self.master, text="8", fg="#fff", bg="#000000", width="11", height="3", command = lambda: mostrar_mostrar(8))
        self.btn_9 = Button(self.master, text="9", fg="#fff", bg="#000000", width="11", height="3", command = lambda: mostrar_mostrar(9))
        self.btn_x = Button(self.master, text="X", fg="#fff", bg="#151616", width="11", height="3", command = lambda: mostrar_mostrar("*"))

        self.btn_7.grid(row=3, column=0, padx=2, pady=5, sticky="SNEW")
        self.btn_8.grid(row=3, column=1, padx=2, pady=5, sticky="SNEW")
        self.btn_9.grid(row=3, column=2, padx=2, pady=5, sticky="SNEW")
        self.btn_x.grid(row=3, column=3, padx=2, pady=5, sticky="SNEW")

        self.btn_4 = Button(self.master, text="4", fg="#fff", bg="#000000", width="11", height="3", command = lambda: mostrar_mostrar(4))
        self.btn_5 = Button(self.master, text="5", fg="#fff", bg="#000000", width="11", height="3", command = lambda: mostrar_mostrar(5))
        self.btn_6 = Button(self.master, text="6", fg="#fff", bg="#000000", width="11", height="3", command = lambda: mostrar_mostrar(6))
        self.btn_ = Button(self.master, text="-", fg="#fff", bg="#151616", width="11", height="3", command = lambda: mostrar_mostrar("-"))

        self.btn_4.grid(row=4, column=0, padx=2, pady=5, sticky="SNEW")
        self.btn_5.grid(row=4, column=1, padx=2, pady=5, sticky="SNEW")
        self.btn_6.grid(row=4, column=2, padx=2, pady=5, sticky="SNEW")
        self.btn_.grid(row=4, column=3, padx=2, pady=5, sticky="SNEW")

        self.btn_1 = Button(self.master, text="1", fg="#fff", bg="#000000", width="11", height="3", command = lambda: mostrar_mostrar(1))
        self.btn_2 = Button(self.master, text="2", fg="#fff", bg="#000000", width="11", height="3", command = lambda: mostrar_mostrar(2))
        self.btn_3 = Button(self.master, text="3", fg="#fff", bg="#000000", width="11", height="3", command = lambda: mostrar_mostrar(3))
        self.btn_m = Button(self.master, text="+", fg="#fff", bg="#151616", width="11", height="3", command = lambda: mostrar_mostrar("+"))

        self.btn_1.grid(row=5, column=0, padx=2, pady=5, sticky="SNEW")
        self.btn_2.grid(row=5, column=1, padx=2, pady=5, sticky="SNEW")
        self.btn_3.grid(row=5, column=2, padx=2, pady=5, sticky="SNEW")
        self.btn_m.grid(row=5, column=3, padx=2, pady=5, sticky="SNEW")
       
        self.btn_CE = Button(self.master, text="CE", fg="#fff", bg="#000000", width="11", height="3", command = clean)
        self.btn_0 = Button(self.master, text="0", fg="#fff", bg="#000000", width="11", height="3", command = lambda: mostrar_mostrar(0))
        self.btn_coma = Button(self.master, text=".", fg="#fff", bg="#000000", width="11", height="3", command = lambda: mostrar_mostrar("."))
        self.btn_ig = Button(self.master, text="=", fg="#fff", bg="#151616", width="11", height="3", command = lambda: resultado('<Return>'))

        self.btn_CE.grid(row=6, column=0, padx=2, pady=5, sticky="SNEW")
        self.btn_0.grid(row=6, column=1, padx=2, pady=5, sticky="SNEW")
        self.btn_coma.grid(row=6, column=2, padx=2, pady=5, sticky="SNEW")
        self.btn_ig.grid(row=6, column=3, padx="1", pady="5", sticky="SNEW")

        self.master.bind('<Return>', resultado)      

def main():
    root = Tk()
    app = window(root)
    root.mainloop()

if __name__ == '__main__':
    main()  