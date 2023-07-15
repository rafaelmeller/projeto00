from calculator_view import CalculatorView

class CalculatorController:
    def __init__(self):
        self.view = CalculatorView(self)

    def adicionar(self):
        if self.view.numero1.get() and self.view.numero2.get():
            resultado = float(self.view.numero1.get()) + float(self.view.numero2.get())
            self.view.atualizar_resultado(resultado)

    def subtrair(self):
        if self.view.numero1.get() and self.view.numero2.get():
            resultado = float(self.view.numero1.get()) - float(self.view.numero2.get())
            self.view.atualizar_resultado(resultado)

    def multiplicar(self):
        if self.view.numero1.get() and self.view.numero2.get():
            resultado = float(self.view.numero1.get()) * float(self.view.numero2.get())
            self.view.atualizar_resultado(resultado)

    def dividir(self):
        if self.view.numero1.get() and self.view.numero2.get():
            resultado = float(self.view.numero1.get()) / float(self.view.numero2.get())
            self.view.atualizar_resultado(resultado)

    def iniciar(self):
        self.view.iniciar()
