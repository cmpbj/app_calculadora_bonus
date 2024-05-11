import streamlit as st

from calcula_bonus import bonus

# Cria título para a aplicação
st.title('Calculadora de Bônus')

# Cria caixas para que o usuário possa inserir as informações
nome = st.text_input('Digite seu nome: ')    
salario = st.text_input(label='Digite seu salario: ')
bonus_salario = st.text_input(label='Digite seu bônus: ')


# Cria botão para controlar o fluxo do cálculo e poder fazer testes para o caso do usuário inserir informações errôneas
if st.button("Calcular"):
    if nome.isalpha() == False:
        st.error('Digite um nome válido')
    try:
        salario = float(salario)
        bonus_salario = float(bonus_salario)
    except Exception as e:
        st.error('Digite números válidos')
    else:
        calcula_bonus_usuario = bonus(salario=salario, porcentagem_bonus=bonus_salario)
        st.write(f"O usuário {nome} possui o bônus de {calcula_bonus_usuario: .2f}")