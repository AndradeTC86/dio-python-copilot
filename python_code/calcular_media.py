# Descrição: Agora vamos calcular a média de três notas fornecidas na entrada do usuário. 

def calcular_media():
    try:
        nota1 = int(input("Digite a primeira nota: "))
        nota2 = int(input("Digite a segunda nota: "))
        nota3 = int(input("Digite a terceira nota: "))
        
        media = (nota1 + nota2 + nota3) / 3
        
        print(f"A média das notas é: {media:.2f}")
        
    except ValueError:
        print("Erro: Certifique-se de que os números informados são válidos.")
        

if __name__ == "__main__":
    calcular_media()

