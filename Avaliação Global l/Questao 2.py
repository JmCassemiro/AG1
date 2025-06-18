from sympy import symbols, integrate, Rational
from sympy import diff

c = 288 % 10
t = symbols('t')
v = 6*(c+1) * t**Rational(1, 5) - 3*(c+1)*t**2 + t/(c+3) - 4

s = integrate(v, t)
print("Função deslocamento s(t):")
print(s)


s_5 = s.subs(t, 5)
s_2 = s.subs(t, 2)
delta_s = s_5 - s_2
print("Deslocamento de t = 2 até t = 5:", delta_s.evalf())


a = diff(v, t)
print("Equação da aceleração a(t):")
print(a)
