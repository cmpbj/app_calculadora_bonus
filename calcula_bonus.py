def bonus(salario: float, porcentagem_bonus: float, CONSTANTE_BONUS=1000) -> float:
    return CONSTANTE_BONUS + (salario * porcentagem_bonus)