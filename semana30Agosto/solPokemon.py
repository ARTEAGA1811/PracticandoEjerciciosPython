INF = 1000000

def cross_forest(H, r, c):
	global W
	DP = {}
	for i in range(r):
		for j in range(c):
			DP[i,j] = 0
	DP[0,0] = H
	for i in range(1, r ):
		DP[i, 0] = W[i][0] + DP[i-1, 0]
		if DP[i-1, 0] <= 0:
			DP[i,0] = - INF 
	for i in range(1, c):
		DP[0, i] = W[0][i] + DP[0, i-1]
		if DP[0, i-1] <= 0:
			DP[0, i] = - INF
	
	for i in range(1, r):
		for j in range(1, c):
			mx = max (DP[i-1, j], DP[i, j-1]) 
			if mx <= 0: DP[i,j] = - INF 
			else: DP[i,j] = mx + W[i][j]
	
	#print DP
	
	return DP[r - 1,c - 1]
	
r, c = 10, 10
W = [map(int, raw_input().split()) for j in range(c)]

lo, hi, ans = 1, 1000000, 1000000
while( lo <= hi ):
	mid = (lo + hi ) / 2
	if(cross_forest(mid,r,c) > 0 ):
		ans = mid
		hi = mid - 1
	else:
		lo = mid + 1

print ans 
	
	
	





def testear():
    casosPrueba = [
        [
            [2,2],
            [
                [0,-2],
                [2,0]
            ]
        ],
        [
            [3,3],
            [
                [0,1,2],
                [-2,-9,-4],
                [-8,5,0]
            ]
        ]

    ]

    salidas = [
        1,2
    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i][0], casosPrueba[i][1])
            assert solution == salidas[i]
            print("respuesta correcta")
        except Exception as error:
            print(
                f"Error, test {casosPrueba[i]}, expected {salidas[i]}, calculated {solution}", error)

testear()