import pytest
from src.calcular_media import CalculadoraMedia

def test_calcular_media():
    calculadora = CalculadoraMedia()
    calculadora.adicionar_nota(6)
    calculadora.adicionar_nota(7)
    calculadora.adicionar_nota(8)
    assert calculadora.calcular_media() == 7

def test_adicionar_nota_invalida():
    calculadora = CalculadoraMedia()
    with pytest.raises(ValueError, match="A nota deve ser um número."):
        calculadora.adicionar_nota("A")


def test_calcular_media_notas_insuficientes():
    calculadora = CalculadoraMedia()
    calculadora.adicionar_nota(7)
    calculadora.adicionar_nota(8)
    with pytest.raises(ValueError, match="Devem ser fornecidas três notas para calcular a média."):
        calculadora.calcular_media()

def test_calcular_media_sem_notas():
    calculadora = CalculadoraMedia()
    with pytest.raises(ValueError, match="Devem ser fornecidas três notas para calcular a média."):
        calculadora.calcular_media()

def test_calcular_media_mais_de_tres_notas():
    calculadora = CalculadoraMedia()
    calculadora.adicionar_nota(6)
    calculadora.adicionar_nota(7)
    calculadora.adicionar_nota(8)
    calculadora.adicionar_nota(9)
    with pytest.raises(ValueError, match="Devem ser fornecidas três notas para calcular a média."):
        calculadora.calcular_media()