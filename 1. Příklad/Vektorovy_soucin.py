import time
import numpy as np

# vektorovy součin bez NumPy
def vektorovy_soucin(vec1: list, vec2: list):
    if len(vec1) != len(vec2):
        raise Exception('Vektory nemají stejnou velikost')

    vec_soucin = [0] * len(vec1)

    for i in range(len(vec1)):
        vec_soucin[i] = vec1[i] * vec2[i]
    
    return vec_soucin

#vektorovy soucin s NumPy
def vektorovy_soucin_np(vec1: list, vec2: list):
    if len(vec1) != len(vec2):
        raise Exception('Vektory nemají stejnou velikost')
    
    np_vec1 = np.array(vec1)
    np_vec2 = np.array(vec2)

    vec_vysledek = np_vec1 * np_vec2
    
    return vec_vysledek.tolist()

def mereni_casu(fce, vec1, vec2):
    poc_cas = time.time()
    result = fce(vec1, vec2)
    konec_cas = time.time()
    cas_trvani = konec_cas - poc_cas
    return result, cas_trvani

vec1 = np.random.randint(1, 1000, size=1000000).tolist()
vec2 = np.random.randint(1, 1000, size=1000000).tolist()

vysledek1, cas1 = mereni_casu(vektorovy_soucin, vec1, vec2)
vysledek2, cas2 = mereni_casu(vektorovy_soucin_np, vec1, vec2)

print(f"Vektorovy soucin bez NumPy:\n- Vysledek = {vysledek1[:10]},\n- cas trvani = {cas1:.8f} sekund")  # Vypsání prvních 10 prvků pro přehlednost
print(f"\nVektorovy soucin s NumPy:\n- Vysledek = {vysledek2[:10]},\n- cas trvani = {cas2:.8f} sekund")  # Vypsání prvních 10 prvků pro přehlednost

if cas1 < cas2:
    print(f"\nBez NumPy je rychlejsi o {cas2 - cas1:.8f} sekund.")
else:
    print(f"\nS NumPy je rychlejsi o {cas1 - cas2:.8f} sekund.")
