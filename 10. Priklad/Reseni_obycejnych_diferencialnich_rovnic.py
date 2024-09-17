#soustavu pro modelování cirkulace atmosféry pomocí Lorenzova systému

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#parametry
sigma = 10
rho = 28
beta = 8/3

def lorenz(y, t):
    x, y, z = y
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

#casove kroky
t = np.linspace(0, 50, 10000)

#pocatecni podminky
y0 = [1, 0, 0]

#reseni
solution = odeint(lorenz, y0, t)
x, y, z = solution.T

#grafy
plt.figure(figsize=(12, 6))

# Graf x, y a z v case
plt.subplot(1, 2, 1)
plt.plot(t, x, label='x')
plt.plot(t, y, label='y')
plt.plot(t, z, label='z')
plt.xlabel('Čas')
plt.ylabel('Hodnota')
plt.legend()
plt.title('Časový vývoj')

#graf fazoveho prostoru x-y a x-z
plt.subplot(1, 2, 2)
plt.plot(x, y, label='x-y')
plt.plot(x, z, label='x-z')
plt.xlabel('x')
plt.ylabel('y/z')
plt.legend()
plt.title('Fázový prostor')
plt.grid()

plt.tight_layout()
plt.show()

print("Lorenzuv system se pouziva k modelovani atmosferickych konvekci a je znamy svou citlivosti na pocatecni podminky a chaotickym chovanim. Tento system jsem si vybrala predevsim kvuli moznosti vytvaret vyrazne a dobre vykreslene grafy.")
