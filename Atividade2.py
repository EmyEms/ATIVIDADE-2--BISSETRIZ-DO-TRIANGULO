def bissetriz_externa(lado_ab, lado_ac, lado_bc):
    # Fórmula da bissetriz externa: razão dos lados adjacentes
    # similar à fórmula da bissetriz interna
    lado_bd = (lado_ab * lado_bc) / (lado_ab - lado_ac)
    lado_dc = lado_bc - lado_bd
    return lado_bd, lado_dc

# Entrada dos lados do triângulo
lado_ab = float(input("Digite o valor do lado AB: "))
lado_ac = float(input("Digite o valor do lado AC: "))
lado_bc = float(input("Digite o valor do lado BC: "))

# Calcular a divisão do lado oposto pela bissetriz externa
lado_bd, lado_dc = bissetriz_externa(lado_ab, lado_ac, lado_bc)
print(f"O lado BC é dividido em BD = {lado_bd:.2f} e DC = {lado_dc:.2f}")
