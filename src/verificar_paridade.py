# Descrição: Como entrada, receba um número inteiro e verifique se ele é par ou ímpar.

class VerificadorParidade:
    def __init__(self):
        self.numero = None

    def receber_numero(self):
        try:
            self.numero = int(input("Informe o número a ser verificado: "))
            return True
        except ValueError:
            print("Erro: Certifique-se de que foi informado um número inteiro válido.")
            return False

    def verificar_paridade(self):
        if self.numero % 2 == 0:
            print(f"O número {self.numero} é par.")
        else:
            print(f"O número {self.numero} é impar.")

if __name__ == "__main__":
    verificador = VerificadorParidade()
    if verificador.receber_numero():
        verificador.verificar_paridade()