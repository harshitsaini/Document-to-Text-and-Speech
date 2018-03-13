###############################KRUSKAL'S MINIMUM SPANNING TREE IN O(Elog(max(E,V))))##########################################

import cv2
import math
import numpy as np

class disjoint_set:
    def __init__(self):
        self.parent= -1
        self.rank=0

class edge:
    def __init__(self):
        self.u=-1
        self.v=-1
        self.w=-1

def find_parent(dset,i):
    if dset[i].parent==-1:
        return i
    return find_parent(dset, dset[i].parent)

def dsUnion(dset,x,y):
    xroot=find_parent(dset,x)
    yroot=find_parent(dset,y)
    if dset[xroot].rank >= dset[yroot].rank:
        dset[yroot].parent = xroot
        dset[xroot].rank += 1
    else :
        dset[xroot].parent = yroot
        dset[yroot].rank += 1


def getMST(edges,n):
    edges.sort(key=lambda item: item.w)
    mst=[] ; st=0
    dset = [disjoint_set() for i in range(n)]
    for it in range(n):
        while (find_parent(dset,edges[st].u)==find_parent(dset,edges[st].v) and (st<n)): st+=1
        if(st>=n): break
        x = edges[st].u ; y = edges[st].v ;   wt = edges[st].w
        dsUnion(dset,x,y)
        mst.append(wt) ; st+=1
    return mst

n,m=map(int,input().strip(' ').split(' '))
edges = [ edge() for i in range(m)]

while(m>0):
    u,v,w=map(int,input().strip(' ').split(' '))
    edges[m-1].u = u ; edges[m-1].v = v ;
    edges[m-1].w = w ;   m-=1

mst=getMST(edges,n)
print(mst)

