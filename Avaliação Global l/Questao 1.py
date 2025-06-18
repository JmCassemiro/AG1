from sympy import symbols, sqrt, limit, oo

c = 288 % 10

# Questão 1
x = symbols('x')
expr1 = ((c+1)*x - (c+1)) / (sqrt(x) - 1)
lim1 = limit(expr1, x, 1)
print("Limite 1:", lim1)

# Questão 2
expr2 = ((c+1)*x**4 + 3*x**2 - 2) / (4 - x**4)
lim2 = limit(expr2, x, oo)
print("Limite 2:", lim2)

# Questão 3
lim3 = limit(expr2, x, -oo)
print("Limite 3:", lim3)
