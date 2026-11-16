# 1- INTERFACE GRAFICA
import tkinter

# 2- ESTRUTURA
botoes = [["AC", "+/-", "%", "÷"], ["7", "8", "9", "x"], ["4", "5", "6", "-"], ["1", "2", "3", "+"], ["0", ".", "√", "="]]

simbolos_direita = ["÷", "x", "-", "+", "="]
simbolos_cima = ["AC", "+/-", "%"]

contador_linhas = len(botoes)
contador_colunas = len(botoes[0])

# 3- CORES
preto = "#303231"
cinza = "#979593"
rosa_claro = "#EBCACF"
rosa_escuro = "#EB9DA7"
branco = "white"


# 4- JANELA
janela = tkinter.Tk() #cria a janela
janela.title("Calculadora")
janela.resizable(False, False)

frame = tkinter.Frame(janela)
label = tkinter.Label(frame, text="0", font=("Arial", 45), background=preto, foreground=branco, anchor="e", width=contador_colunas)

# 5- GRID
label.grid(row=0, column=0, columnspan=contador_colunas, sticky="we")

for row in range(contador_linhas):
    for column in range(contador_colunas):
        valor = botoes[row][column]
        botao = tkinter.Button(frame, text=valor, font=("Arial", 30), width=contador_colunas - 1, height=1, command=lambda valor=valor:clique_botao(valor) )


        if valor in simbolos_cima:
            botao.config(foreground=preto, background=cinza)

        elif valor in simbolos_direita:
            botao.config(foreground=branco,background=rosa_escuro)

        else:
            botao.config(foreground=branco, background=rosa_claro)


        botao.grid(row=row+1, column=column)


frame.pack()

# a+b, a-b, a*b, a/b
A = "0"
operador = None
B = None

def reset():
    global A, B, operador
    A = "0"
    operador = None
    B = None

def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)

    return str(num)


def clique_botao(valor):
    global simbolos_direita, simbolos_cima, label, A, B, operador

    if valor in simbolos_direita:

        if valor == "=":
            if A is not None and operador is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operador == "+":
                    label["text"] = remove_zero_decimal(numA + numB)

                elif operador == "-":
                    label["text"] = remove_zero_decimal(numA - numB)

                elif operador == "x":
                    label["text"] = remove_zero_decimal(numA * numB)

                elif operador == "÷":
                    if numB != 0:
                        label["text"] = remove_zero_decimal(numA / numB)                 
                    else:
                        label["text"] = "Erro"

                reset()

        elif valor in "+-x÷":
            
            if operador is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"

            operador = valor

        
    elif valor in simbolos_cima:
        if valor == "AC":
            reset()
            label["text"] = "0"

        elif valor == "+/-":
            resultado = float(label["text"])* -1
            label["text"] = remove_zero_decimal(resultado)

        elif valor == "%":
            resultado = float(label["text"])/ 100
            label["text"] = remove_zero_decimal(resultado)

    else:

        if valor == ".":
            if valor not in label["text"]:
                label["text"] += valor

        elif valor in "0123456789":

            if label["text"] == "0":
                label["text"] = valor
            else:
                label["text"] += valor



# 6- CENTRALIZAR A JANELA
janela.update()
janela_width = janela.winfo_width()
janela_height = janela.winfo_height()
screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()

janela_x = int((screen_width/2) - (janela_width/2))
janela_y = int((screen_height/2) - (janela_height/2))

janela.geometry(f"{janela_width}x{janela_height}+{janela_x}+{janela_y}")

janela.mainloop()

