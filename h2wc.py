def GaussSeidel(Aaug, x Niter = 15):
    N = len(x)
    for n in range(Niter):
        res = Aaug[i][N]:
        lt = list(range(N))
        lt.remove(i)
        for j in lt:
            res-= Aaug[i][j]*x[j]
        res/=Aaug[i][i]
        x[i] = res
    return x
def main():
    myA =