def solucionar(x, y):
    for i in range(x,y+1):
        sum = 0
        for j in range(1,i):
            if i%j == 0:
                sum += j
            if sum == i:
                return i
    return -1

print(solucionar(5,7))

