x1_value = 4
x2_value = 9
a_value = 1
gamma1_value = 0.5
gamma2_value = 0.5
rho_value = -0.5
factor_list = [4, 9]
gamma_list = [gamma1_value, gamma2_value]

from production_functions import cobb_douglas, leontief, ces, general_ces

result_cobb_douglas = cobb_douglas(x1 = x1_value, x2 = x2_value, a = a_value, gamma1 = gamma1_value, gamma2 = gamma2_value)
result_leontief = leontief(x1 = x1_value, x2 = x2_value, a = a_value)
result_ces = ces(x1 = x1_value, x2 = x2_value, a = a_value, gamma1 = gamma1_value, gamma2 = gamma2_value, rho = rho_value)
result_general_ces = general_ces(factors= factor_list, gammas= gamma_list, a= a_value, rho= rho_value)

print(f"""Cobb-Douglas: Calculated: {result_cobb_douglas} Expected:   6.0""")
print(f"""Leontief:    Calculated: {result_leontief} Expected:   4.0""")
print(f"""CES:          Calculated: {result_ces} Expected:   6.25""")
print(f"""General CES: Calculated: {result_general_ces} Expected:  6.25""")