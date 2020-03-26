import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,50)
y = x
allx=[]
ally=[]
    
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([0,10])
ax.set_ylim([0,10])

def onclick(event):
    global ix, iy
    plt.clf()
    ix, iy = (event.xdata), (event.ydata)
    print('x = ', ix,'\ty = ', iy)
    
    coords = [ix, iy]
    allx.append(ix)
    ally.append(iy)
    plt.xlim(0,10)
    plt.ylim(0,10)
    plt.scatter(allx,ally) #color='red'

    tx=allx
    ty=ally
    tx=tx-np.mean(allx)
    ty=ty-np.mean(ally)
    temp=tx*ty
    temps=tx*tx
    n, d = sum(temp), sum(temps)
    if d==0:
    	pass
    else:
    	slope=n/d
    	intercept=np.mean(ally)-slope*np.mean(allx)
    	print('y=',slope,'x+',intercept)
    	#axes=plt.gca()
    	xval=np.array([0,10])
    	yval=xval*slope+intercept
    	plt.plot(xval,yval)

    fig.canvas.draw()
    return coords


for i in range(0,1):

    cid = fig.canvas.mpl_connect('button_press_event', onclick)


plt.show()
print(allx,ally)