def geraLista():
    #essa função não recebe parametros, e nem faz nada demais, ela só serve para retornar a lista, para o mesmo não ser uma variavvel global.
    lista = []
    return lista
def cadastro(lista):
    #essa função atende o 1 item do menu, sendo ela cadastrar um dicionario que recebe por referencia o mês-ano, total de habitantes e o total de óbitos, enquanto da um append() na lista que recebeu por parametro da geraLista(), retornando a mesma.
    print('CADASTRANDO MÊS-ANO DE REFERÊNCIA!!')
    lista.append({
    'mês-ano': input('Digite o mês-ano no formato:(mm-aaaa): '),
    'Total de habitantes' : int(input('Total de habitantes: ')),
    'Total de óbitos' : int(input('Total de óbitos: '))
    })
    #print(lista)
    print('***** Gravado com sucesso *****')
    return lista
def buscar(lista):
    #essa função atende o segundo item do menu que é buscar um mês-ano especifico, isso se existir, caso exista ele printa o mês solicitado e uma mensagem que foi encontrado, caso não esteja cadastrado o mesmo printa uma mensagem dizendo que não fora encontrado.
    print('CONSULTANDO MÊS-ANO DE REFERÊNCIA!!')
    m = input('Digite o mês-ano no formato:(mm-aaaa): ')
    for i in lista:
        if m == i['mês-ano']:
            print(f"***** Registro encontrado *****\n", i)
        else:
            print('***** Mês-ano não cadastrado! *****')
def listaMVP():
    #essa função não recebe parametros, e nem faz nada demais, ela só serve para retornar a listamvp, para o mesmo não ser uma variavvel global.
    listamvp = []
    return listamvp
def cadastroMVP(listamvp):
    #essa função recebe uma lista, faz os appends e retorna essa lista, tem como função cadastrar um usuario no site.
    novoUsuario = []
    nome = input('Digite seu nome:')
    idade = input('Digite sua idade:')
    login = input('Digite o que vai ser seu login:')
    senha = input('Digite a sua senha:')
    novoUsuario.append(nome)
    novoUsuario.append(idade)
    novoUsuario.append(login)
    novoUsuario.append(senha)
    listamvp.append(novoUsuario)
    return listamvp
def login(listamvp):
    #essa função recebe a listamvp, e tem como função fazer o login do usuario, caso o login e senha fornecidos pelo o mesmo estejam corretos.
    logar = False
    #print(listamvp)
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')
    for user in listamvp: 
        if user[2] == login and user[3] == senha: 
            logar = True
            print('Login efetuado com sucesso')
    
    while logar == False:
        print('Login inválido, tente novamente: ')
        login = input('Digite seu login: ')
        senha = input('Digite sua senha: ')

        for user in listamvp: 
            if user[2] == login and user[3] == senha: 
                logar = True
                print('Login efetuado com sucesso')
                break
def mvp(listamvp):
    #essa função corresponde ao menu do mvp, seguindo o padrão do primeiro menu, ele lista as opções trata a escolha do usuario, e chama as funções de cada opção, e depois chama recursivamente a função mvp() para poder novamnetea navegar no menu..
    #se a opção fora 1(cadastrar-se) vai chamar a função cadastroMVP(listamvp) que recebe como parametro uma lista para guardar e manipular futuramente os dados que foram ali guardados, e depois chama recursivamente a função mvp() para poder novamnetea navegar no menu..
    #se a opção for 2(sobre nós) vai printar um texto contendo informações sobre nós(a empresa da solução), e depois chama recursivamente a função mvp() para poder novamnetea navegar no menu.
    #se a opção for 3(listar veiculos), vai printar todos os veiculos disponiveis na empresa,(futuramente caso seja aceito em uma ata, vamos permitir que empresas cadastrem veiculos, logo esses números serão mais dinâmicos),e depois chama recursivamente a função mvp() para poder novamnetea navegar no menu.
    #se a opção for 4(login), vai chamar a função login(listamvp), que serve para realizar o login do usuario no site, tratando e validando os dados para só permitir o login caso os dados estejam corretos, e depois chama recursivamente a função mvp() para poder novamnetea navegar no menu.
    #se a opção for 5(quero um veiculo), vai printar na tela um menu contendo os tipos de veiculos disponiveis de acordo com a opção 3 desse menu, permitindo o usuario escolher 2 veiculos e validando que sua escolha não passe disso, e depois chama recursivamente a função mvp() para poder novamnetea navegar no menu.
    #se a opção for 6(sair), vai printar uma saudação e encerrar o menu, voltando para o primeiro menu que tem outras opções além do mvp.
    print('''Bem vindo ao nosso menu, selecione uma das opções:\n[ 1 ] - Cadastrar-se\n[ 2 ] - Sobre nós\n[ 3 ] – Listar veículos\n[ 4 ] - Login\n[ 5 ] - Quero um veiculo\n[ 6 ] - Sair\n''')
    opt = input('Digite o número da opção: ')
    if opt == '6':
        print('Fim do programa! Volte sempre!')
    while True: 
        if opt != '1' and opt != '2' and opt != '3' and opt != '4' and opt != '5' and opt != '6': 
            opt = input('Opção inválida, digite o número correspondente a sua opção: ')
            continue
        break
    if opt == '1':
        cadastroMVP(listamvp)
        mvp(listamvp)
    if opt == '2':
        print('Visando em tornar o mundo um lugar mais tecnológico e sustentável, nós do grupo ZNDev’s produzimos uma solução que irá impactar diretamente na vida não só das pessoas que dependem de alugar um veículo para seu dia a dia, mas também daquelas que buscam preservar da natureza enquanto usufruem da mais avançada tecnologia nos meios de transporte.')
        mvp(listamvp)
    if opt == '3':
        listaV = [{'Carros':['Normal:100','Viagem:30','Com cadeirinha:50','Para pcd:20']}, {'Motos':'65'}, {'Patinetes':'30'},{'Bike eletrica':'200'}]
        for i in range(len(listaV)):
                print(f'Veiculo {i}: {listaV[i]}')
                i+1
        mvp(listamvp)
    if opt == '4':
        login(listamvp)
        mvp(listamvp)
    if opt == '5':
        print('Veiculos disponiveis:\n[ 1 ] - Carro elétrico normal\n[ 2 ] - Carro elétrico para viagem\n[ 3 ] - Carro eletrico com cadeirinha infantil\n[ 4 ] - Carro elétrico para pessoas com pcd\n[ 5 ] - moto\n[ 6 ] - patinete\n[ 7 ] - Bike eletrica\n[ 8 ] - Sair')
        escolha = input('Escolha um dos veiculos:')
        if escolha == '8':
            print('Fim do programa! Volte sempre!')
        while True: 
            if escolha != '1' and escolha != '2' and escolha != '3' and escolha != '4' and escolha != '5' and escolha != '6' and escolha != '7' and escolha != '8': 
                escolha = input('Opção inválida, digite o número correspondente a sua opção: ')
                continue
            break
        if escolha == '1':
            c = input('Digite a quantidade(max 2 por usuário):')
            while True:
                if c != '1' and c != '2':
                    c = input('Opção inválida, digite o número correspondente a sua opção: ')
                    continue
                break
            print(f'Dados do usuário: {listamvp}\n{c} Carro Comum')
            mvp(listamvp)
        if escolha == '2':
            c = input('Digite a quantidade(max 2 por usuário):')
            while True:
                if c != '1' and c != '2':
                    c = input('Opção inválida, digite o número correspondente a sua opção: ')
                    continue
                break
            print(f'Dados do usuário: {listamvp}\n{c} Carro para viagem')
            mvp(listamvp)
        if escolha == '3':
            c = input('Digite a quantidade(max 2 por usuário):')
            while True:
                if c != '1' and c != '2':
                    c = input('Opção inválida, digite o número correspondente a sua opção: ')
                    continue
                break
            print(f'Dados do usuário: {listamvp}\n{c} Carro com cadeirinha infantil')
            mvp(listamvp)
        if escolha == '4':
            c = input('Digite a quantidade(max 2 por usuário):')
            while True:
                if c != '1' and c != '2':
                    c = input('Opção inválida, digite o número correspondente a sua opção: ')
                    continue
                break
            print(f'Dados do usuário: {listamvp}\n{c} Carro pcd')
            mvp(listamvp)
        if escolha == '5':
            c = input('Digite a quantidade(max 2 por usuário):')
            while True:
                if c != '1' and c != '2':
                    c = input('Opção inválida, digite o número correspondente a sua opção: ')
                    continue
                break
            print(f'Dados do usuário: {listamvp}\{c} Moto')
            mvp(listamvp)
        if escolha == '6':
            c = input('Digite a quantidade(max 2 por usuário):')
            while True:
                if c != '1' and c != '2':
                    c = input('Opção inválida, digite o número correspondente a sua opção: ')
                    continue
                break
            print(f'Dados do usuário: {listamvp}\n{c} Patinete')
            mvp(listamvp)
        if escolha == '7':
            c = input('Digite a quantidade(max 2 por usuário):')
            while True:
                if c != '1' and c != '2':
                    c = input('Opção inválida, digite o número correspondente a sua opção: ')
                    continue
                break
            print(f'Dados do usuário: {listamvp}\n{c} Bike elétrica')
            mvp(listamvp)
def principal(lista, listamvp):
    #@thiagoGabriel
    #essa função atende os outros requisitos do menu além de ser um próprio menu, inicialmente vai printar as saudações e listar as opções para o usuario, tendo 2 vereficações, uma para sair do menu e encerrar o programa, e outra para validar a opcao que o usuario digitar.
    #se a opção for 1(cadatrar o mês...), vai chamar a função cadastro, e chamar recursivamente a função principal para continuar navegando pelo menu;
    #se a opção for 2(exibir dados do mês...), vai chamar a função buscar, e chamar recursivamente a função principal para continuar navegando pelo menu;
    #se a opção for 3(relatório comparativo...), vai perguntar ao usuario qual ano que o mesmo quer que seja feito um relatório, depois entrando em um loop para poder percorrer a lista de dicionarios e somar todos os meses desse ano espeacifico, retornando um relatorio;
    #se a opção for 4(listar todos os meses...), vai entrar em um loop para imprimir a lista de dicionários mas devidamente formatada para uma melhor experiencia ou analise.
    #se a opção for 5(mvp), vai entrar em outro menu que aborda a solução, mais detalhes na def mvp().
    #se a opção for 6(sair), o programa encerra.
    #EXTRA!!, como eu terminei bem rápido o trabalho e achei legal de fazer, vou rodar o código colocando dados válidos sobre o total de habitantes e total de óbitos após 2019 e fazer um arquivo write :)
    print('''Bem vindo ao nosso menu, selecione uma das opções:\n[ 1 ] - Cadastrar mês de referência\n[ 2 ] - Exibir dados do mês de referência [pesquisa por mês]\n[ 3 ] – Relatório comparativo – Referência 2019\n[ 4 ] - Listar todos os meses cadastrados\n[ 5 ] - Mvp\n[ 6 ] - Sair\n''')
    op = input('Digite o número da opção: ')
    if op == '6':
        print('Fim do programa! Volte sempre!')
    while True: 
       if op != '1' and op != '2' and op != '3' and op != '4' and op != '5' and op != '6': 
           op = input('Opção inválida, digite o número correspondente a sua opção: ')
           continue
       break

    if op == '1':
        cadastro(lista)
        principal(lista, listamvp)

    if op == '2':
        buscar(lista)
        principal(lista, listamvp)

    if op == '3': 
        somaHB = 0
        somaOBT = 0
        taxa = 0
        pct = 0
        ano = input('Digite o ano a ser comparado:')
        for i in (lista):
            if i["mês-ano"][3:] == ano:
                    somaHB += i['Total de habitantes']
                    somaOBT += i['Total de óbitos'] 
        taxa = (somaOBT/somaHB)*100000
        pct = (taxa-15)/15*100
        print(f'Total de habitantes: - {somaHB}')
        print(f'Total de óbitos: - {somaOBT}')
        print(f'Taxa por 100k habitantes – {ano}: {taxa:.2f}')
        print(f'Taxa por 100k habitantes – 2019: 15')
        print(f'Comparativo % entre {ano}-2019: {pct:.2f}%')
        principal(lista, listamvp)    
    if op == '4': 
        for i in range(len(lista)):
            print(f'Relátorio {i}: {lista[i]}')
            i +1
        principal(lista,listamvp)

    if op == '5':
        mvp(listamvp)
        principal(lista, listamvp)
lista = geraLista()
listamvp = listaMVP()
principal(lista, listamvp)