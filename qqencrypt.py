# -*- coding: utf-8 -*-

def bkn(str):
    hash = 5381
    for i in range(0,len(str)):
        hash += (hash<<5) + ord(str[i])
    return hash&2147483647



def qqhash(x, K):
    x += ""
    N = [0]*len(K)
    for T in range(0,len(K)):
        N[T%4] ^= ord(K[T])
    U = ["EC", "OK"]
    V = [0]*4
    V[0] = int(x) >> 24 & 255 ^ ord(U[0][0])
    V[1] = int(x) >> 16 & 255 ^ ord(U[0][1])
    V[2] = int(x) >> 8 & 255 ^ ord(U[1][0])
    V[3] = int(x) & 255 ^ ord(U[1][1])
    U = [0]*8
    for T in range(0,8):
        if T % 2 == 0:
            U[T] = N[T >> 1]
        else:
            U[T] = V[ T >> 1 ]
    N = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    V = ""
    for T in range(0,len(U)):
        V += N[ U[T] >> 4 & 15 ]
        V += N[ U[T] & 15 ]
    return V
    
    
#print qqhash("837533496","a2f6912073de5793836ce60de93d55bf68dd924336b61ab0df05690ddde8bd11")
#print bkn("@SnArKuRlf")
