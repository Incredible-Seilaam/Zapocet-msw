import time
import numpy as np

#maticovy soucin bez NumPy
def maticovy_soucin(mat1: list, mat2: list):
    rows1 = len(mat1)
    cols1 = len(mat1[0])
    rows2 = len(mat2)
    cols2 = len(mat2[0])
    
    if cols1 != rows2:
        raise Exception('Počet sloupců první matice musí být rovný počtu řádků druhé matice')

    vysledek = [[0] * cols2 for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                vysledek[i][j] += mat1[i][k] * mat2[k][j]
    
    return vysledek

#maticovy soucin s NumPy
def maticovy_soucin_np(mat1: list, mat2: list):
    np_mat1 = np.array(mat1)
    np_mat2 = np.array(mat2)
    np_vysledek = np.matmul(np_mat1, np_mat2)
    return np_vysledek.tolist()

def mereni_casu(fce, mat1, mat2):
    poc_cas = time.perf_counter()   #muzeme pouzit time.time(), ale perf_counter je presnejsi
    result = fce(mat1, mat2)
    konec_cas = time.time()
    cas_trvani = konec_cas - poc_cas
    return result, cas_trvani

mat1 = np.random.randint(100, 1000, size=(100, 100)).tolist() #generace cisel od 100 do 1000 pro viditelne vysledky
mat2 = np.random.randint(100, 1000, size=(100, 100)).tolist()

vysledek1, cas1 = mereni_casu(maticovy_soucin, mat1, mat2)
vysledek2, cas2 = mereni_casu(maticovy_soucin_np, mat1, mat2)

print(f"Maticovy soucin bez NumPy:\n- cas trvani = {cas1:.8f} sekund")
print(f"\nMaticovy soucin s NumPy:\n- cas trvani = {cas2:.8f} sekund")

if cas1 < cas2:
    print(f"\nBez NumPy je rychlejsi o {cas2 - cas1:.8f} sekund.")
else:
    print(f"\nS NumPy je rychlejsi o {cas1 - cas2:.8f} sekund.")
