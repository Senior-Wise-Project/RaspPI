N_values = []
Xavg_values = []
V_values = []
g = 9.81
def shoot():
    print("Shoot!")

angle = input("Enter the angle at which you want the barrel to be")
sinVal = Math.sin(2*angle)
for x in range(10):
    n = input("Enter an N value")
    xVals = 0
    for y in range(3):
        go = input("Write Y to shoot")
        shoot()
        dis = input("What was the distance travelled?")
        xVals += dis
    xAvg = xVals/3
    v = g*xAvg/(sinVal)
    Xavg_values.append(xAvg)
    N_values.append(n)
    V_values.append(v)

print(N_values)
print(V_values)



