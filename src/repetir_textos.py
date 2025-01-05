# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

class RepetidorTextos:
    def __init__(self):
        self.texto = ""
        self.repeticoes = 0

    def receber_dados(self):
        try:
            self.texto = input("Informe o texto a ser repetido: ")
            self.repeticoes = int(input("Informe o número de vezes que o texto deve ser repetido: "))
        except ValueError:
            print("Erro: Certifique-se de que o número de vezes é um valor inteiro.")
            return False
        return True

    def repetir_texto(self):
        return (self.texto + "\n") * self.repeticoes

    def exibir_resultado(self):
        resultado = self.repetir_texto()
        print(resultado)

if __name__ == "__main__":
    repetidor = RepetidorTextos()
    if repetidor.receber_dados():
        repetidor.exibir_resultado()