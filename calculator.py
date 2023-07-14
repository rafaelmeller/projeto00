from tkinter import *

# Funções das operações
def adicionar():
    resultado = float(numero1.get()) + float(numero2.get())
    atualizar_resultado(resultado)

def subtrair():
    resultado = float(numero1.get()) - float(numero2.get())
    atualizar_resultado(resultado)

def multiplicar():
    resultado = float(numero1.get()) * float(numero2.get())
    atualizar_resultado(resultado)

def dividir():
    resultado = float(numero1.get()) / float(numero2.get())
    atualizar_resultado(resultado)

def atualizar_resultado(resultado):
    resultado_label.config(text="Resultado: " + str(resultado))

# Configuração da janela principal
janela = Tk()
janela.title("Calculadora")
janela.geometry("300x200")

# Labels e campos de entrada
numero1_label = Label(janela, text="Número 1:")
numero1_label.pack()

numero1 = Entry(janela)
numero1.pack()

numero2_label = Label(janela, text="Número 2:")
numero2_label.pack()

numero2 = Entry(janela)
numero2.pack()

resultado_label = Label(janela, text="Resultado:")
resultado_label.pack()

# Botões de operação
adicionar_button = Button(janela, text="Adicionar", command=adicionar)
adicionar_button.pack()

subtrair_button = Button(janela, text="Subtrair", command=subtrair)
subtrair_button.pack()

multiplicar_button = Button(janela, text="Multiplicar", command=multiplicar)
multiplicar_button.pack()

dividir_button = Button(janela, text="Dividir", command=dividir)
dividir_button.pack()

# Iniciar a janela principal
janela.mainloop()
