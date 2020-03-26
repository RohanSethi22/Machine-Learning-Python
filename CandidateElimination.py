import pandas as pd
import numpy as np
df=pd.read_csv("enjoy_sport.csv")
S=['phi']*(df.shape[1]-1)
G=['?']*(df.shape[1]-1)
gt=[G]

def gen(k):
    for i in range(len(S)):
        if S[i]=='phi':
            S[i]=df[df.columns[i]][k]
        elif S[i]=='?':
            pass
        elif S[i]==df[df.columns[i]][k]:
            pass
        else:
            S[i]='?'
def specy(k,l):
    for i in range(len(S)):
        if gt[l][i]=='?':
            pass
        elif gt[l][i]==df[df.columns[i]][k]:
            pass
        else:
            gt.pop(l)
            return -1
    return 0
def specn(k,l):
    for i in range(len(S)):
        if gt[l][i]=='?':
            vals=set()
            for m in range(k):
                if ((df[df.columns[-1]][m]=='Yes') and (df[df.columns[i]][m]!=df[df.columns[i]][k])):
                    vals.add(df[df.columns[i]][m])
            for z in vals:
                G=gt[l]
                Q=[]
                for vo in range(len(G)):
                    Q.append(G[vo])
                Q[i]=z
                gt.append(Q)
            if i==len(S)-1:
                gt.pop(l)
        elif gt[l][i]!=df[df.columns[i]][k]:
            pass
        else:
            gt.pop(k)

print('Initial specific boundary S = ',S)
print('Initial generic boundary G = ',gt)
for i in range(len(df)):
    if df[df.columns[-1]][i]=='Yes':
        gen(i)
        print('S=',S)
        j=0
        while j<len(gt):
            delta=specy(i,j)
            j=j+delta
            j=j+1
        print('G=',gt)
    else:
        for p in range(len(gt)):
            specn(i,p)
        print('S remains same.')
        print('G=',gt)
print('Final specific boundary S = ',S)
print('Final generic boundary G = ',gt)