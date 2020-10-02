import numpy as np

num_de_suportes=input('Insira a qtd de suportes/fixações:')
var_momentum=[]
var_torque=[]
var_fx=[]
var_fy=[]
for i in range(num_de_suportes):
    print('1 - Fixo\n2 - Pino\n 3 - Rolete')
    tipo=input('Qual o {.f}-ésimo tipo:')
    if(tipo==1):
        var_momentum+=[0]
        var_torque+=[0]
        var_fx+=[0]
        var_fy+=[0]
    elif(tipo==2):
        var_torque+=[0]
        var_fx+=[0]
        var_fy+=[0]
    else:
        var_fy+=[0]
    
num_force_x=input('Insira qtd de forças no eixo x:')
print('Assumindo que o a origem do plano cartesiano está na extremidade esquerda da viga e que a esquerda representa o semi-eixo negativo e a direita representa o semi-eixo positivo')
for i in range(num_force_x):
    force_x+=input('{.f}-ésima força x:')
    dist=input('A que distância da origem está essa força? (para cálculo de momentos)')
    momentum+=dist*force_x[len(force_x)-1]

num_force_y=input('Insira qtd de forças no eixo y:')
print('Assumindo que o a origem do plano cartesiano está na extremidade esquerda da viga e que para baixo temos o semi-eixo negativo e para cima o semi-eixo positivo')
for i in range(num_force_y):
    force_y+=input('{.f}-ésima força y:')
    dist=input('A que distância da origem está essa força? (para cálculo de momentos)')
    momentum+=dist*force_y[[len(force_y)-1]

num_angular_force=input('Insira qtd de forças que fazem ângulo com algum eixo:')
for i in range(num_angular_force):
    force=input('Módulo da força:')
    theta=input('Ângulo:')
    eixo=input('Com o eixo:')
    if(eixo=='x'):
        force_x+=[math.cos(theta)*force]
        dist=input('A que distância da origem está a componente x dessa força? (para cálculo de momentos)')
        momentum+=dist*force_x[[len(force_x)-1]

        force_y+=[math.sin(theta)*force]
        dist=input('E a componente y?')
        momentum+=dist*force_y[[len(force_y)-1]
    else:
        force_x+=[math.sin(theta)*force]
        dist=input('A que distância da origem está a componente x dessa força? (para cálculo de momentos)')
        momentum+=dist*force_x[[len(force_x)-1]

        force_y+=[math.cos(theta)*force]
        dist=input('A que distância da origem está a componente x dessa força? (para cálculo de momentos)')
        momentum+=dist*force_y[[len(force_y)-1]

num_torque=input('Insira qtd de torques agindo no sistema:')
print('Assumindo que torques com eixo orientado para esquerda são negativos e para direita são positivos')
for i in range(num_torque):
    torque+=input('{.f}-ésimo torque:')

