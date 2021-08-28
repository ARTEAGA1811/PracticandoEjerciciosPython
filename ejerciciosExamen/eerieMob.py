def solucionar(valor):
    n = valor
    if(valor<1 or valor>255 or valor == None):
        return('(O_o)')
    elif(n ==1):
        return('(-_-)')
    elif(n ==2):
        return('(-_(-_-)')
    else:
        rigth_side_guy = '_-)'
        rigth_partial_guy = '-_-)'
        rigth_final_guy = '-)'
        left__side_guy = '(-_'
        left_partial_guy = '(-_-'
        left_final_guy = '(-'
        arrMobs = ['(-_-)']

        n = n-1 #por la cara central
        seAgregaCara = False
        if(n%2 == 0):
            n = int(n/2)
        else:
            n = n-1
            n = int(n/2)
            seAgregaCara = True
        
        contador = 1 # para el especial guy
        for i in range(n-1):
            #agrego a la izq y derecha.
            if(contador != 3):
                arrMobs = [left__side_guy, *arrMobs]
                arrMobs.append(rigth_side_guy)
            else:
                arrMobs = [left_partial_guy, *arrMobs]
                arrMobs.append(rigth_partial_guy)
                contador = 0
            contador+=1

        #aqui me falta agregar los finales.
        if(seAgregaCara):
            if(n%3 == 0):
                arrMobs = [left_partial_guy, *arrMobs]
            else:
                arrMobs = [left__side_guy, *arrMobs]
        if(valor>7):
            arrMobs = [left_final_guy, *arrMobs]
            arrMobs.append(rigth_final_guy)
        else:
            if(n%3 == 0):
                arrMobs = [left_partial_guy, *arrMobs]
                arrMobs.append(rigth_partial_guy)
            else:
                arrMobs = [left__side_guy, *arrMobs]
                arrMobs.append(rigth_partial_guy)
            
        #concateno todo
        mobs = ''
        for k in arrMobs:
            mobs+=k
        return(mobs)


def testear():
    casosPrueba = [
        4, 14,1
    ]

    salidas = [
        '(-_(-_(-_-)_-)', '(-(-_-(-_(-_(-_-(-_(-_(-_-)_-)_-)-_-)_-)_-)-)'
    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i])
            assert solution == salidas[i]
            print("ta bien")
        except Exception as error:
            print(f"Error, test {casosPrueba[i]}, expected {salidas[i]}, calculated {solution}", error)

#testear()
print(solucionar(7))


#  (-(-_-(-_(-_(-_-(-_(-_(-_-)_-)_-)-_-)_-)_-)-)
# (-_(-_-(-_(-_(-_-(-_(-_(-_-)_-)_-)-_-)_-)_-)_-)