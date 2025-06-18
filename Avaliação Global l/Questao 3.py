from sympy import symbols, exp, ln, integrate

x = symbols('x')
c = 288 % 10
f = exp(3*x + c) - 4 * ln(x**2 + 5*x - c)

area = integrate(f, (x, 2, 8))
print("Área sob a curva de x = 2 até x = 8:")
print(area.evalf())
