# region imports
import math
from math import cos
# endregion

# region functions
def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):

    delta = (x1-x0)  #value for delta with initial guesses
    x = x1
    fOld = fcn(x0)  # value of callback at x0
    fNew = fOld
    Niter = 0  # a counting variable for number of iterations
    while Niter < maxiter and abs(delta) > xtol:
        fNew = fcn(x)  # value of callback at x
        delta = -fNew*delta/(fNew-fOld)
        x += delta  # the next value of x
        fOld = fNew
        Niter += 1
    return x

def main():

    # functions using lambda notation
    fn1 = lambda x: 3*cos(x)
    fn2 = lambda x: cos(2*x)*x**3

    maxiter1 = 5
    maxiter2 = 15
    maxiter3 = 3

    r1 = Secant(fn1, 1, 2, maxiter=maxiter1, xtol=1e-4)
    r2 = Secant(fn2, 1, 2, maxiter=maxiter2, xtol=1e-8)
    r3 = Secant(fn2, 1, 2, maxiter=maxiter3, xtol=1e-8)

    #output of root values and test in functions to see if fn(r)=0.00
    print("r1={:0.6f}".format(r1))
    print("fn1(r1)={:0.6f}".format(fn1(r1)))
    print("\nwith maxiter={}:  r2={:0.6f}".format(maxiter2,r2))
    print("fn2(r2)={:0.6f}".format(fn2(r2)))
    print("\nwith maxiter={}:  r3={:0.6f}".format(maxiter3, r3))
    print("fn2(r3)={:0.6f}".format(fn2(r3)))
    print("\nExact answer for fn2={:0.6f}".format(math.pi/4.0))
# endregion

# region function call(s)
if __name__ == "__main__":
    main()
# endregion
