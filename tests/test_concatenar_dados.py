import pytest
from src.concatenar_dados import ConcatenadorDados

def test_concatenar_dados(monkeypatch):
    inputs = iter(["primeiro", "segundo"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    concatenador = ConcatenadorDados()
    concatenador.receber_dados()
    resultado = concatenador.concatenar_dados()
    assert resultado == "primeiro segundo"

def test_concatenar_dados_vazio(monkeypatch):
    inputs = iter(["", ""])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    concatenador = ConcatenadorDados()
    concatenador.receber_dados()
    resultado = concatenador.concatenar_dados()
    assert resultado == " "

def test_exibir_resultado(monkeypatch, capsys):
    inputs = iter(["primeiro", "segundo"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    concatenador = ConcatenadorDados()
    concatenador.receber_dados()
    concatenador.exibir_resultado()
    captured = capsys.readouterr()
    assert captured.out == "O resultado concatenado é: primeiro segundo\n"