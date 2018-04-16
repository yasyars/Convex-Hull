import sys
import random
import matplotlib.pyplot as plt
import math


def inputs():
	global n
	global listpoint
	global size
	global pointx
	global pointy
	
	size=100
	listpoint=[]
	pointx=[]
	pointy=[]
	
	n= eval(raw_input('Masukkan jumlah poin: '))
	for x in range(n):
		listpoint.append([random.randint(0,size),random.randint(0,size)])
			
	for x in range(len(listpoint)):
		pointx.append(listpoint[x][0])
		pointy.append(listpoint[x][1])
		
def Determinan(listp):
	det=((listp[0][0]*listp[1][1])+(listp[2][0]*listp[0][1])+(listp[1][0]*listp[2][1])-(listp[2][0]*listp[1][1])-(listp[1][0]*listp[0][1])-(listp[0][0]*listp[2][1]))
	return det
	
def QuickHull():
	global leftmost
	global rightmost
	global ConvexHull

#========================= cari paling kiri sama paling kanan =====================+#	

	leftmost=[size,50]
	rightmost=[0,50]
	ConvexHull=[]
	for x in range(len(listpoint)):
		if listpoint[x][0]<leftmost[0]:
			leftmost=listpoint[x]
			
	for x in range(len(listpoint)):
		if listpoint[x][0]>rightmost[0]:
			rightmost=listpoint[x]

	
	print ('leftmost: ',leftmost)
	print ('rightmost: ',rightmost)
	ConvexHull.append(leftmost)
	ConvexHull.append(rightmost)
	
#=========================== cari atas bawah =======================================#
	global MatrixDet
	global S1
	global S2
	
	S1=[]  			
	S2=[]
	MatrixDet= []
	MatrixDet.append(leftmost)
	MatrixDet.append(rightmost)
	for x in range(len(listpoint)):	
		MatrixDet.append(listpoint[x])	
		if Determinan(MatrixDet)>0:				#kalau >0 berarti di kiri
			S1.append(listpoint[x])
		elif Determinan(MatrixDet)<0:			#kalau <0 berarti di kanan
			S2.append(listpoint[x])
		del MatrixDet[2]
	#print MatrixDet
	
	CariHull(S1,leftmost,rightmost) #cari hull buat bagian atas
	CariHull(S2,rightmost,leftmost) #cari hull buat bagian bawah
	
	#print ('S1 :', S1)
	#print ('S2 :', S2)

		
def jarak(P1,P2,Point): #fungsi cari jarak
	#print ('P1 :', P1)
	#print ('P2 :', P2)
	#print ('Point :', Point)
	
	pembilang= abs(((P2[1]-P1[1])*Point[0])-((P2[0]-P1[0])*Point[1])+(P2[0]*P1[1])-(P2[1]*P1[0]))
	penyebut= math.sqrt(math.pow((P2[1]-P1[1]),2)+math.pow((P2[0]-P1[0]),2))
	if penyebut>0:
		return (pembilang/penyebut)
	else:
		return 0
	
def CariHull(S,P,Q):
	
	global pmax
	
	
	if S==[]:
		#print ('hahahah berhenti yeyeyey')
		pass
	else:
		maks=0
		pmax=[]
		
		del pmax[:]
		for x in range (len(S)): 
			print ('P :',P)
			print ('Q :', Q)
			print ('S[x] :' ,S[x])
			if (jarak(P,Q,S[x])>maks):
				maks=jarak(P,Q,S[x])
				pmax= S[x][:]		
		if pmax not in ConvexHull:
			ConvexHull.insert(1,pmax)
		
		#print ('Convex Hull a: ',ConvexHull)
		#print ('List poin: ',listpoint)
		
		global A
		global B

		A=[]
		B=[]
	
		del MatrixDet[:]
		MatrixDet.append(pmax)
		MatrixDet.append(Q)

		for x in range(len(S)):
			if S[x] not in MatrixDet:
				MatrixDet.append(S[x])
				if Determinan(MatrixDet)>0:
					B.append(S[x])
				del MatrixDet[2]
		
		del MatrixDet[:]
		MatrixDet.append(P)
		MatrixDet.append(pmax)
		for x in range(len(S)):
			if S[x] not in MatrixDet:
				MatrixDet.append(S[x])	
				if Determinan(MatrixDet)>0:
					A.append(S[x])
				del MatrixDet[2]
		
		print ('Pmax= ',pmax)
		CariHull(A,P,pmax)
		CariHull(B,pmax,Q)
		
			
def drawHull(Q):
	global xhull
	global yhull
	global atas
	global bawah
	
	MatrixDet= []
	atas=[leftmost,rightmost]
	bawah=[rightmost,leftmost]
	MatrixDet.append(leftmost)
	MatrixDet.append(rightmost)

	for x in range(len(Q)):
		MatrixDet.append(Q[x])	
		if Determinan(MatrixDet)>0:
			atas.insert(1,MatrixDet[2])
		else:
			bawah.insert(1,MatrixDet[2])
		del MatrixDet[2]
	
	def takeA(elem):
		return elem[0]
		
	del Q[:]
	atas.sort(key=takeA)
	bawah.sort(key=takeA,reverse=True)
	Q= atas+bawah
	
	for x in range(len(Q)):
		print ('ConvexHull: ',Q[x])
	#print('ConvexHull: ', Q)
	xhull=[]
	yhull=[]
	
	for x in range(len(Q)):
		xhull.append(Q[x][0])
		yhull.append(Q[x][1])
	
	plt.plot(xhull,yhull,c='green')
	plt.scatter(xhull,yhull,c='green',edgecolors='none')


inputs()
QuickHull()
plt.scatter(pointx,pointy, c='orange',edgecolors='none')
drawHull(ConvexHull)
plt.scatter([leftmost[0],rightmost[0]],[leftmost[1],rightmost[1]], c='red',edgecolors='none')
#plt.plot([leftmost[0],rightmost[0]],[leftmost[1],rightmost[1]],c='green')
#plt.scatter(S1[,pointy, c='orange',edgecolors='none')
plt.show()
exit()

	
