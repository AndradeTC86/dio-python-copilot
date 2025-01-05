# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string

class ConcatenadorDados:
    def __init__(self):
        self.dado1 = ""
        self.dado2 = ""

    def receber_dados(self):
        self.dado1 = input("Digite o primeiro dado: ")
        self.dado2 = input("Digite o segundo dado: ")

    def concatenar_dados(self):
        return f"{self.dado1} {self.dado2}"

    def exibir_resultado(self):
        resultado = self.concatenar_dados()
        print(f"O resultado concatenado é: {resultado}")

if __name__ == "__main__":
    concatenador = ConcatenadorDados()
    concatenador.receber_dados()
    concatenador.exibir_resultado()