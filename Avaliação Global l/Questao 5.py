from sympy import symbols, Eq, cos, solve, sqrt, exp

x = symbols('x')
c = 288 % 10


eq = Eq(2 * cos(4 * (c + 1) * x), -5)

# Questao 1
sol = solve(eq, x)
print("Soluções da equação 1:")
print(sol)

# Questao 2
eq2 = Eq(5*sqrt(x) - 4*x**2 + x/2, c)
sol2 = solve(eq2, x)
print("Soluções da equação 2:")
print([s.evalf() for s in sol2])

# Questao 3
eq3 = Eq(exp(x + 1) + exp(x - 2) + exp(x), c+4)
sol3 = solve(eq3, x)
print("Soluções da equação 3:")
print(sol3)
