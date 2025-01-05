import pytest
from src.repetir_textos import RepetidorTextos

def test_repetir_texto(monkeypatch):
    inputs = iter(["hello", "3"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    repetidor = RepetidorTextos()
    assert repetidor.receber_dados()
    resultado = repetidor.repetir_texto()
    assert resultado == "hello\nhello\nhello\n"

def test_repetir_texto_zero(monkeypatch):
    inputs = iter(["hello", "0"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    repetidor = RepetidorTextos()
    assert repetidor.receber_dados()
    resultado = repetidor.repetir_texto()
    assert resultado == ""

def test_entrada_invalida(monkeypatch, capsys):
    inputs = iter(["hello", "three"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    repetidor = RepetidorTextos()
    assert not repetidor.receber_dados()
    captured = capsys.readouterr()
    assert "Erro: Certifique-se de que o número de vezes é um valor inteiro." in captured.out