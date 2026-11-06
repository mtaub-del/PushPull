def cobb_douglas (x1, x2, a, gamma1, gamma2):
    """Calculates the output of a Cobb-Douglas production function given inputs x1 and x2, scale factor a, and elasticity gamma1 and gamma2.

    Args:
        x1 (float): Input 1
        x2 (float): Input 2
        a (float): Total factor productivity 
        gamma1 (float): Output elasticity of input 1
        gamma2 (float): Output elasticity of input 2

    Returns:
        float: Output of the Cobb-Douglas production function
    """

    y = a * (x1**gamma1) * (x2**gamma2) 
    return y 

def leontief (x1, x2, a):
    """Calculates the output of a Leontief production function given inputs x1 and x2, and scale factor a.

    Args:
        x1 (float): Input 1
        x2 (float): Input 2
        a (float): Total factor productivity
    Returns:
        float: Output of the Leontief production function
    """ 
    y = a * min(x1, x2) 
    return y 

def ces (x1, x2, a, gamma1, gamma2, rho):
    """Calculates the output of a CES production function given inputs x1 and x2, scale factor a, elasticity gamma1 and gamma2, and substitution parameter rho.

    Args:
        x1 (float): Input 1
        x2 (float): Input 2
        a (float): Total factor productivity
        gamma1 (float): Output elasticity of input 1
        gamma2 (float): Output elasticity of input 2
        rho (float): Substitution parameter
    Returns:
        float: Output of the CES production function
    """
    y = a*(gamma1 * x1**-rho + gamma2 * x2**-rho)**(-1/rho)
    return y 


x1_value = 4
x2_value = 9
a_value = 1
gamma1_value = 0.5
gamma2_value = 0.5
rho_value = -0.5

result_cobb_douglas = cobb_douglas(x1 = x1_value, x2 = x2_value, a = a_value, gamma1 = gamma1_value, gamma2 = gamma2_value)
result_leontief = leontief(x1 = x1_value, x2 = x2_value, a = a_value)
result_ces = ces(x1 = x1_value, x2 = x2_value, a = a_value, gamma1 = gamma1_value, gamma2 = gamma2_value, rho = rho_value)

print(f"""Cobb-Douglas: Calculated: {result_cobb_douglas} Expected:   6.0""")
print(f"""Leontief:    Calculated: {result_leontief} Expected:   4.0""")
print(f"""CES:          Calculated: {result_ces} Expected:   6.25""")
