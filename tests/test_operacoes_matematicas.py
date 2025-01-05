import pytest
from src.operacoes_matematicas import OperacoesMatematicas

def test_adicao(monkeypatch):
    inputs = iter(["10", "5", "1"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    operacao = OperacoesMatematicas()
    assert operacao.receber_numeros()
    operacao.escolher_operacao()
    resultado = operacao.realizar_operacao()
    assert resultado == 15

def test_subtracao(monkeypatch):
    inputs = iter(["10", "5", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    operacao = OperacoesMatematicas()
    assert operacao.receber_numeros()
    operacao.escolher_operacao()
    resultado = operacao.realizar_operacao()
    assert resultado == 5

def test_multiplicacao(monkeypatch):
    inputs = iter(["10", "5", "3"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    operacao = OperacoesMatematicas()
    assert operacao.receber_numeros()
    operacao.escolher_operacao()
    resultado = operacao.realizar_operacao()
    assert resultado == 50

def test_divisao(monkeypatch):
    inputs = iter(["10", "5", "4"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    operacao = OperacoesMatematicas()
    assert operacao.receber_numeros()
    operacao.escolher_operacao()
    resultado = operacao.realizar_operacao()
    assert resultado == 2

def test_divisao_por_zero(monkeypatch, capsys):
    inputs = iter(["10", "0", "4"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    operacao = OperacoesMatematicas()
    assert operacao.receber_numeros()
    operacao.escolher_operacao()
    operacao.realizar_operacao()
    captured = capsys.readouterr()
    assert "Erro: Divisão por zero não é permitida" in captured.out

def test_operacao_invalida(monkeypatch, capsys):
    inputs = iter(["10", "5", "5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    operacao = OperacoesMatematicas()
    assert operacao.receber_numeros()
    operacao.escolher_operacao()
    operacao.realizar_operacao()
    captured = capsys.readouterr()
    assert "Operação inválida. Por favor, escolha uma operação válida." in captured.out

def test_entrada_invalida(monkeypatch, capsys):
    inputs = iter(["dez", "5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    operacao = OperacoesMatematicas()
    assert not operacao.receber_numeros()
    captured = capsys.readouterr()
    assert "Erro: Certifique-se de que os números informados são válidos." in captured.out