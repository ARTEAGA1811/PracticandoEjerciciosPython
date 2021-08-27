
def solucionar(elements, query: str):
    sortedElements = sorted(elements) 
    cons = []
    for i in range(1, len(query)): #aumenta caracter
        aux = []
        sub = query[0:i+1]
        for j in sortedElements: #busca en cada elemento
            if sub in j[0:i+1]:
                if(len(aux)<3):
                    aux.append(j)
                else:
                    break
            
        cons.append(aux)
    return cons






def testear():
    elements = ['car', 'cartouches', 'carpet', 'cartoonist', 'carrot', 'cared', 'carton', 'captain', 'cartoon', 'carter']
    query = 'cartoons'
    salidas = [
        ['captain', 'car', 'cared'],
        ['car', 'cared', 'carpet'],
        ['carter', 'carton', 'cartoon'],
        ['carton', 'cartoon', 'cartoonist'],
        ['cartoon', 'cartoonist'],
        ['cartoon', 'cartoonist'],
        []
    ]

    try:
        solution = solucionar(elements, query)
        assert solution == salidas
        print("ta bien")
    except Exception as error:
            print(f"Error, test {''}, expected {salidas}, calculated {solution}", error)

testear()