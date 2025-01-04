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
    with pytest.raises(ValueError):
        calculadora.adicionar_nota("nota invalida")

def test_calcular_media_notas_insuficientes():
    calculadora = CalculadoraMedia()
    calculadora.adicionar_nota(7)
    calculadora.adicionar_nota(8)
    with pytest.raises(ValueError):
        calculadora.calcular_media()