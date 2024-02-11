from API.Projeto.main_fast_API import home, venda, venda_especifica
from pytest import mark

def test_home():
    esperado = 'ou galerinha'
    resultado = home()
    assert  resultado == esperado

def test_venda():
    esperado = {'Vendas': 4}
    resultado = venda()
    assert  resultado == esperado

def test_venda_especifica():
    # entrada = 1
    # esperado = {'item': 'lata', 'preco_unitario': 4, 'quantidade': 5}
    # resultado = venda_especifica(entrada)
    # assert  resultado == esperado

    assert venda_especifica(1) == {'item': 'lata', 'preco_unitario': 4, 'quantidade': 5}

@mark.skip(reason='WIP')
def test_mark_pytest():
    assert  venda() == {'Vendas': 4}