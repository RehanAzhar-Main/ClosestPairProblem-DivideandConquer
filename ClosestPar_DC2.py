import math 
import copy

class Point2DPlane(): 
    def __init__(self, x, y): 
        self.x = x
        self.y = y
 
def SetDist(p1, p2): 
    return math.sqrt((p1.x - p2.x) *
                     (p1.x - p2.x) +
                     (p1.y - p2.y) *
                     (p1.y - p2.y))
 
def bruteForce(P, n): 
    minim_value = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if SetDist(P[i], P[j]) < minim_value:
                minim_value = SetDist(P[i], P[j])
 
    return minim_value
 

def FindClosestStrip(strip, size, d): 
     
    minim_value = d
    
    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y -
                            strip[i].y) < minim_value:
            minim_value = SetDist(strip[i], strip[j])
            j += 1
 
    return minim_value
 
def FindClosestUtil(P, Q, n):
    
    #base acse
    if n <= 3:
        return bruteForce(P, n)
 
    # recursive case
    mid = n // 2
    midPoint = P[mid]
 

    Pl = P[:mid]
    Pr = P[mid:]
 
    dl = FindClosestUtil(Pl, Q, mid)
    dr = FindClosestUtil(Pr, Q, n - mid)
 
    d = min(dl, dr)
 
    # combine
    stripP = []
    stripQ = []
    lr = Pl + Pr
    for i in range(n):
        if abs(lr[i].x - midPoint.x) < d:
            stripP.append(lr[i])
        if abs(Q[i].x - midPoint.x) < d:
            stripQ.append(Q[i])
 
    stripP.sort(key = lambda point: point.y) #<-- REQUIRED
    min_a = min(d, FindClosestStrip(stripP, len(stripP), d))
    min_b = min(d, FindClosestStrip(stripQ, len(stripQ), d))
    
    return min(min_a,min_b)


def closest(P, n):
    P.sort(key = lambda point: point.x)
    Q = copy.deepcopy(P)
    Q.sort(key = lambda point: point.y)   
 

    return FindClosestUtil(P, Q, n)
 
# Driver code
P = [Point2DPlane(5, 2), Point2DPlane(13, 7),
     Point2DPlane(16, 19), Point2DPlane(2, 12),
     Point2DPlane(20, 20), Point2DPlane(17, 11),
     Point2DPlane(50, 2), Point2DPlane(25, 11),
     Point2DPlane(117, 30), Point2DPlane(37, 40)]
n = len(P)
print("The smallest distance is",closest(P, n))
 
