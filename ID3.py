import pandas as pd
import numpy as np
import math

def entropy(db):
    ent=0
    tc=db[db.columns[-1]].value_counts()
    for i in range(tc.size):
        pi=tc[i]/len(db)
        ent=ent-pi*math.log2(pi)
    return ent

def gain(db):
    gn=[0]*(len(db.columns)-1)
    for ci in range(1,len(db.columns)-1):
        gn[ci]=entropy(db)
        cv=db[db.columns[ci]].value_counts()
        for val in range(len(cv)):
            mdb=db[db[db.columns[ci]]==cv.index[val]]
            gn[ci]=gn[ci]-(cv[val]/len(db))*entropy(mdb)
            #print(mdb)
            #print('Entropy=',cv.index[val],' = ',entropy(mdb))
        #print('Gain ',db.columns[ci],' = ',gn[ci])
    return gn.index(max(gn))

def id(cur,depth):
    if entropy(cur)!=0:
        spc=gain(cur)
        print('\t'*depth,'->Splitting along ',cur.columns[spc])
        cv=cur[cur.columns[spc]].value_counts()
        for val in range(len(cv)):
            mdb=cur[cur[cur.columns[spc]]==cv.index[val]]#.pop(cur.columns[spc])
            print('\t'*depth,'#',cv.index[val])#,'\n',mdb)
            id(mdb,depth+1)
    else:
        print('\t'*depth,'Entropy is zero.')

df=pd.read_csv("play_tennis.csv")
id(df,0)