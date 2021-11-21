# * Haz depositado a tu cuenta bancaria una cantidad especifica de dinero (deposit).
# * Cada año tu saldo incrementa a la misma tasa de crecimiento (rate).
# * Asumiendo que no haces depósitos adicionales,
# * averigua cuánto tiempo le tomaría a tu saldo superar un umbral específico (threshold).

deposit = int(input("Ingrese el dopisto inicial: "))
rate = int(input("ingrese tasa de crecimiento: "))
trueshold = int(input("Ingrese el unmbral a superar: "))


def depositProfit(deposit, rate, trueshold):
    dineroacumulado = deposit
    rate = rate * 0.01
    year = 0
    while dineroacumulado < trueshold:
        dineroacumulado = dineroacumulado + (dineroacumulado * rate)
        year = year + 1
    print("\n")
    print(f'Se superara el umbral en {year} años')


depositProfit(deposit, rate, trueshold)

# Resuleto
