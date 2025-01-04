# Descrição: Vamos testar se uma palavra é um palíndromo?!

def verificar_palindromo():
    palavra = input("Digite uma palavra: ")
    
    palavra = palavra.replace("", "").lower()
    
    palavra_invertida = palavra[::-1]
    
    if palavra == palavra_invertida:
        print(f"A palavra {palavra} é um palíndromo!")
    else:
        print(f"A palavra {palavra} não é um palíndromo!")
        
    
if __name__ == "__main__":
    verificar_palindromo()