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
		
def Determinan(P1,P2,P3):
	det=((P1[0]*P2[1])+(P3[0]*P1[1])+(P2[0]*P3[1])-(P3[0]*P2[1])-(P2[0]*P1[1])-(P1[0]*P3[1]))
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
	global S1
	global S2
	
	S1=[]  			
	S2=[]
	for x in range(len(listpoint)):	
		if Determinan(leftmost,rightmost,listpoint[x])>0:				#kalau >0 berarti di kiri
			if listpoint[x] not in S1:
				S1.append(listpoint[x])
		elif Determinan(leftmost,rightmost,listpoint[x])<0:			#kalau <0 berarti di kanan
			if listpoint[x] not in S2:
				S2.append(listpoint[x])
	
	print ('S1 :',S1)
	print('S2 :',S2)
	CariHull(S1,leftmost,rightmost) #cari hull buat bagian atas
	CariHull(S2,rightmost,leftmost) #cari hull buat bagian bawah
		
def jarak(P1,P2,Point): #fungsi cari jarak
	pembilang= abs(((P2[1]-P1[1])*Point[0])-((P2[0]-P1[0])*Point[1])+(P2[0]*P1[1])-(P2[1]*P1[0]))
	return pembilang
		
def CariHull(S,P,Q):	
	if S==[]:  #kondisi berhenti jika tidak ada titik di himpunan
		return
	else:
		maks=0
		pmax=[]
		
		A=[]
		B=[]
		
		for x in range (len(S)):
			if (jarak(P,Q,S[x])>maks):      #jika menemukan jarak maksimum akan disimpan ke dalam pmax
				del pmax[:]
				maks=jarak(P,Q,S[x])
				pmax.append(S[x][0]),
				pmax.append(S[x][1])

        ConvexHull.insert(1,pmax)       #memasukkan pmax ke dalam convexhull
		
        for x in range(len(S)): 
			print 'S[x]',S[x]                #membagi titik-titik ke dalam dua partisi yang ada di luar
			if Determinan(P,pmax,S[x])>0:       #segitiga yang dibetnuk oleh P pmax dan Q
				if S[x] not in A:
					A.append(S[x])
			print('A :',A)
			if Determinan(pmax,Q,S[x])>0:
				if S[x] not in B:
					B.append(S[x])
			print('B :',B)
        CariHull(A,P,pmax)                  #melakukan rekursif
        CariHull(B,pmax,Q)    
	
    			
def drawHull(Q):

	atas=[leftmost,rightmost]
	bawah=[rightmost,leftmost]

	for x in range(len(Q)):                            #partisi titik menjadi dua bagian
		if Determinan(leftmost,rightmost,Q[x])>0:
			atas.insert(1,Q[x])
		else:
			bawah.insert(1,Q[x])
              
    
	def takeA(elem):
		return elem[0]
		
	atas.sort(key=takeA)                        #mengurutkan list sesuai partisinya
	bawah.sort(key=takeA,reverse=True)
	Q= atas+bawah

	global sets
	sets=[]                             #membuat list unik dari convex hull
	for x in range(len(Q)):
		if Q[x] not in sets:
			sets.append(Q[x])

			
	for x in range(len(sets)):                  #menampilkan set convex hull yang sudah rapi
		print 'ConvexHull: ', sets[x] 
	 
	xhull=[]
	yhull=[]
	
	for x in range(len(Q)):                 #memasukkan list poin x dan poin y convex hull
		xhull.append(Q[x][0])
		yhull.append(Q[x][1])

	plt.plot(xhull,yhull,c='green')                 #visualisasi convex hull
	plt.scatter(xhull,yhull,c='green',edgecolors='none')


inputs()
QuickHull()
plt.scatter(pointx,pointy, c='orange',edgecolors='none')
drawHull(ConvexHull)
plt.scatter([leftmost[0],rightmost[0]],[leftmost[1],rightmost[1]], c='red',edgecolors='none')
plt.show()
exit()

	
