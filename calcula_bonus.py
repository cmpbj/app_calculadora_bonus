# Cria função que recebe como parâmetro o salário do usuário e a porcentagem do bônus. Além disso, a função calcula o bônus em cima de um valor de 1000 reais
# passado na função como uma constante
def bonus(salario: float, porcentagem_bonus: float, CONSTANTE_BONUS=1000) -> float:
    return CONSTANTE_BONUS + (salario * porcentagem_bonus)