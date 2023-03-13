def opcao():
    print('''Bem vindo ao nosso menu, selecione uma das opções:\n [ 0 ] - Cadastro\n [ 1 ] - Primeiro Emprego\n [ 2 ] - Sistema Avaliativo\n [ 3 ] - Feedback\n [ 4 ] - Sobre Nós\n [ 5 ] - Sair\n''')
    op = int(input('Digite o número da opção: '))
    if op == 5:
        print('Fim do programa! Volte sempre!')
    elif op > 5:
        print('Opção inválida!!')
    return op

def cadastro1():
    #função cadastro para ter acesso ao site.
    login = input('Seu login:\n')
    senha = int(input('Sua senha: '))

def voltar():
    #função para sair do menu ou retornar a ele.
    menu = int(input('Deseja voltar ao menu?\n [1] - Sim\n [2] - Não\n'))
    if menu == 1:
        principal()

    else:
        print('Fim do programa! Volte sempre!')
   

def cadastro2():
    #função para cadastrar no método primeiro emprego.
    login = input('Seu login:\n')
    senha = int(input('Sua senha: '))
    idade = int(input('Sua idade: '))  
    formacao = str(input("Formação: ")) 
    Contato = float(input("Telefone: "))  
    endereco = input('Endereço: ')
    nr = float(input('Número da sua casa: '))
    complemento = input('Complemento: ')

def opcao0(op):
     if op == 0:
        cadastro1()
        voltar()

def opcao1(op):
    if op == 1:
        print('Deseja se cadastrar ou obter informações?')
        teste = int(input('[1] - cadastro ou [2] - informações: '))
        if teste == 1:
            cadastro2()
            voltar()
        else:
            print('A plataforma contará com uma área exclusiva para pessoas em busca da sua primeira oportunidade de estágio/emprego, mostrando empresas que estão interessadas em moldar novos profissionais que no médio longo prazo trarão o resultado desejado pela empresa. Com isso, facilitando o início da carreira de iniciantes.\n')
            voltar()

def opcao2(op):
    if op == 2:
        print('Ofereceremos a opção de a empresa criar avaliações na plataforma, para analisar os conhecimentos dos interessados pela vaga, em uma certa linguagem, conhecimentos gerais e conhecimentos que serão necessários para a mesma. As avaliações não serão obrigatórias, cabe a empresa decidir se criará ou não e ela decidirá o peso que esse método terá na hora da contratação.\n')
        voltar()

def opcao3(op):
    if op == 3:
        print('Teremos um sistema único de feedback personalizado pela empresa, que poderá citar ao candidato pontos a melhorar, possíveis formas de obter alguns diferenciais, elogia-lo em algum ponto, e de maneira geral incentiva-lo a continuar tentando. Esse sistema também terá um gráfico que mostrará como os concorrentes estão indo em determinada avaliação, sem mostrar nomes e dados, apenas uma média comparando a pontuação geral alcançada, a maior pontuação e a pontuação do candidato após realizar a avaliação. Com isso a empresa testa os conhecimentos do profissional e pode dar continuidade na contratação, enquanto ele recebe feedbacks e analisa suas chances de alcançar a vaga.\n')
        voltar()

def opcao4(op):
    if op == 4:
        print('O projeto tem o intuito de facilitar as contratações, tanto pelo lado da empresa, quanto do candidato. Nosso intuito é esclarecer algumas das ansiedades que ocorrem ao procurar uma nova vaga de emprego, mas também ajudar a empresa a achar o profissional que mais se adequa ao perfil desejado para o cargo.')
        voltar()

def principal():
    op = opcao()
    opcao0(op)
    opcao1(op)
    opcao2(op)
    opcao3(op)
    opcao4(op)

principal()
