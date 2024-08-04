from colorama import init, Fore, Style
from copy import deepcopy

def verificar_matriz(matriz, tamanho_linha, tamanho_coluna):
    # True: Matriz funciona
    # False: f"Matriz incorreta, celula_tal"
    matriz_copia = deepcopy(matriz)
    for lin in range(tamanho_linha):
        for col in range(tamanho_coluna):
   
            if ((lin + 1) > tamanho_linha - 1):
                celula3 = matriz[0][col]
            else:
                celula3 = matriz[lin + 1][col]
                
            if ((col + 1) > tamanho_coluna - 1):
                celula2 = matriz[lin][0]
            else:
                celula2 = matriz[lin][col + 1]
                
            celula = matriz[lin][col]

            if ((verificar_diferencas(celula, celula2)) or (verificar_diferencas(celula, celula3))):
                matriz_copia[lin][col] = f"{Fore.RED}{celula}{Style.RESET_ALL}"
            else:
                matriz_copia[lin][col] = f"{Fore.WHITE}{celula}{Style.RESET_ALL}"
    
    for i in matriz_copia:
        print(f"[{', '.join(i)}]")
        

def verificar_diferencas(celula, celula2):
    # True: celula != celula2
    # False: celula == celula
    diferencas = 0
    for i in range(len(celula)):
        if celula[i] != celula2[i]:
            diferencas += 1
            if diferencas > 1:
                return True
    return False

init()

print("-- Gerador de Mapa de Karnaught --\n")

while (True):
    escolha = int(input("\n[1] USAR\n[0] SAIR: "))
    
    if escolha == 0:
        print("\nEncerrando...")
        break
            
    elif escolha == 1:
        linhas = input(f"-Valores das linhas -\n")
        colunas = input(f"--Valores das colunas\n")
        linha =  []
        coluna = []
        matriz = []
        linha = linhas.split(" ")
        coluna = colunas.split(" ")
        tamanho_linha = len(linha)
        tamanho_coluna = len(coluna)
        
        for i in range(tamanho_linha):
            matriz.append([])
            for j in range(tamanho_coluna):
                matriz[i] = [0] * tamanho_coluna
        for i in range(tamanho_linha):
            for j in range(tamanho_coluna):
                matriz[i][j] = linha[i] + coluna[j]
        print("\n")
        
    verificar_matriz(matriz, tamanho_linha, tamanho_coluna)
    