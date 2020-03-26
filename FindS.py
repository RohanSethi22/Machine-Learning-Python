import pandas as pd
import numpy as np

df=pd.read_csv("zoo.csv")

def gen(k):
    for i in range(len(S[0])):
        if S[df[df.columns[-1]][k]-1][i]=='phi':
            S[df[df.columns[-1]][k]-1][i]=df[df.columns[i]][k]
        elif S[df[df.columns[-1]][k]-1][i]=='?':
            pass
        elif S[df[df.columns[-1]][k]-1][i]==df[df.columns[i]][k]:
            pass
        else:
            S[df[df.columns[-1]][k]-1][i]='?'

S=[['phi']*(df.shape[1]-1),['phi']*(df.shape[1]-1),['phi']*(df.shape[1]-1),['phi']*(df.shape[1]-1),['phi']*(df.shape[1]-1),['phi']*(df.shape[1]-1),['phi']*(df.shape[1]-1)]
for i in range(7):
    print('Initial specific boundary S for category ',i+1,' = ',S[i])
for i in range(len(df)):
    gen(i)
    #print('S for category ',df[df.columns[-1]][i],'=',S[df[df.columns[-1]][i]-1])
for i in range(7):
    print('Final specific boundary S for category ',i+1,' = ',S[i])

