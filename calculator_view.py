from tkinter import *

class CalculatorView:
    def __init__(self, controller):
        self.controller = controller

        self.janela = Tk()
        self.janela.title("Calculadora")
        self.janela.geometry("300x300")

        self.numero1_label = Label(self.janela, text="Número 1:")
        self.numero1_label.pack()

        self.numero1 = Entry(self.janela)
        self.numero1.pack()

        self.numero2_label = Label(self.janela, text="Número 2:")
        self.numero2_label.pack()

        self.numero2 = Entry(self.janela)
        self.numero2.pack()

        self.resultado_label = Label(self.janela, text="Resultado:")
        self.resultado_label.pack()

        self.adicionar_button = Button(self.janela, text="Adicionar", command=self.controller.adicionar)
        self.adicionar_button.pack()

        self.subtrair_button = Button(self.janela, text="Subtrair", command=self.controller.subtrair)
        self.subtrair_button.pack()

        self.multiplicar_button = Button(self.janela, text="Multiplicar", command=self.controller.multiplicar)
        self.multiplicar_button.pack()

        self.dividir_button = Button(self.janela, text="Dividir", command=self.controller.dividir)
        self.dividir_button.pack()

    def atualizar_resultado(self, resultado):
        self.resultado_label.config(text="Resultado: " + str(resultado))

    def iniciar(self):
        self.janela.mainloop()
