import sys
import random
import matplotlib.pyplot as plt
import math

def inputs():
	global n
	global listpoint
	global size
	
	size=1000
	listpoint=[]
	
	n= eval(raw_input('Masukkan jumlah poin: '))
	for x in range(n):
		listpoint.append([random.randint(0,size),random.randint(0,size)])
		
def Determinan(listp):
	det=((listp[0][0]*listp[1][1])+(listp[2][0]*listp[0][1])+(listp[1][0]*listp[2][1])-(listp[2][0]*listp[1][1])-(listp[1][0]*listp[0][1])-(listp[0][0]*listp[2][1]))
	return det
	
def jarak(P1,P2,Point):
	if (P1!=[] and P2!=[] and Point!=[]):
		pembilang= abs(((P2[1]-P1[1])*Point[0])-((P2[0]-P1[0])*Point[1])+(P2[0]*P1[1])-(P2[1]*P1[0]))
		penyebut= math.sqrt(math.pow((P2[1]-P1[1]),2)+math.pow((P2[0]-P1[0]),2))
		if penyebut>0:
			return (pembilang/penyebut)
		else:
			return 0
				
def QuickHull():
	global leftmost
	global rightmost
	global ConvexHull
	
	leftmost=[size,0]
	rightmost=[0,size]
	ConvexHull=[]

#================= Mencari titik terkanan dan terkiri ===================#	
	for x in range(len(listpoint)):
		if leftmost[0]>listpoint[x][0]:
			leftmost=listpoint[x]
		if rightmost[0]<listpoint[x][0]:
			rightmost=listpoint[x]
	ConvexHull.append(leftmost)
	ConvexHull.append(rightmost)
	
	#print ("Leftmost: ",leftmost)
	#print ("Rightmost: ",rightmost)
	
#================== Ngebagi dua area ====================================#

	global S1
	global S2
	global Hitung
	
	S1=[]
	S2=[]
	Hitung=[]
	
	Hitung.append(leftmost)
	Hitung.append(rightmost)
	for x in range (len(listpoint)):
		Hitung.append(listpoint[x])
		if Determinan(Hitung)>0:
			S1.append(listpoint[x])
		elif Determinan(Hitung)<0:
			S2.append(listpoint[x])
		del Hitung[2]
	
	#print ('S1 : ',S1)
	#print ('S2 : ',S2)
#=======================Rekursif====================================#	
			
	FindHull(S1,leftmost,rightmost)
	FindHull(S2,rightmost,leftmost)
	
#===================================================================+#

def FindHull(S,P,Q):
	
	global pmax
	pmax=P
	
	if S==[]:
		pass
	else:
		#==================== cari pmax ===============================================#
		for x in range(len(S)):
			if jarak(P,Q,S[x])>jarak(P,Q,pmax):
				pmax = S[x]
		ConvexHull.insert(1,pmax)
		
		#print ('Pmax : ',pmax)
		#===================== nyari yang di kanan sama di kiri dari garis =============#
			
		global kanan
		global kiri
		global Mat
		
		kanan=[]
		kiri=[]
		Mat= []
		
		Mat.append(P)
		Mat.append(pmax)
		for x in range (len(S)):
			Mat.append(S[x])
			if Determinan(Mat)>0:
				kiri.append(S[x])
			del Mat[2]
						
		Mat.append(pmax)
		Mat.append(Q)
		for x in range (len(S)):
			Mat.append(listpoint[x])
			if Determinan(Mat)<0:
				kanan.append(S[x])
			del Mat[2]
				
	FindHull(kiri,P,pmax)
	FindHull(kanan,pmax,Q)
	
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
			atas.insert(1,Q[x])
		else:
			bawah.insert(1,Q[x])
		del MatrixDet[2]
	
	def takeA(elem):
		return elem[0]
		
	del Q[:]
	S1.sort(key=takeA)
	S2.sort(key=takeA,reverse=True)
	Q= atas+bawah
	
	print('ConvexHull: ', Q)
	xhull=[]
	yhull=[]
	
	for x in range(len(Q)):
		xhull.append(Q[x][0])
		yhull.append(Q[x][1])
	
	plt.plot(xhull,yhull,c='green')
	plt.scatter(xhull,yhull,c='green',edgecolors='none')
		

inputs()
QuickHull()

drawHull(ConvexHull)
#plt.scatter([leftmost[0],rightmost[0]],[leftmost[1],rightmost[1]], c='green',edgecolors='none')
#plt.plot([leftmost[0],rightmost[0]],[leftmost[1],rightmost[1]],c='green')
plt.scatter(pointx,pointy, c='orange',edgecolors='none')
#plt.scatter(S1[,pointy, c='orange',edgecolors='none')
plt.show()
exit()
		
			
		
		
		
