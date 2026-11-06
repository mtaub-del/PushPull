def cobb_douglas (x1, x2, a, gamma1, gamma2):
    """
    Calculates the output of a Cobb-Douglas production function given inputs x1 and x2, scale factor a, and elasticity gamma1 and gamma2.

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
    """
    Calculates the output of a Leontief production function given inputs x1 and x2, and scale factor a.

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
    """
    Calculates the output of a CES production function given inputs x1 and x2, scale factor a, elasticity gamma1 and gamma2, and substitution parameter rho.

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

def general_ces (factors, gammas, a, rho):
    """
    Calculates the output of a generalized CES production function given inputs xj, scale factor a, elasticitys gammaj, and substitution parameter rho.

    Args:
        xj (list): list of inputs
        gammaj (list): list of output elasticities of inputs
        a (float): Total factor productivity
        rho (float): Substitution parameter
    Returns:
        float: Output of the generalized CES production function
    """
    y = a*(sum([gammas[i] * factors[i]**-rho for i in range(len(factors))]))**(-1/rho)
    return y
