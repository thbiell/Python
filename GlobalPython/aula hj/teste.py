investidor1 = {
    'nome':'João',
    'capital':10000,
    'investimentos': {
        'CDB':0.35,
        'ACOES':0.12,
        'LCA':0.33,
        'LCI':0.20
    }
}

investidor2 = {
    'nome':'Maria',
    'capital':8000,
    'investimentos': {
        'CDB':0.01,
        'ACOES':0.7,
        'FII':0.2
    }
}
taxas = {
    'CDB':'0.01',
    'LCI':'0.02',
    'FII':'0.09',
    'LCA':'0.03',
    'ACOES':'1'
}

def calcular_montante_acumulado(investidor, anos):
    capital = investidor['capital']
    for tipo, percentual in investidor['investimentos'].items():
        capital = capital * (1 + percentual)**anos
    return capital

investidores = [investidor1, investidor2]
anos = 3

for investidor in investidores:
    nome = investidor['nome']
    montante = calcular_montante_acumulado(investidor, anos)
    print(f"O montante acumulado em capital pelo {nome} daqui a {anos} anos é de R$ {montante:.2f}")