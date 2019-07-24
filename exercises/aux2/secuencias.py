# Problema original Semestre Otoño 2017.

# Invariante: (sum_i < sum_i+1 && i <= N) || (element_i > element_i+1 && i <= N)
# Inicialización: N > 0 && i = 1 => (0 < 1 <= N) . sum_0 = 0 && sum_1 = 1 => sum_0 < sum_1
# Término: i > N.

def f(n):
    sum = 0
    for i in range(1, n + 1):
        sum += 1 / i
    return sum


def f_check_invariant(n):
    sum = 0
    previous_sum = sum
    for i in range(1, n + 1):
        sum += 1 / i
        if sum < previous_sum or i > n:
            print("Invariante inválido")
            return
        previous_sum = sum
    return sum


def g(n):
    state = False
    sum = 0
    for i in range(1, n + 1):
        state = not state  # cambia estado
        current_value = 1 / i
        if state:
            sum += current_value
        else:
            sum -= current_value
    return sum


print("Función f\n")
for i in range(1, 100):
    print(f(i))
print("\n\n")
print("Función g\n")
for i in range(1, 100):
    print(g(i))