import matplotlib.pyplot as plt
#@author thug
#m = c*(1+i)**n
#m = montante, c = capital inicial, i = taxa de juros, n = tempo de aplicação, j = juros compostos
#crie um programa que imprime o montante final de cada investidor após um periodo de 3 anos.
#dicionario investidor1, que tem 3 chaves, sendo uma delas um outro dicionario, esse dicionario como o nome investimentos guarda informaçoes sobre o investidor joao.
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
#dicionario investidor2, que tem 3 chaves, sendo uma delas um outro dicionario, esse dicionario como o nome investimentos guarda informaçoes sobre a investidora maria.
investidor2 = {
    'nome':'Maria',
    'capital':8000,
    'investimentos': {
        'CDB':0.1,
        'ACOES':0.7,
        'FII':0.2
    }
}
#dicionario taxas, que tem 5 chaves e seus respectivos valores atribuidos as taxas de juros de cada aplicação.
taxas = {
    'CDB':'0.01',
    'LCI':'0.02',
    'FII':'0.09',
    'LCA':'0.03',
    'ACOES':'1'
}
#essaa função sem parametros chamada contas vai fazer os calculos para saber o montante de cada investidor em cada aplicação e após isso imprimi-las.
def contas():
    for i, investidor in enumerate([investidor1, investidor2]):
        nome = investidor['nome']
        capital = investidor['capital']
        print(f"Investidor: {nome}")
        print(f"Capital inicial: {capital}")
        total = 0
        for investimento, porcentagem in investidor['investimentos'].items():
            taxa = float(taxas[investimento])
            montante = capital * (1 + taxa) ** 3 * porcentagem
            total += montante
            print(f"Montante em {investimento}: {montante:.2f}")

        print(f"Montante após 3 anos: {total:.2f}")
        print()
#essa função sem parametros serve para criar um grafico usando a biblioteca matplotlib.
def plotar_graficos():
    nomes = []
    antes = []
    depois = []

    for i, investidor in enumerate([investidor1, investidor2]):
        nome = investidor['nome']
        capital = investidor['capital']

        total = 0
        for investimento, porcentagem in investidor['investimentos'].items():
            taxa = float(taxas[investimento])
            montante = capital * (1 + taxa) ** 3 * porcentagem
            total += montante

        
        nomes.append(nome)
        antes.append(capital)
        depois.append(total)

    fig, ax = plt.subplots()
    ax.bar(nomes, depois, label='Depois')
    ax.bar(nomes, antes, label='Antes')

    plt.xlabel("Investidor")
    plt.ylabel("Montante")
    plt.title("Comparação Antes e Depois do Investimento")
    plt.legend()
    plt.show()
#esa função sem parametros cria uma tabela contendo todas informações e alguns comparativos.
def tabela():
    print("Investidor | Aplicação | Antes | Depois | Diferença")
    print("----------------------------------------------------------------------")
    for i, investidor in enumerate([investidor1, investidor2]):
        nome = investidor['nome']
        capital = investidor['capital']
        for investimento, porcentagem in investidor['investimentos'].items():
            taxa = float(taxas[investimento])
            juros = float(porcentagem) * capital
            montante = capital * (1 + taxa) ** 3 * porcentagem
            diferenca = montante - juros
            print(f"{nome:<15} | {investimento:<10} | {juros:<10.2f} | {montante:<10.2f} | {diferenca:<10.2f}")
        print("----------------------------------------------------------------------")
import matplotlib.pyplot as plt

def plotar_graficos_pizza():
    for i, investidor in enumerate([investidor1, investidor2]):
        nome = investidor['nome']
        capital = investidor['capital']
        
        labels = []
        sizes = []
        
        for investimento, porcentagem in investidor['investimentos'].items():
            taxa = float(taxas[investimento])
            juros = float(porcentagem) * capital
            montante = capital * (1 + taxa) ** 3 * porcentagem
            labels.append(investimento)
            sizes.append(montante * 100)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
        ax1.axis('equal')  
        plt.title(f"Investimentos de {nome}")
        plt.show()

contas()
tabela()
plotar_graficos()
plotar_graficos_pizza()