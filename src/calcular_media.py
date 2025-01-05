# Descrição: Agora vamos calcular a média de três notas fornecidas na entrada do usuário. 

class CalculadoraMedia:
    def __init__(self):
        self.notas = []

    def adicionar_nota(self, nota):
        try:
            nota = float(nota)
            self.notas.append(nota)
        except ValueError:
            raise ValueError("A nota deve ser um número.")

    def calcular_media(self):
        if len(self.notas) != 3:
            raise ValueError("Devem ser fornecidas três notas para calcular a média.")
        return sum(self.notas) / 3

if __name__ == "__main__":
    calculadora = CalculadoraMedia()
    try:
        for i in range(1, 4):
            nota = input(f"Digite a {i}ª nota: ")
            calculadora.adicionar_nota(nota)
        media = calculadora.calcular_media()
        print(f"A média das notas é: {media:.2f}")
    except ValueError as e:
        print(f"Erro: {e}")