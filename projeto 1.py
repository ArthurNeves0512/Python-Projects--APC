#FUNÇÕES COM BASE NO CHAMADO DE T:

def primeira():
    'pego os itens do input a partir do início e manipulo is indices de uma lista'
    for item in lista_itens:
        print(f'{item[0]},{item[1]},{item[2]},{item[3]},{item[4]},{item[5]}')

def segunda():
    'taco em uma lista eai eu faço a contagem desses itens para cada elemento presente nela '
    lista_objetos = []
    for elemento in lista_itens:
        lista_objetos.append(elemento[1])
    print(f'black-bison: {(lista_objetos.count("black-bison")*100)/n:.1f}')
    print(f'elephant: {(lista_objetos.count("elephant")*100)/n:.1f}')
    print(f'white-horse: {(lista_objetos.count("white-horse")*100)/n:.1f}')
    print(f'brown-horse: {(lista_objetos.count("brown-horse")*100)/n:.1f}')
    print(f'scarlet-ibis: {(lista_objetos.count("scarlet-ibis")*100)/n:.1f}')
    print(f'black-ibis: {(lista_objetos.count("black-ibis")*100)/n:.1f}')
    print(f'white-ibis: {(lista_objetos.count("white-ibis")*100)/n:.1f}')
    print(f'blue-sky: {(lista_objetos.count("blue-sky")*100)/n:.1f}')
    print(f'overcast-sky: {(lista_objetos.count("overcast-sky")*100)/n:.1f}')
    print(f'cloudy-sky: {(lista_objetos.count("cloudy-sky")*100)/n:.1f}')
    print(f'dusthaze-sky: {(lista_objetos.count("dusthaze-sky")*100)/n:.1f}')
    print(f'rocky-mountain: {(lista_objetos.count("rocky-mountain")*100)/n:.1f}')
    print(f'snowy-mountain: {(lista_objetos.count("snowy-mountain")*100)/n:.1f}')
    print(f'birdseye-building: {(lista_objetos.count("birdseye-building")*100)/n:.1f}')
    print(f'perspective-building: {(lista_objetos.count("perspective-building")*100)/n:.1f}')
    print(f'front-building: {(lista_objetos.count("front-building")*100)/n:.1f}')
    print(f'red-flower: {(lista_objetos.count("red-flower")*100)/n:.1f}')
    print(f'purple-flower: {(lista_objetos.count("purple-flower")*100)/n:.1f}')
    print(f'pink-flower: {(lista_objetos.count("pink-flower")*100)/n:.1f}')
    print(f'sand: {(lista_objetos.count("sand")*100)/n:.1f}')
    print(f'tree: {(lista_objetos.count("tree")*100)/n:.1f}')
    print(f'green-field: {(lista_objetos.count("green-field")*100)/n:.1f}')
    print(f'snowy-field: {(lista_objetos.count("snowy-field")*100)/n:.1f}')
    print(f'yellow-field: {(lista_objetos.count("yellow-field")*100)/n:.1f}')
    print(f'road: {(lista_objetos.count("road")*100)/n:.1f}')
    print(f'tower: {(lista_objetos.count("tower")*100)/n:.1f}')
    print(f'blue-ocean: {(lista_objetos.count("blue-ocean")*100)/n:.1f}')
    print(f'green-cliff: {(lista_objetos.count("green-cliff")*100)/n:.1f}')
    print(f'black-cliff: {(lista_objetos.count("black-cliff")*100)/n:.1f}')
    print(f'waterfall: {(lista_objetos.count("waterfall")*100)/n:.1f}')

def terceira():
    "optei por fazer listas para cada caso, pois assim, seria melhor de manipular os valores a partir dos indices"
    "round arredonda os valores, uso do max e do min para pegar o maior e o menor que se pede"
    lista_médiaX = []
    lista_médiaY = []
    lista_médiaL = []
    lista_médiaA = []
    for elemento in lista_itens:
        lista_médiaX.append(elemento[2]+elemento[4])
        lista_médiaY.append(elemento[3]+elemento[5])
        lista_médiaL.append(elemento[5]-elemento[3])
        lista_médiaA.append(elemento[4]-elemento[2])
    print(f'{round((sum(lista_médiaX)/2)/n)} {round((sum(lista_médiaY)/2)/n)} {round(sum(lista_médiaA)/n)} {round(sum(lista_médiaL)/n)} ')

def quarta():
    "para cada iten na lista principal"
    "faço os calculos e crio variáveis para pegar os valores, eai eu crio listas que pegam os resultados para cada coisa"
    "por exemplo l1, que é a distancia, que é uma das coisas que ele pede, e depois, crio outras variáveis"
    "essas variáveis pegam os indices de maior, menor, depende do que pedem"
    for i in lista_itens:
        maisx = i[2]+i[4]
        xmédio = (i[2]+i[4])/2
        ymédio = (i[3]+i[5])/2
        distancia = ((xmédio-128)**2+(ymédio-128)**2)**0.5
        area = (i[4]-i[2])*(i[5]-i[3])
        altura = i[5]+i[3]
        l_1.append(distancia), l_2.append(i[0]), l_3.append(i[1]), l_4.append(xmédio), l_5.append(ymédio), l_6.append(area)
        l_7.append(maisx), l_8.append(altura)
    menorcentral = l_1.index(min(l_1))
    dismax = l_7.index(max(l_7))
    dismex = l_7.index(min(l_7))
    alto = l_8.index(min(l_8))
    menor = l_8.index(max(l_8))
    maiorA = l_6.index(max(l_6))
    menoA = l_6.index(min(l_6))
    print(f"""mais central: {l_3[menorcentral]},{l_2[menorcentral]}
mais a esquerda: {l_3[dismex]},{l_2[dismex]}
mais a direita: {l_3[dismax]},{l_2[dismax]}
mais acima: {l_3[alto]},{l_2[alto]}
mais abaixo: {l_3[menor]},{l_2[menor]}
maior area: {l_3[maiorA]},{l_2[maiorA]}
menor area: {l_3[menoA]},{l_2[menoA]}""")
"manipulo a lista que pega os nomes e os objetos eai dessas listas eu pego os indices, que estão nas variáveis"
def quinta():
    "crio listas, e a partir disso eu vejo se elas não estao na lista, igual pedem, exemplo do mercado "
    lista_objeto =[]
    tem_arvore =[]
    green_field = []
    snowy_field = []
    yellow_field = []
    atende_tudo =[]
    for i in lista_itens:
        if i[1] =='tree':
            tem_arvore.append(i[0])
        elif 'green-field' in i[1]:
            green_field.append(i[0])
        elif 'snowy-field' in i[1]:
            snowy_field.append(i[0])
        elif 'yellow-field' in i[1]:
            yellow_field.append(i[0])
    for i in tem_arvore:
        if i not in green_field and i not in snowy_field and i not in yellow_field:
            if i not in atende_tudo:
                atende_tudo.append(i)
    if len(atende_tudo) == 0:
        print('nada')
    for i in atende_tudo:
        print(i)

#PROJETO

t, n = map(int, input().split())

lista_itens = []

l_1 = []
l_2 = []
l_3 = []
l_4 = []
l_5 = []
l_6 = []
l_7 = []
l_8 = []

for numero_de_itens in range(0, n):
    input()
    imagem = input()
    objeto = input()
    x1,y1,x2,y2 = map(int, input().split())
    lista_itens.append([imagem, objeto,x1,y1,x2,y2])
if t == 1:
    primeira()
elif t ==2:
    segunda()
elif t ==3:
    terceira()
elif t ==4:
    quarta()
elif t ==5:
    quinta()