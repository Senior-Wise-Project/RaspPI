import math
import numpy as np
N_values = np.array([])
Xavg_values = np.array([])
V_values = np.array([])
angles = [15, 30, 45, 60, 75]
Sin_vals = np.arrays([])
for i in angles:
    sinVal = math.sin(2*i)
    Sin_vals = np.append(Sin_vals, sinVal)



g = 9.81

def shoot():
    print("Shoot!")


angle = input("Enter the angle at which you want the barrel to be")
sinVal = math.sin(2*angle)
for x in range(10):
    n = input("Enter an N value")
    xVals = 0
    for y in range(5):
        print("The barrel is angled at "+ angles[y])
        go = input("Write Y to shoot")
        shoot()
        dis = input("What was the distance travelled?")
        Xavg_values = np.append(Xavg_values, dis)

    A = np.vstack([Sin_vals, np.ones(len(Sin_vals))]).T
    m, c = np.linalg.lstsq(A, Xavg_values)[0]
    v = m*g
    N_values = np.append(N_values, n)
    V_values = np.append(V_values, v)

print(N_values)
print(V_values)



