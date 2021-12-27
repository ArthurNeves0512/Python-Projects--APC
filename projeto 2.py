'CHAMADOS DE T '
def primeira():
    tudo = []
    repetidos = []
    for nome in lista_imagens:
        if nome not in repetidos:
            repetidos.append(nome)
    for elemento in repetidos:
        objetos = {'nome': elemento, 'bison': 0,
                   'elephant': 0,
                   'horse': 0,
                   'ibis': 0,
                   'sky': 0,
                   'mountain': 0,
                   'building': 0,
                   'flower': 0,
                   'sand': 0,
                   'tree': 0,
                   'field': 0,
                   'road': 0,
                   'tower': 0,
                   'ocean': 0,
                   'cliff': 0,
                   'waterfall': 0}
        for i in lista_principal:
            if elemento == i[0]:
                if 'bison' in i[1]:
                    objetos['bison'] = 1
                elif 'elephant' in i[1]:
                    objetos['elephant'] = 1
                elif 'horse' in i[1]:
                    objetos['horse'] = 1
                elif 'ibis' in i[1]:
                    objetos['ibis'] = 1
                elif 'sky' in i[1]:
                    objetos['sky'] = 1
                elif 'mountain' in i[1]:
                    objetos['mountain'] = 1
                elif 'building' in i[1]:
                    objetos['building'] = 1
                elif 'flower' in i[1]:
                    objetos['flower'] = 1
                elif 'sand' in i[1]:
                    objetos['sand'] = 1
                elif 'tree' in i[1]:
                    objetos['tree'] = 1
                elif 'field' in i[1]:
                    objetos['field'] = 1
                elif 'road' in i[1]:
                    objetos['road'] = 1
                elif 'tower' in i[1]:
                    objetos['tower'] = 1
                elif 'ocean' in i[1]:
                    objetos['ocean'] = 1
                elif 'cliff' in i[1]:
                    objetos['cliff'] = 1
                elif 'waterfall' in i[1]:
                    objetos['waterfall'] = 1
        if objetos not in tudo:
            tudo.append(objetos.values())
    return tudo
def segunda():
    tudo = []
    repetido = []
    for b in lista_imagens:
        if b not in repetido:
            repetido.append(b)
    for nome in repetido:
        a = lista_imagens.count(nome)
        objeto ={'nome':nome,'caixas':f'{(a)/2:.1f}','mediadox': 0.0,'médiadoy': f'{0.0:.1f}'
                 ,'largura':f'{0.0:.1f}','altura':0.0,'area': 0.0,'desvioX': 0.0,'desvioY': 0.0,'deslarg': 0.0,'desalt':0.0}
        médiaX = []
        médiaY = []
        largura = []
        altura =[]
        área = []
        desX = []
        rex = []
        rey = []
        rel = []
        rea = []
        for elemento in lista_principal:
            if nome == elemento[0]:
                médiaX.append(elemento[2]+elemento[4])
                médiaY.append(elemento[3]+elemento[5])
                largura.append(elemento[4]-elemento[2])
                calculoarea = (elemento[4]-elemento[2])*(elemento[5]-elemento[3])
                calculoaltura = elemento[5]-elemento[3]
                altura.append(calculoaltura)
                área.append(calculoarea)
        lek = sum(médiaX)/(2*a)
        lak = sum(médiaY)/(2*a)
        lik = sum(largura)/(2*a)
        luk = sum(altura)/(2*a)
        for i in lista_principal:
            if nome == i[0]:
                rex.append(((i[2]+i[4])/2-lek)**2)
                rey.append(((i[3]+i[5])/2-lak)**2)
                rel.append(((i[4]-i[2])/2-lik)**2)
                rea.append(((i[5]-i[3])/2-luk)**2)
        objeto['mediadox'] = ((sum(médiaX)/2/a)/128)
        objeto['médiadoy'] = ((sum(médiaY)/2/a)/128)
        objeto['largura'] = ((sum(largura)/a)/128)
        objeto['area'] = ((sum(área)/a)/(128**2))
        objeto['altura'] = ((sum(altura)/a)/128)
        objeto['desvioX'] = (((sum(rex)/(a))**0.5)/32)
        objeto['desvioY'] = (((sum(rey)/a)**0.5)/32)
        objeto['deslarg'] = (((sum(rel)/a)**0.5)*2/32)
        objeto['desalt'] = (((sum(rea)/a)**0.5)*2/32)
        tudo.append(objeto.values())
    return tudo
def terceira(listabin,listaesta):
    e =[]
    d =[]
    calc =[]
    m = {'m1':0,'m2':0,'m3':0,'m4':0,'m5':0,'m6':0,'m7':0,'m8':0,'m9':0,
         'm10':0,'m11':0,'m12':0,'m13':0,'m14':0,'m15':0,'m16':0,'m17':0,'m18':0,'m19':0,'m20':0,'m21':0,'m22':0,
         'm23':0,'m24':0,'m25':0,'m26':0}
    numeros = []
    for i in range(0,len(listabin)):
        e.append(list(listabin[i])[1:]+list(listaesta[i])[1:])
    for l in e:
        numeros.append(list(map(float,l)))
    for i in numeros:
        print(i)
        for l in range(1,27):
            m[f'm{l}'] = m[f'm{l}']+ i[l-1]/len(numeros)
    return m.values()
def quarta(ou,o):
    nrepetidos = []
    valores = []
    valoresf = []
    distancias = []
    e = []
    for i in range(0,len(o)):
        valores.append(list(ou[i])[1:] + list(o[i])[1:])
    for i in valores:
        valoresf.append(list(map(float, i)))
    for numero in valoresf:
        for l in valoresf:
            for p in range(0,26):
                distancia = abs(numero[p]-l[p])
                distancias.append(distancia)
        e.append([sum(distancias)])
        distancias.clear()
    menor = e.index(min(e))
    for i in lista_imagens:
        if i not in nrepetidos:
            nrepetidos.append(i)
    print(nrepetidos[menor])

'PROGRAMA'
t, n = map(int, input().split())
lista_principal = []
lista_objetos = []
lista_imagens = []
for e in range(0,n):
    input()
    imagem = input()
    objeto_na_imagem = input()
    x1,y1,x2,y2 = map(int, input().split())
    lista_principal.append([imagem, objeto_na_imagem,x1,y1,x2,y2])
    lista_objetos.append(f'{objeto_na_imagem}')
    lista_imagens.append(f'{imagem}')
if t ==1:
    for a in primeira():
        print(*a)
if t ==2:
    for i in segunda():
        for d in i:
            if type(d) == float:
                print(f'{d:.1f}', end=' ')
            else:
                print(d, end=' ')
        print()
if t ==3:
    for l in terceira(primeira(),segunda()):
        print(f'{l:.1f}', end=' ')
else:
    quarta(primeira(),segunda())



