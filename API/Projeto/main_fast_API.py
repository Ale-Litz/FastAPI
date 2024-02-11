from fastapi import FastAPI

app = FastAPI()
# save and run the app in your computer with: 'python -m uvicorn main:app --reload'

vendas = {
    1: {'item': 'lata', 'preco_unitario': 4, 'quantidade': 5},
    2: {'item': 'garrafa', 'preco_unitario': 10, 'quantidade': 5},
    3: {'item': 'jarro', 'preco_unitario': 12, 'quantidade': 5},
    4: {'item': 'latao', 'preco_unitario': 25, 'quantidade': 5},
}


@app.get('/')
def home():
    return 'ou galerinha'

@app.get('/vendas')
def venda():
    return {'Vendas': len(vendas)}

@app.get('/vendas/{venda_especifica}')
def venda_especifica(venda_especifica:int):
    return vendas[venda_especifica]