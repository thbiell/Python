media = 0
import time
#import matplotlib.pyplot as plt
def gerarLista10k():
    file = open('lista10k.txt','r')
    lista1 =  file.readlines()
    lista10k = []
    for i in lista1:
        lista10k.append(int(i))
    file.close()
    return lista10k

def gerarLista100k():
    file = open('lista100k.txt','r')
    lista2 = file.readlines()
    lista100k = []
    for i in lista2:
        lista100k.append(int(i))
    file.close()
    return lista100k

def gerarLista500k():
    file = open('lista500k.txt','r')
    lista3 = file.readlines()
    lista500k = []
    for i in lista3:
        lista500k.append(int(i))
    file.close()
    return lista500k

def gerarLista1M():
    file = open('lista1M.txt','r')
    lista4 = file.readlines()
    lista1M = []
    for i in lista4:
        lista1M.append(int(i))
    file.close()
    return lista1M

def gerarLista5M():
    file = open('lista5M.txt','r')
    lista5 = file.readlines()
    lista5M = []
    for i in lista5:
        lista5M.append(int(i))
    file.close()
    return lista5M
 
def opcao():
    print('''Bem vindo ao nosso menu, selecione uma das opções:\n [ 0 ] - Bubble Sort\n [ 1 ] - Selection Sort\n [ 2 ] - Insertion Sort\n [ 3 ] - Merge Sort\n [ 4 ] - Quick Sort \n [ 5 ] - Configuração do pc\n [ 6 ] - Sair\n''')
    op = int(input('Digite o número da opção: '))
    if op == 6:
        print('Fim do programa! Volte sempre!')
    elif op > 6:
        print('Opção inválida!!')
    return op

def EscolherTam():
    print('''Escolha uma das quantitades:\n [ 0 ] - 10000\n [ 1 ] - 100000\n [ 2 ] - 500000\n [ 3 ] - 1000000\n [ 4 ] - 5000000''')
    tam = int(input('Digite o número da opção: '))
    if tam >4:
        print('Número inválido!!')
    elif tam == 0:
        tam = gerarLista10k()
    elif tam == 1:
        tam = gerarLista100k()
    elif tam == 2:
        tam = gerarLista500k()
    elif tam == 3:
        tam = gerarLista1M()
    elif tam == 4:
        tam = gerarLista5M()
    return tam

    
def opcao5(op):
    if op == 5: 
        print('Configuração da máquina utilizada: (Processador Intel Xeon E5-2640 v3 (com overclock 3.40 GHZ), 16 gb ECC(memória de servidor), 1 ssd kingston 500gb e 1 hd wd blue 1 tb, Placa mãe atermiter X-99 D4, Placa de vídeo GTX 1660ti)')

def opcao0(op):
    if op == 0:
        calcBubble()

def opcao1(op):
    if op == 1:
        calcSelect()

def opcao2(op):
    if op == 2:
        calcInsert()

def opcao3(op):
    if op == 3:
        calcMerge()

def opcao4(op):
    if op == 4:
        calcQuick()


def bubble(lista):
    
  for i in range(len(lista)):

    for j in range(0, len(lista) - i - 1):
      if lista[j] > lista[j + 1]:
        temp = lista[j]
        lista[j] = lista[j+1]
        lista[j+1] = temp

def select(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
            lista[i], lista[min_index] = lista[min_index], lista[i]


def insert(lista):
   for index in range(1,len(lista)):

     currentvalue = lista[index]
     position = index

     while position>0 and lista[position-1]>currentvalue:
         lista[position]=lista[position-1]
         position = position-1

     lista[position]=currentvalue

def merge(lista):
    if len(lista) > 1:
        mid = len(lista) // 2  
        left = lista[:mid] 
        right = lista[mid:] 

        merge(left)
        merge(right)

        i = j = k = 0

        #  data to temp arrays L[] and R[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lista[k] = left[i]
                i += 1
            else:
                lista[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            lista[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lista[k] = right[j]
            j += 1
            k += 1

def partition(lista, inicio, fim):
    pivot = lista[inicio]
    low = inicio + 1
    high = fim
    while True:
        while low<= high and lista[high]>= pivot:
            high -=1
        while low<= high and lista[low]<= pivot:
            low +=1

        if low <= high:
            lista[low], lista[high] = lista[high], lista[low]

        else:
            break

    lista[inicio], lista[high] = lista[high], lista[inicio]
    return high
def quick(lista, inicio, fim):
    if inicio >= fim:
        return
    p = partition(lista, inicio, fim)
    quick(lista, inicio, p-1)
    quick(lista, p+1, fim)

def calcBubble():
    soma = 0
    tempo = []
    tam = EscolherTam()
    for i in range(20):
        copia = tam[:]
        start_time = time.time()
        bubble(copia)
        o = (time.time() - start_time)
        tempo.append(o)
        print(f'tempo: {o:.3f}segundos')
    for i in range(len(tempo)):
        print(f'tempo do {i}: {tempo[i]:.3f} segundos')#, se quiser ver o tempo de cada uma das execuções é só tirar o #
        soma = tempo[i] + soma
        i + 1
    media = soma/20
    print('O bubble sort realiza múltiplas passagem por uma lista. Ele compara itens adjacentes e troca aqueles que estão fora de ordem. Cada passagem pela lista coloca o próximo maior valor na sua posição correta. Em essência, cada item se desloca como uma “bolha” para a posição à qual pertence.')
    print(f'Média do tempo: {media:.3f} segundos.')

def calcSelect():
    soma = 0
    tempo = []
    tam = EscolherTam()
    for i in range(20):
        copia = tam[:]
        start_time = time.time()
        select(copia)
        o = (time.time() - start_time)
        tempo.append(o)
        print(f'tempo: {o:.3f}segundos')
    for i in range(len(tempo)):
        #print(f'tempo do {i}: {tempo[i]:.3f} segundos'), se quiser ver o tempo de cada uma das execuções é só tirar o #
        soma = tempo[i] + soma
        i + 1
    media = soma/20
    print('A ordenação por seleção (do inglês, selection sort) é um algoritmo de ordenação baseado em se passar sempre o menor valor do vetor para a primeira posição (ou o maior dependendo da ordem requerida), depois o de segundo menor valor para a segunda posição, e assim é feito sucessivamente com os {\displaystyle n-1}n-1 elementos restantes, até os últimos dois elementos.')
    print(f'Média do tempo: {media:.3f} segundos.')

def calcInsert():
    soma = 0
    tempo = []
    tam = EscolherTam()
    for i in range(20):
        copia = tam[:]
        start_time = time.time()
        insert(copia)
        o = (time.time() - start_time)
        tempo.append(o)
        print(f'tempo: {o:.3f}segundos')
    for i in range(len(tempo)):
        print(f'tempo do {i}: {tempo[i]:.3f} segundos')#, se quiser ver o tempo de cada uma das execuções é só tirar o #
        soma = tempo[i] + soma
        i + 1
    media = soma/20
    print('Insertion Sort, ou ordenação por inserção, é um algoritmo de ordenação que, dado uma estrutura (array, lista) constrói uma matriz final com um elemento de cada vez, uma inserção por vez. Assim como algoritmos de ordenação quadrática, é bastante eficiente para problemas com pequenas entradas, sendo o mais eficiente entre os algoritmos desta ordem de classificação.')
    print(f'Média do tempo: {media:.3f} segundos.')

def calcMerge():
    soma = 0
    tempo = []
    tam = EscolherTam()
    for i in range(20):
        copia = tam[:]
        start_time = time.time()
        merge(copia)
        o = (time.time() - start_time)
        tempo.append(o)
        #print(f'tempo: {o:.3f}segundos')
    for i in range(len(tempo)):
        print(f'tempo do {i}: {tempo[i]:.3f} segundos') #se quiser ver o tempo de cada uma das execuções é só tirar o #
        soma = tempo[i] + soma
        i + 1
    media = soma/20
    print('Merge Sort é um algoritmo eficiente de ordenação por divisão e conquista. Se nossa missão é ordenar um array comparando seus elementos, do ponto de vista assintótico, n∗logn é o nosso limite inferior. Ou seja, nenhum algoritmo de ordenação por comparação é mais veloz do que n∗logn. Formalmente, todos são Ω(n∗logn).')
    print(f'Média do tempo: {media:.3f} segundos.')


def calcQuick():
    soma = 0
    tempo = []
    tam = EscolherTam()
    for i in range(1):
        copia = tam[:]
        start_time = time.time()
        quick(copia, 0, (len(copia)-1))
        o = (time.time() - start_time)
        tempo.append(o)
        #print(f'tempo: {o:.3f}segundos')
    for i in range(len(tempo)):
        print(f'tempo do {i}: {tempo[i]:.3f} segundos')# se quiser ver o tempo de cada uma das execuções é só tirar o #
        soma = tempo[i] + soma
        i + 1
    media = soma/20
    #print(copia)
    print(f'Média do tempo: {media:.3f} segundos.')

    
#def graficos():
#    data = {f'Bubble\n9517733.534s':158628.892, 'Select\n9423219.156s':157053.652, 'Insert\n4330236.284s':72170.604,
#        'Merge\n35.526s':0.592,'Quick\n22.979s':0.383}
#    courses = list(data.keys())
#    values = list(data.values())
#    
#    fig = plt.figure(figsize = (10, 5))
#    
#    # creating the bar plot
#    plt.bar(courses, values, color ='maroon',
#            width = 0.4)
#    
#    plt.xlabel("Algoritmos de ordenação sort")
#    plt.ylabel("Tempo em minutos")
#    plt.title("Gráfico para todos os métodos com lista 5M")
#    plt.show()


    
def menu():
    op = opcao()
    opcao0(op)
    opcao1(op)
    opcao2(op)
    opcao3(op)
    opcao4(op)
    opcao5(op)

menu()

#graficos()


