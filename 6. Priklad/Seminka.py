import random
import os
import hashlib
import socket
import time
import matplotlib.pyplot as plt
import numpy as np
from pynput import mouse, keyboard

mouse_data = []
key_data = []   #seznamy pro uchovávání dat
timestamps = []

def on_move(x, y): #pohyby myši
    timestamp = time.time()
    mouse_data.append((x, y))
    timestamps.append(timestamp)

def on_click(x, y, button, pressed): #pohyby klavesnice
    if not pressed:
        return False

def on_press(key):
    try:
        key_data.append((key.char, time.time()))
    except AttributeError:
        key_data.append((str(key), time.time()))

# Funkce pro získání semínek
def GetSeeds():
    #1 - systémový čas
    s1 = int(time.time())
    #2 - náhodné číslo
    s2 = random.randint(0, 1000000)
    #3 - hašování pohybů myši a stisků kláves
    combined_data = ''.join([f"{x}{y}{t}" for (x, y), t in zip(mouse_data, timestamps)])
    combined_data += ''.join([f"{key}{t}" for key, t in key_data])
    s3 = int(hashlib.md5(combined_data.encode()).hexdigest(), 16)
    #4 - číslo procesu
    s4 = os.getpid()
    #5 - síťové informace
    hname = socket.gethostname()
    s5 = hash(hname + socket.gethostbyname(hname))
    #6 - systémové proměnné
    env_str = ''.join(os.environ.get(key, '') for key in os.environ)
    s6 = hash(env_str)
    
    return s1, s2, s3, s4, s5, s6

def Generator(seminko): #generování náhodných čísel
    random.seed(seminko)
    return [random.randint(0, 100) for _ in range(100)]

def Generate_numbers(): #vykreslení grafu
    seminka = GetSeeds()
    colors = ['Crimson', 'DarkOrange', 'Gold', 'Green', 'RoyalBlue', 'Indigo']
    
    for i, seminko in enumerate(seminka):
        numbers = Generator(seminko)
        x_values = range(len(numbers))
        plt.scatter(x_values, numbers, color=colors[i], label=f"Semínko {i+1}")
    
    plt.xlabel('Iterace generace')
    plt.ylabel('Hodnota 0-100')
    plt.title('Generovaná náhodná čísla z různých semínek')
    
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.) #legenda mimo graf
    
    plt.tight_layout()  #úprava rozvržení, aby se všechno vešlo
    plt.show()

with mouse.Listener(on_move=on_move, on_click=on_click) as mouse_listener, \
    keyboard.Listener(on_press=on_press) as keyboard_listener:
    print("Pohybujte mysi a stisknete klavesy.\nKliknete mysi pro ukonceni sledovani.")
    mouse_listener.join()
    keyboard_listener.stop()

Generate_numbers()
