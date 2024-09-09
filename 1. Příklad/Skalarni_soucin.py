import time
import numpy as np

#skalární součin bez NumPy
def skalar_souc(vec1: list, vec2: list):
    if len(vec1) != len(vec2):
        raise Exception('Vektory nemají stejnou velikost')
    
    vec_soucin = 0
    for i in range(len(vec1)): #vektory jsou tsjně dlouhé
        vec_soucin += vec1[i] * vec2[i]
    return vec_soucin

def skalar_souc_np(vec1: list, vec2: list):
    if len(vec1) != len(vec2):
        raise Exception('Vektory nemají stejnou velikost')
    
    vec_vysledek = np.dot(vec1, vec2)
    return vec_vysledek

def mereni_casu(fce, vec1, vec2):
    poc_cas = time.time()
    result = fce(vec1, vec2)
    konec_cas = time.time()
    cas_trvani = konec_cas - poc_cas
    return result, cas_trvani

vec1 = np.random.randint(1, 1000, size=1000000).tolist()
vec2 = np.random.randint(1, 1000, size=1000000).tolist()

vysledek1, cas1 = mereni_casu(skalar_souc, vec1, vec2)
vysledek2, cas2 = mereni_casu(skalar_souc_np, vec1, vec2)

# Výstup a porovnání
print(f"Skalarni soucin bez NumPy:\n- Vysledek = {vysledek1},\n- cas trvani = {cas1:.8f} sekund")
print(f"\nSkalarni soucin s NumPy:\n- Vysledek = {vysledek2},\n- cas trvani = {cas2:.8f} sekund")

if cas1 < cas2:
    print(f"\nBez NumPy je rychlejsi o {cas2 - cas1:.8f} sekund.")
else:
    print(f"\nS NumPy je rychlejsi o {cas1 - cas2:.8f} sekund.")