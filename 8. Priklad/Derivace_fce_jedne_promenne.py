import numpy as np

def fce(x):
    return np.exp(x) * np.sin(x)

def analyticka_derivace_fce(x):
    return np.exp(x) * (np.sin(x) + np.cos(x))

def numericka_derivace_stat(x, h):
    return (fce(x + h) - fce(x - h)) / (2 * h)

def numericka_derivace_adapt(x, h_initial, tolerance):
    h = h_initial
    derivative_old = numericka_derivace_stat(x, h)
    
    while True:
        h /= 2
        derivative_new = numericka_derivace_stat(x, h)
        if np.abs(derivative_new - derivative_old) < tolerance:
            return derivative_new
        derivative_old = derivative_new

#parametry
x = 1.0  #test bod
h_static = 0.1
h_initial = 0.1
tolerance = 1e-6

#vypocet
derivace_analytic = analyticka_derivace_fce(x)
derivace_static = numericka_derivace_stat(x, h_static)
derivace_adapt = numericka_derivace_adapt(x, h_initial, tolerance)

print(f"Analyticka derivace: {derivace_analytic}")
print(f"Numericka derivace - staticky krok: {derivace_static}")
print(f"Numericka derivace - adaptivni krok: {derivace_adapt}")
