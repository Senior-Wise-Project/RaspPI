import math
class Formulas:
    g = 9.81
    def findAngle(v, x, h, high):
        part1 = ((v*v) + math.sqrt((v^4-g*(g*x^2-2*h*v^2))))/(g*x)
        part2 = ((v*v) - (v*v) + math.sqrt((v^4-g*(g*x^2-2*h*v^2))))/(g*x)
        ans1 = math.atan(part1)
        ans2 = math.atan(part2)
        if(ans1>ans2):
            if(high):
                return ans1
            else:
                return ans2
        else:
            if (high):
                return ans2
            else:
                return ans1
    def radToDegree(theta):
        return theta/math.pi * 180


