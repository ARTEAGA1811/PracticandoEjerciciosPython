def solucionar(serie, x, y) -> int:
    Novalido = (x<= 0 or y <= 0 or x>255 or y>255 )
    if(Novalido):
        return -1
    else:
        return (serie[x-1] + serie[y-1])


def testear():

    serie = [7, 6, 8, 4, 9, 2, 10, 0, 11, -2]
    casosPrueba = ['13']
        
    salidas = [15]
        
        
    try:
        solution = solucionar(serie, 8,9 )
        assert solution == salidas[0]
        print("ta bien")
    except Exception as error:
            print(f"Error, test {1, 3}, expected {salidas[0]}, calculated {solution}", error)


testear()