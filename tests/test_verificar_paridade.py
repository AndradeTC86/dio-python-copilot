import pytest
from src.verificar_paridade import VerificadorParidade

def test_numero_par(monkeypatch, capsys):
    inputs = iter(["4"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    verificador = VerificadorParidade()
    assert verificador.receber_numero()
    verificador.verificar_paridade()
    captured = capsys.readouterr()
    assert "O número 4 é par." in captured.out

def test_numero_impar(monkeypatch, capsys):
    inputs = iter(["5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    verificador = VerificadorParidade()
    assert verificador.receber_numero()
    verificador.verificar_paridade()
    captured = capsys.readouterr()
    assert "O número 5 é impar." in captured.out

def test_entrada_invalida(monkeypatch, capsys):
    inputs = iter(["abc"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    verificador = VerificadorParidade()
    assert not verificador.receber_numero()
    captured = capsys.readouterr()
    assert "Erro: Certifique-se de que foi informado um número inteiro válido." in captured.out