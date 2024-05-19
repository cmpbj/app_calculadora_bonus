import tkinter as tk

from calcula_bonus import bonus


# Cria função para controlar o fluxo do cálculo e poder fazer testes para o caso do usuário inserir informações errôneas
def calcula():
    try:
        salario = float(entry_salario.get())
        bonus_salario = entry_bonus.get().replace(',', '.').replace('%', '')
        bonus_salario = float(bonus_salario)
        if bonus_salario > 1:
            bonus_salario = bonus_salario / 100
    except ValueError:
        label_resultado.config(text='Digite números válidos')
        return
    except Exception as e:
        label_resultado.config(text=f'Erro: {e}')
        return
    
    nome = entry_nome.get()
    if not nome.replace(" ", "").isalpha() or len(nome.strip()) == 0:
        label_resultado.config(text='Digite um nome válido')
        return

    calcula_bonus_usuario = bonus(salario=salario, porcentagem_bonus=bonus_salario)
    label_resultado.config(text=f"O usuário {nome} possui um salário de {salario} e um bônus de {calcula_bonus_usuario:.2f}")

# Cria janela para a aplicação
window = tk.Tk()
window.geometry("500x300")
window.title("Calculadora de Bônus")

# Criação dos widgets
label_nome = tk.Label(window, text='Digite seu nome:')
label_nome.pack()

entry_nome = tk.Entry(window)
entry_nome.pack()

label_salario = tk.Label(window, text='Digite seu salário:')
label_salario.pack()

entry_salario = tk.Entry(window)
entry_salario.pack()

label_bonus = tk.Label(window, text='Digite seu bônus:')
label_bonus.pack()

entry_bonus = tk.Entry(window)
entry_bonus.pack()

# Botão para calcular o bônus
button_calcular = tk.Button(window, text='Calcular Bônus', command=calcula)
button_calcular.pack(side='bottom')

label_resultado = tk.Label(window, text='', wraplength=250)
label_resultado.pack()