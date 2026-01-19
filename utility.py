import numpy as np
from itertools import product

# Constantes del Modelo
ALPHA, BETA, GAMMA = 1.0, 1.0, 1.0
DELTA, THETA, LAMBDA = 0.6, 0.4, 0.5
E_MAX, T_MAX = 1.0, 1.0
FACTOR_M, FACTOR_A = 0.5, 0.5

class Ciudad:
    def __init__(self, id_c, E, R, T):
        self.id = id_c
        self.E_base = E
        self.R_base = R
        self.T = T

def calcular_utilidad(ciudad, estrategia):
    E_i = ciudad.E_base * FACTOR_M if estrategia == 'M' else ciudad.E_base
    R_i = ciudad.R_base * FACTOR_A if estrategia == 'A' else ciudad.R_base
    coop_i = 1.0 if estrategia == 'C' else 0.0
    
    B_i = DELTA * (1 - (E_i / E_MAX)) + THETA * coop_i
    C_i = LAMBDA * (1 - (ciudad.T / T_MAX))
    
    return (ALPHA * B_i) - (BETA * C_i) - (GAMMA * R_i)

ciudades = [
    Ciudad(1, 0.9, 0.6, 0.8),
    Ciudad(2, 0.7, 0.4, 0.6),
    Ciudad(3, 0.4, 0.8, 0.3)
]

estrategias = ['A', 'M', 'C']
perfiles = list(product(estrategias, repeat=3))

print(f"{'PERFIL':<15} | {'U1':<6} {'U2':<6} {'U3':<6} | NASH")
print("-" * 50)

for perfil in perfiles:
    utilidades = [calcular_utilidad(c, perfil[i]) for i, c in enumerate(ciudades)]
    es_nash = True
    
    for i, ciudad in enumerate(ciudades):
        for s_alt in estrategias:
            if s_alt != perfil[i]:
                if calcular_utilidad(ciudad, s_alt) > utilidades[i]:
                    es_nash = False
                    break
        if not es_nash: break
            
    if es_nash:
        print(f"{str(perfil):<15} | {utilidades[0]:.3f}  {utilidades[1]:.3f}  {utilidades[2]:.3f}  | SI")
