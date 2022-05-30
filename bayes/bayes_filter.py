p = [.2, .2, .2, .2, .2] # PRIOR
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green'] # Z
motions = [1, 1] # U
pHit = .6
pMiss = .2
pExact = .8
pOvershoot = .1
pUndershoot = .1

def sense(p, Z):
    q = [] # POSTERIOR 
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] /= s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s += pOvershoot * p[(i-U-1) % len(p)]
        s += pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

for k in range(len(measurements)):
    p = sense(p, measurements[k])
    p = move(p, motions[k])

print(p)
