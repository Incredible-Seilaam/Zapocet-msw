import numpy as np
from scipy.integrate import quad
import math

def polynomialni_fce(x):
    return x**3 - 6*x**2 + 11*x - 6  #analytický integrál: (x^4/4) - (6*x^3/3) + (11*x^2/2) - 6*x

def exponencialni_fce(x):
    return np.exp(x) - 2  #analytický integrál: exp(x) - 2*x

def harmonicka_fce(x):
    return np.sin(x) - 0.5*x  #analytický integrál: -cos(x) - 0.25*x^2

def vypocet_integralu(func, a, b):
    integral, _ = quad(func, a, b)
    return integral

def test_metody():
    a = 0  # dolní mez
    b = 3  # horní mez

    #polynomiální fce
    print("Polynomialni funkce: f(x) = x^3 - 6x^2 + 11x - 6")
    analyticky_integral_polynomial = (b**4 / 4) - (6 * b**3 / 3) + (11 * b**2 / 2) - 6 * b - (a**4 / 4) + (6 * a**3 / 3) - (11 * a**2 / 2) + 6 * a
    vypocet_integral_polynomial = vypocet_integralu(polynomialni_fce, a, b)
    print(f"    Analyticky integral: {analyticky_integral_polynomial}")
    print(f"    Numericky vypocet integral: {vypocet_integral_polynomial}\n")

    #exponenciální fce
    a = 0
    b = 2
    print("Exponencialni funkce: f(x) = e^x - 2")
    analyticky_integral_exp = np.exp(b) - 2 * b - (np.exp(a) - 2 * a)
    vypocet_integral_exp = vypocet_integralu(exponencialni_fce, a, b)
    print(f"    Analyticky integral: {analyticky_integral_exp}")
    print(f"    Numericky vypocet integral: {vypocet_integral_exp}\n")

    #harmonicka fce
    a = 0
    b = 2
    print("Harmonicka funkce: f(x) = sin(x) - 0.5x")
    analyticky_integral_harmonic = -np.cos(b) - 0.25 * b**2 - (-np.cos(a) - 0.25 * a**2)
    vypocet_integral_harmonic = vypocet_integralu(harmonicka_fce, a, b)
    print(f"    Analyticky integral: {analyticky_integral_harmonic}")
    print(f"    Numericky vypocet integral: {vypocet_integral_harmonic}\n")

test_metody()
