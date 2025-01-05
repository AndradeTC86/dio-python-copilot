# Descrição: Vamos testar se uma palavra é um palíndromo?!

class VerificadorPalindromo:
    def __init__(self):
        self.palavra = ""

    def receber_palavra(self):
        self.palavra = input("Digite uma palavra: ").replace(" ", "").lower()

    def verificar_palindromo(self):
        palavra_invertida = self.palavra[::-1]
        if self.palavra == palavra_invertida:
            print(f"A palavra {self.palavra} é um palíndromo!")
        else:
            print(f"A palavra {self.palavra} não é um palíndromo!")

if __name__ == "__main__":
    verificador = VerificadorPalindromo()
    verificador.receber_palavra()
    verificador.verificar_palindromo()