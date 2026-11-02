def echanger (L):
    L [0], L[-1], = L [-1],L [0]
    return L

L = [10,20,30,40,50]

print ("liste avant echange :",L)

echanger (L)

print ("liste apres echange :",L)