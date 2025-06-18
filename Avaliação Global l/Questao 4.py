from sympy import symbols, Eq, solve


c = 288 % 10
I_A, I_B = symbols('I_A I_B')


V1 = 10 + 2*c
V2 = 5 + 2*c


eq1 = Eq(35*I_A - 10*I_B, V1)
eq2 = Eq(-10*I_A + 30*I_B, V2)


solution = solve((eq1, eq2), (I_A, I_B))


I1 = solution[I_A]
I2 = solution[I_B]
I3 = I1 - I2

print("Solução do sistema de equações:")
print("I1 =", I1)
print("I2 =", I2)
print("I3 =", I3)
