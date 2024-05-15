import streamlit as st

from calcula_bonus import bonus

# Cria título para a aplicação
st.title('Calculadora de Bônus')

# Cria caixas para que o usuário possa inserir as informações
nome = st.text_input('Digite seu nome: ')    
salario = st.text_input(label='Digite seu salario: ')
bonus_salario = st.text_input(label='Digite seu bônus: ')

# Remove caracteres especiais:

bonus_salario = bonus_salario.replace(',', '.').replace('%', '')


# Cria botão para controlar o fluxo do cálculo e poder fazer testes para o caso do usuário inserir informações errôneas
if st.button("Calcular"):
    try:
        salario = float(salario)
        bonus_salario = float(bonus_salario)
        if bonus_salario > 1:
            bonus_salario = bonus_salario / 100
        else:
            bonus_salario = bonus_salario
    except Exception as e:
        st.error('Digite números válidos')
    finally:
        if nome.replace(" ", "").isalpha() == False or len(nome) == 0 or len(nome.strip()) == 0:
            st.error('Digite um nome válido')
        else:
            calcula_bonus_usuario = bonus(salario=salario, porcentagem_bonus=bonus_salario)
            st.write(f"O usuário {nome} possui um salário de {salario} e um bônus de {calcula_bonus_usuario: .2f}")