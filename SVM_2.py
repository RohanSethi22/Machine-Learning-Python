import matplotlib.pyplot as plt
import numpy as np

n=int(input('Enter number of elements in class 1: '))
m=int(input('Enter number of elements in class 2: '))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([-10,10])
ax.set_ylim([-2,100])
allx=[]
ally=[]
clicks=0

def onclick(event):
	global n, clicks, m
    #plt.clf()
	ix, iy = (event.xdata), (0)
	print('x = ', ix,'\ty = ', iy)
	clicks=clicks+1
	allx.append(ix)
	ally.append(ix*ix)
	print(clicks)
	plt.xlim(-10,10)
	plt.ylim(-2,100)
	if clicks<=n:
		plt.scatter(ix,iy,color='black')
	elif clicks<=n+m:
		plt.scatter(ix,iy,color='grey')
	elif clicks>n+m:
		plt.scatter(allx[0:n],ally[0:n],color='red')
		plt.scatter(allx[n:n+m],ally[n:n+m],color='blue')
		pi, pj, md=0, 0, 1000000
		for i in range(n):
			for j in range(n,n+m):
				print(i,' ',j)
				dist=(allx[i]-allx[j])**2+(ally[i]-ally[j])**2
				if dist<md:
					md=dist
					pi=i
					pj=j
		print(pi,' ',pj)
		px=(allx[pi]+allx[pj])/2
		py=(ally[pi]+ally[pj])/2
		xval=np.array([-10,10])
		slope=(allx[pi]-allx[pj])/(ally[pj]-ally[pi])
		intercept=-slope*px+py
		yval=slope*xval+intercept
		plt.plot(xval,yval)
		fig.canvas.mpl_disconnect(cid)

for i in range(0,1):
	cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
plt.close()