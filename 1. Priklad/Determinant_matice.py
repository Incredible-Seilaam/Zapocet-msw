import time
import numpy as np
import scipy
from random import randint

import warnings #pro přehlednost outputu programu
warnings.filterwarnings("ignore", category=RuntimeWarning)  #ignoruje runtime warning spojený s problémem přetékání

def vytvor_matici(rows, cols):
    matice = np.random.randint(1, 100, size=(rows, cols))
    return matice

def determinant(matice):
    if len(matice) != len(matice[0]):
        raise Exception("Spatne zadana matice")
    if len(matice) == 2:
        return matice[0, 0] * matice[1, 1] - matice[0, 1] * matice[1, 0]

    det = 0
    for i in range(len(matice)):
        minor = np.delete(matice, 0, axis=0)
        minor = np.delete(minor, i, axis=1)
        cofactor = (-1) ** i * matice[0, i] * determinant(minor)
        det += cofactor
    return det

def determinant_numpy(matice):
    return np.linalg.det(matice)

def determinant_scipy(matice):
    return scipy.linalg.det(matice)

def mereni_casu(fce, matice):
    poc_cas = time.process_time()
    vysledek = fce(matice)
    konec_cas = time.process_time()
    cas_trvani = konec_cas - poc_cas
    return vysledek, cas_trvani

def test(funcs, matice):
    casy = []
    for func in funcs:
        vysledek, ex_time = mereni_casu(func, matice)
        print(f"{func.__name__}: {vysledek}, cas: {ex_time:.8f} sekund")
        casy.append((func.__name__, ex_time))
    
    print(f"\nSerazeno podle rychlosti: {sorted(casy, key=lambda x: x[1])}")

matice = vytvor_matici(10, 10)

test([determinant, determinant_numpy, determinant_scipy], matice)

print(f'\nPrikladova matice:\n{matice}')
print('\nPri vlastni implementaci dochazi k problemum s pretecenim,\nzpusobeno tim, ze vypocty v rekurzivnim algoritmu mohou rychle rust do velmi velkych cisel.\nZ tohoto duvovu je vlastni implementace vyrazne pomalejsi nez NumPy a SciPy')