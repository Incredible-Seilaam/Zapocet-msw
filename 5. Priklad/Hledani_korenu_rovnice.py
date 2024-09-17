import math
from scipy.optimize import bisect, newton
import time


def polynomialni_fce(x):
    return x**4 - 8*x**3 + 18*x**2 - 12*x + 1

def exponencialni_fce(x):
    return math.exp(x) - 2

def harmonicka_fce(x):
    return math.sin(x) - x**3 + 0.1*x

def ohran_metoda(func, a, b):   # ohranicena metoda: puleni intervalu
    start_time = time.time()
    koren = bisect(func, a, b)
    end_time = time.time()
    return koren, end_time - start_time

def neohran_metoda(func, x0):   # neohranena metoda: Newtonova metoda
    start_time = time.perf_counter()
    koren = newton(func, x0)
    end_time = time.perf_counter()
    return koren, end_time - start_time

def porovnani(func, a, b, x0):
    print(f"\nFunkce: f(x) = {func.__doc__}")

    koren_ohran, cas_ohran = ohran_metoda(func, a, b)
    presnost_ohran = abs(func(koren_ohran))
    print(f"    Metoda puleni intervalu:")
    print(f"        Koren = {koren_ohran}")
    print(f"        Cas = {cas_ohran:.8f} s")
    print(f"        Presnost (f(koren)) = {presnost_ohran:.8e}")

    koren_newton, cas_newton = neohran_metoda(func, x0)
    presnost_newton = abs(func(koren_newton))
    print(f"    Newtonova metoda:")
    print(f"        Koren = {koren_newton}")
    print(f"        Cas = {cas_newton:.8f} s")
    print(f"        Presnost (f(koren)) = {presnost_newton:.8e}")

def test_metod():
    polynomialni_fce.__doc__ = "x^4 - 8x^3 + 18x^2 - 12x + 1"   #polynomialni fce
    porovnani(polynomialni_fce, 0, 3, 2)
    
    exponencialni_fce.__doc__ = "e^x - 2"   #exponencialni fce
    porovnani(exponencialni_fce, 0, 2, 1)
    
    harmonicka_fce.__doc__ = "sin(x) - x^3 + 0.1x"  #harmonicka fce
    porovnani(harmonicka_fce, 0, 2, 1)

test_metod()
