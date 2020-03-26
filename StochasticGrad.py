import numpy as np
import matplotlib.pyplot as plt
from time import sleep

x = np.arange(0,50)
y = x
allx=[]
ally=[]
learn_rate=0.001
    
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([0,10])
ax.set_ylim([0,10])
slope, intercept=0, 0

def onclick(event):
    global ix, iy
    plt.clf()
    ix, iy = (event.xdata), (event.ydata)
    print('x = ', ix,'\ty = ', iy)
    
    allx.append(ix)
    ally.append(iy)
    plt.xlim(0,10)
    plt.ylim(0,10)
    plt.scatter(allx,ally,color='red')
    err=0
    erri=0
    global intercept, slope

    for epochs in range(0,50):                  #stochastic
        for i in range(len(allx)):
    #print(i)

            err=intercept+slope*allx[i]-ally[i]
            slope=slope-learn_rate*allx[i]*err
            intercept=intercept-learn_rate*err
                
                
        xval=np.array([0,10])
        yval=xval*slope+intercept	
        #sleep(0.1)
        plt.clf()
        plt.scatter(allx,ally,color='red')
        plt.plot(xval,yval)

    '''for epochs in range(0,50):				#batch
    	for i in range(len(allx)):
	    	erri=erri+intercept+slope*allx[i]-ally[i]
	    	err=err+(intercept+slope*allx[i]-ally[i])*allx[i]
    	slope=slope-learn_rate*err
    	intercept=intercept-learn_rate*erri'''
    print('y=',slope,'x+',intercept)
    #axes=plt.gca()
    xval=np.array([0,10])
    yval=xval*slope+intercept
    plt.plot(xval,yval)

    fig.canvas.draw()
    #return coords


for i in range(0,1):

    cid = fig.canvas.mpl_connect('button_press_event', onclick)


plt.show()
print(allx,ally)