import math
def dist(x1, y1, x2, y2):  
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) )

def isTriangleValid(x1,y1,x2,y2,x3,y3):
    a = (x1 * (y2 - y3) + x2 * (y3 - y1) +  x3 * (y1 - y2)) 
    if a:
        return True
    return  False

def circumcircleRadius(a, b, c):
    return (a * b * c) / math.sqrt((a + b + c) * (b + c - a) * (c + a - b) * (a + b - c))

def incircleRadius(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt((s - a) * (s - b) * (s - c) / s)

def solve(x1, y1, x2, y2, x3, y3):
    # calculate side lengths like below:
    a = dist(x1, y1, x2, y2)
    b = dist(x3, y3, x2, y2)
    c = dist(x1, y1, x3, y3)

    # check that a, b, c form a valid triangle
    if isTriangleValid(x1,y1,x2,y2,x3,y3):
        pi=3.14159265358

        circumcircle_radius = circumcircleRadius(a, b, c)
        incircle_radius = incircleRadius(a, b, c)

        area_of_ring = pi*(circumcircle_radius**2)-pi*(incircle_radius**2)
        print('{0:.2f}'.format(area_of_ring)) 
        return 0
    else:
        print ("Not Possible")
        return 0
n=int(input())
n=n//3
for _ in range(n):
    x1,y1=(map(float,input().split()))
    x2,y2=(map(float,input().split()))
    x3,y3=(map(float,input().split()))
    solve(x1,y1,x2,y2,x3,y3)





