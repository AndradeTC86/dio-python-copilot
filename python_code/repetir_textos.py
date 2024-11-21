# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

def repetir_textos():
    try:
        texto = input("Informe o texto a ser repetido: ")
        repeticoes = int(input("Informe o número de vezes que o número deve ser repetido: "))
        
        resultado = (texto + "\n") * repeticoes
        
        print(resultado)
        
    except ValueError:
        print("Erro: Certifique-se de que o número de vezes é um valor inteiro.")

if __name__ == "__main__" :
    repetir_textos()
    
    