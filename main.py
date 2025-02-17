import numpy as np

a = 5
x0 = 2
err = 0.001

x1 = 0.5*(x0 + a/x0)

tol = np.absolute( (x1 - x0)/x1 )


while tol > err:
    x1 = 0.5*(x0 + a/x0)
    tol = np.absolute( (x1 - x0)/x1 )
    x0 = x1
    print("Tol = ",tol)
    print("xn: ",x1)
    print()


print(f"O valor da raíz é {x1:.6f}: ")