# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string

def concatenar_dados():
    dado1 = input("Digite o primeiro dado: ")
    dado2 = input("Digite o segundoo dado: ")
    
    resultado = dado1 + " " + dado2
    
    print(f"O resultado concatenado é: {resultado}")
    
if __name__ == "__main__" :
    concatenar_dados()        