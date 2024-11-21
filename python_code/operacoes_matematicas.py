# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

def operacoes_matematicas():
    try:
        num1 = int(input("Informe o primeiro numero: "))
        num2 = int(input("Informe o segundo numero: "))
        
        print("\nEscolha uma operação a ser realizada:")
        print("1 - Adicao")
        print("2 - Subtracao")
        print("3 - Multiplicacao")
        print("4 - Divisao")
        operacao = input("Digite o número da operação desejada: ")
        
        resultado = None
        operacao_str = None
        
        if operacao == "1":
            resultado = num1 + num2
            operacao_str = "Adição"
        elif operacao == "2":
            resultado = num1 - num2
            operacao_str = "Subtração"
        elif operacao == "3":
            resultado = num1 * num2
            operacao_str = "Multiplicação"
        elif operacao == "4":
            if num2 != 0:
                resultado = num1 / num2
                operacao_str = "Divisão"
            else:
                print("Erro: Divisão por zero não é permitida")
        else:
            print("Operação inválida. Por favor, escolha uma operação válida.")
            return
        
        if operacao_str and resultado is not None:
            print(f"\nResultado da {operacao_str}: {resultado}")
    
    except ValueError:
        print("Erro: Certifique-se de que os números informados são válidos.")
        
if __name__ == "__main__":
    operacoes_matematicas()