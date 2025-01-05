import pytest
from src.verificar_palindromo import VerificadorPalindromo

def test_palindromo(monkeypatch, capsys):
    inputs = iter(["radar"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    verificador = VerificadorPalindromo()
    verificador.receber_palavra()
    verificador.verificar_palindromo()
    captured = capsys.readouterr()
    assert "A palavra radar é um palíndromo!" in captured.out

def test_nao_palindromo(monkeypatch, capsys):
    inputs = iter(["hello"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    verificador = VerificadorPalindromo()
    verificador.receber_palavra()
    verificador.verificar_palindromo()
    captured = capsys.readouterr()
    assert "A palavra hello não é um palíndromo!" in captured.out

def test_palindromo_com_espacos(monkeypatch, capsys):
    inputs = iter(["A man a plan a canal Panama"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    verificador = VerificadorPalindromo()
    verificador.receber_palavra()
    verificador.verificar_palindromo()
    captured = capsys.readouterr()
    assert "A palavra amanaplanacanalpanama é um palíndromo!" in captured.out