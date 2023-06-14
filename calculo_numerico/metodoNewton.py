from numpy import log as ln
import math

# --- CONSTANTES ----
V = 6          # Tensão da fonte (6 Volts)
T = 300        # Temperatura em Kelvin (300 K)
K = 1.38e-23   # Boltzmann cte (1.38 x 10^-23 J/K)
E = 1.602e-19  # Carga e (1.602 x 10^-19 C)
IS = 2e-3      # Corrente de saturação (2m A)
R = 330        # Resistência do resistor (330 Ω)
ERRO = 1e-4    # Erro geral 

''' ---- Lei de Kirchhoff das malhas ----
  -V + VD + VR = 0
   
  - V é um valor absoluto
  - VD é um valor dado em função de constantes (conhecidas) e i (corrente do circuito)
  - VR é um valor dado em função de uma constante e i (corrent do circuito)
  
  Neste caso, queremos o zero da função -V + VD + VR, que tem como variável a corrente do circuito
'''

# Função obtida pela Lei de Kirchhoff
def f(i):
  VFonte = -V
  VDiodo = K * T * ln( (i / IS) + 1 ) / E
  VResistor = R * i

  # (f em função da corrente i)
  return VFonte + VDiodo + VResistor  

def f_derivada(x):  #define a derivada

    # Defina aqui a derivada da função
  return K*T/(E * (x+IS)) + R

def metodo_newton(aprox_inicial, tolerancia):

    x = aprox_inicial   #define o x inicial na função
    iteracoes = 0
    while True:
      iteracoes += 1  #numero de iteraçoes
      x_anterior = x
      x = x_anterior - f(x_anterior) / f_derivada(x_anterior) #calcula o x da iteração
      if abs(x - x_anterior) < tolerancia:  #verifica o criterio de parada
        break
    print("numero de iterações = ",iteracoes)
    return x

erro = 1e-4
aprox_inicial = 1.5 #valor 
tolerancia = ERRO

raiz_aproximada = metodo_newton(aprox_inicial, tolerancia)  #chama a função para o método
print("Raiz aproximada:", raiz_aproximada)    #printa a raiz encontrada

