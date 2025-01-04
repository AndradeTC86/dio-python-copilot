# Descrição: Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. 

def verificar_paridade():
    try:
        numero = int(input("Informe o número a ser verificado: "))
        
        if numero %2 == 0:
            print(f"O número {numero} é par.")
        else:
            print(f"O número {numero} é impar.")
    
    except ValueError:
        print("Erro: Certifique-se de que foi informado um número inteiro válido.")
        
if __name__ == "__main__":
    verificar_paridade()