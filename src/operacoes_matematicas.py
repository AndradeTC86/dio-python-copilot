# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

class OperacoesMatematicas:
    def __init__(self):
        self.num1 = None
        self.num2 = None
        self.operacao = None

    def receber_numeros(self):
        try:
            self.num1 = int(input("Informe o primeiro numero: "))
            self.num2 = int(input("Informe o segundo numero: "))
        except ValueError:
            print("Erro: Certifique-se de que os números informados são válidos.")
            return False
        return True

    def escolher_operacao(self):
        print("\nEscolha uma operação a ser realizada:")
        print("1 - Adicao")
        print("2 - Subtracao")
        print("3 - Multiplicacao")
        print("4 - Divisao")
        self.operacao = input("Digite o número da operação desejada: ")

    def realizar_operacao(self):
        resultado = None
        operacao_str = None

        if self.operacao == "1":
            resultado = self.num1 + self.num2
            operacao_str = "Adição"
        elif self.operacao == "2":
            resultado = self.num1 - self.num2
            operacao_str = "Subtração"
        elif self.operacao == "3":
            resultado = self.num1 * self.num2
            operacao_str = "Multiplicação"
        elif self.operacao == "4":
            if self.num2 != 0:
                resultado = self.num1 / self.num2
                operacao_str = "Divisão"
            else:
                print("Erro: Divisão por zero não é permitida")
                return
        else:
            print("Operação inválida. Por favor, escolha uma operação válida.")
            return

        if operacao_str and resultado is not None:
            print(f"\nResultado da {operacao_str}: {resultado}")
        return resultado

if __name__ == "__main__":
    operacao = OperacoesMatematicas()
    if operacao.receber_numeros():
        operacao.escolher_operacao()
        operacao.realizar_operacao()