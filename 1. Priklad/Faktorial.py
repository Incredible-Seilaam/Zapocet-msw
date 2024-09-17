import time
import math
from scipy.special import factorial as scipy_faktorial

#faktorial pres loop
def faktorial_manual(n: int):
    if n < 0:
        raise ValueError("Faktorial je definovan pouze pro nezaporna cisla")
    vysledek = 1
    for i in range(2, n + 1):
        vysledek *= i
    return vysledek

#faktorial s Math
def faktorial_math(n: int):
    if n < 0:
        raise ValueError("Faktorial je definovan pouze pro nezaporna cisla")
    return math.factorial(n)

#faktorial se SciPy
def faktorial_scipy(n: int):
    if n < 0:
        raise ValueError("Faktorial je definovan pouze pro nezaporna cisla")
    return scipy_faktorial(n, exact=True)

def mereni_casu(fce, n):
    poc_cas = time.perf_counter()   #muzeme pouzit time.time(), ale perf_counter je presnejsi
    result = fce(n)
    konec_cas = time.perf_counter()
    cas_trvani = konec_cas - poc_cas
    return result, cas_trvani

#cislo pro vypocet faktorialu
n = 999

vysledek1, cas1 = mereni_casu(faktorial_manual, n)
vysledek2, cas2 = mereni_casu(faktorial_math, n)
vysledek3, cas3 = mereni_casu(faktorial_scipy, n)

print(f"Faktorial bez knihoven:\n- Vysledek = {vysledek1},\n- cas trvani = {cas1:.16f} sekund")
print(f"\nFaktorial s math modulem:\n- Vysledek = {vysledek2},\n- cas trvani = {cas2:.16f} sekund")
print(f"\nFaktorial se scipy:\n- Vysledek = {vysledek3},\n- cas trvani = {cas3:.16f} sekund")

if cas1 < cas2 and cas1 < cas3:
    print(f"\nManualni vypocet je rychlejsi o {min(cas2, cas3) - cas1:.16f} sekund.")
elif cas2 < cas1 and cas2 < cas3:
    print(f"\nS math modulem je rychlejsi o {min(cas1, cas3) - cas2:.16f} sekund.")
else:
    print(f"\nSe scipy je rychlejsi o {min(cas1, cas2) - cas3:.16f} sekund.")

print(f'\nU tohoto cviceni jsem narazila na problem.\nPri vypoctu faktorialu jsem zjistila, ze pouziti funkce "time.time()" nebylo dostatecne presne.\nProto byla v dalsich ulohach pouzita funkce "time.perf_counter()", ktera poskytuje lepsi presnost mereni casu.')
