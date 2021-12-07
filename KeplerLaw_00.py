# Leis de Kepler - introdução

# Bibliotecas
from math import sqrt
from time import sleep

# Funções
def olá(quem):
    sleep(0.5)
    print(f'Bom dia, {quem}')

def lei1(per, afe):
    print(f'Mais próximo: {per} milhões de km')
    sleep(0.5)
    print(f'Mais distante: {afe} milhões de km')
    ex = (afe-per)/(afe+per)
    sleep(0.5)
    print(f'Excentricidade da órbita: {ex:.4f}')
    a2 = per + afe # 2a = comprimento horizontal da elipse
    a = a2/2 
    b =int((a)*(sqrt(1-(ex**2)))) # 1/2 do comprimento vertical da elipse
    c = sqrt(a**2 - b**2) # 1/2 da distância entre os focos da elipse
    c = round(c, 2) # Arredonda o valor de c para duas casas decimais


# Programa

olá(str(input('Quem? ')))
sleep(0.5)
while True:
    sleep(0.5)
    print('''Como prosseguir: 
    [1]: Teoria
    [2]: Sair''')
    r = int(input('Opção: '))
    if r == 1:
        sleep(1)
        print('''1° Lei de Kepler:
    "Órbitas planetárias são elipses em cujo foco está o Sol"''')
        # Função da elipse
        sleep(0.5)
        print('Elipse da órbita da Terra:')
        sleep(0.5)
        lei1(147, 152)
        sleep(1)
        while True:
            res = str(input("Deseja informar outro valor? [S/N]: ")).strip().upper()[0]
            if res == 'S':
                per = int(input('Digite (milhões de km) a distância mais próxima:'))
                afe = int(input('Digite (milhões de km) a distância mais longe:'))
                sleep(1)
                lei1(per, afe)
            elif res == 'N':
                break
            else:
                print('Comando inválido')
        sleep(1)
        print('''2° Lei de Kepler:
    "O raio vetor que liga um planeta ao Sol varre áreas iguais em tempos iguais"
Essa lei implica que a velocidade areolar de um astro muda em sua órbita.''')
        sleep(1)
        print('''3° Lei de Kepler:
    "O quadrado do período de rotação de um planeta em relação ao Sol é
     proporcional ao cubo da distância entre eles.''')
        sleep(2)
        print('k, constante de Kepler, depende do corpo central.')
        sleep(1)
#       print('Tabela: Planetas x distância ao Sol (milhões de km), Período (dias)')
        tabela = {'Planeta': ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Júpiter',
                              'Saturno', 'Urano', 'Netuno'],
                  'dist': [58, 108, 149, 288, 778, 1427, 2870, 4498],
                  'tempo': [88, 243, 365, 687, 4328, 10731, 30667, 60148]}
    elif r == 2:
        break
    else:
        print('Comando inválido')
        sleep(1)
sleep(1)
print('FIM...')