#Explanation of the program as a whole :
#The main fuction is the inputfuc which works upon the given string and accordingly stores the list of donot care and the list of ones element
#then comes the binary function which does everything and works on the Quine-Mccluskey method and the Petrick's method for programming, 
#the steps are explaned accordingly at their respective places, some helping codes is also done
#for eliminating the corner cases in the program. All steps are in accordance with the algorithm only.
#NOTE: All print statements are commented at various places, To understand the step by step working of the program uncomment them and run this program it will show every matrix on all the steps.


import numpy as np

def binary(a,olist,dlist,n):

	#STEP : Variables declaration and conversion of minterms to their binary values and storing them in the respected fashion

	variables = ['w','x','y','z']
	minexp = ''
	matrixo=[[0 for x in range(n+4)] for y in range(len(a))]
	z=0
	q=0
	l=0
	for i in a:
		bina=bin(int(i))
		bina=bina[2:]

		if(len(bina)==n):
			for i in range(0,n):
				matrixo[z][i]=int(bina[i])
			z=z+1
		else:
			remainder=n-len(bina)
			for i in range(0,remainder):
				matrixo[z][i]=0
			for j in range(remainder,len(bina)+remainder):
				matrixo[z][j]=int(bina[q])
				q=q+1
			z=z+1
			q=0

	for i in range(0,len(a)):
		matrixo[i][n+2] = matrixo[i][n+3] = int(a[i])

	for i in range(0,len(a)):
			for j in range(0,n):	
				z=matrixo[i][j]
				l=l+int(z)
			matrixo[i][n]=l
			l=0

	#Sorting on the basis of the ones colomn as per the QM method

	matrixo = sorted(matrixo, key = lambda x:x[n])

	#print("Matrix 0:")
	#print(matrixo)
	#print("\n")


	onestring1 = []

	for i in range(0,len(a)):
		onestring1.append(matrixo[i][n+3])

	#print("coloumn 1:")
	#print(onestring1)
	#print("\n")


	#STEP : The main part i.e is the Quine Mccluskey method implimentation:-

	#Here the binary are sorted on the basis of ones in them and number of ones are stored along with the binary
	#then each case is compared with the rest i.e no of ones = 0 is compared with 1,2,3 and so on according to the algo
	#if difference in binary is of one element during the comparision that digit is replaced with "X" and the process
	#moves on untill no more comparison are left. The resulting matrix is stored consisting of final binary transformation
	#along with the minterms contributing to it.

	copymatrix = matrixo

	mat = np.array(matrixo)
	l = np.unique(mat[:,n])

	coloumnsize = len(a)

	if (copymatrix[0][n] == copymatrix[coloumnsize-1][n]):
		matrix1 = matrixo

	elif((copymatrix[coloumnsize-1][n] - copymatrix[0][n])>=len(l)):
		matrix1 = matrixo

	for i in range(copymatrix[0][n],copymatrix[coloumnsize-1][n]):
		#print("Iteration " + str(i) + "\n")
		matrix1=[]
		y=0
		e=0
		counter=0
		for i in range(0,coloumnsize-1):
			for j in range(i+1,coloumnsize):
				if(matrixo[j][n]-matrixo[i][n]==1):
					for p in range(0,n):
						if(matrixo[i][p]!=matrixo[j][p]):
							e = e+1
						else:
							continue
					if(e==1):
						for b in range(n):
							if(matrixo[i][b]!=matrixo[j][b]):
								counter=b
						matrix1.append([0]*(n+4))
						for t in range(n):
							matrix1[y][t]=matrixo[j][t]
						matrix1[y][counter]='X'
						matrix1[y][n+2]=matrix1[y][n+3]=str(matrixo[i][n+2])+'-'+str(matrixo[j][n+2])
						matrixo[i][n+1] = matrixo[j][n+1] = 1
						matrix1[y][n] = matrixo[j][n]
						y=y+1
					counter=0
					e=0
				else:
					continue

		for i in range(coloumnsize):
			if(matrixo[i][n+1]!=1):
				matrix1.append(matrixo[i])
		# print("matrix 0")
		# print(matrixo)
		# print("\n")
		# print("matrix 1")
		# print(matrix1)
		# print("\n")

	#STEP : Removing the Repeatation and standardising teh matrix 


	#The repeatation of the terms are uniqed on the basis of the transformed binary and then stored in another matrix
	#The minterms in the beginning are checked if they appear here or not, for making our prime implicant matrix
	#the matrix is made according to the algo and the PImat and Pilist are made for it. The next is to select the EPI


		coloumnsize = len(matrix1)

		matrixo = matrix1
	
	matrix2 = [[0 for x in range(2)] for y in range(len(matrix1))]

	for i in range(len(matrix1)):
		matrix2[i][1]  = matrix1[i][n+3]
		for j in range(n):
			matrix2[i][0] = ''
			for k in range(n):
				matrix2[i][0] += str(matrix1[i][k])
	# print("coloumn 2")
	# print(matrix2)
	# print("\n")

	result = []
	result.append(matrix2[0])
	fl = 0
	for o in range(len(matrix2)):
		for oo in range(len(result)):
			if matrix2[o][0] != result[oo][0]:
				fl = fl+1
			if fl == len(result):
				result.append(matrix2[o])
		fl = 0


	# print("answer")
	# print(result)
	# print("\n")

	PIlength = len(olist)
	
	PImat=[[0 for x in range(PIlength+1)] for y in range(len(result))]

	for i in range(len(result)):
		if(type(result[i][1])==str):
			for j in result[i][1].split('-'):
				for k in range(PIlength):
					if(j==a[k]):
						PImat[i][k]=1
		elif(type(result[i][1])==int):
			for k in range(PIlength):
				if(str(result[i][1])==a[k]):
					#print(a[k])
					PImat[i][k]=1
	
	# print("Prime Implicant Matrix")
	# print(PImat)
	# print("\n")

	PI1list = [0 for ix in range(len(PImat[0]))]

	for x in range(len(PImat[0])):
		for y in range(len(PImat)):
			PI1list[x] += PImat[y][x]

	# print("Prime Implicatnt with 1 list: ")
	# print(PI1list)
	# print("\n")

	for x in range(len(PI1list)):
		if PI1list[x] == 1:
			for q in range(len(PImat)):
				if(PImat[q][x]==1):
					PImat[q][len(PImat[0])-1] = 1

	# print("Updated PI list:")
	# print(PImat)
	# print("\n")

	#STEP : Selection of Essential Prime Implicants

	#The selection of the EPI is done in accordance with the petricks method to include both basic as well as dont
	#cares terms in our EPI matrix as shown below
	#Now the second main step i.e to check for the dont care condition i.e done through the Petrick's method
	#the steps include the algorithm and selecting the epi from the petrick terms which should be shown in our ans
	#the P and PQ matrix/list are used for the purpose of the petrick method

	EssPI = []
	PetPI = []
	for x in range(len(PImat)):
		if PImat[x][len(PImat[0])-1] == 1:
			EssPI.append(result[x][0])
		else: 
			PetPI.append(result[x][0])

	# print("Essential Prime Implicatnt")
	# print(EssPI)
	# print("\n")

	# print("Petricks Prime Implicatnt")
	# print(PetPI)
	# print(len(PetPI))
	# print("\n")

	PQ = []
	P = [[] for y in range(len(PetPI))]

	if(len(PetPI))==1:
		pass

	elif(len(PetPI)!=0):
		for i in range(0,len(PetPI)):
			for j,k in zip(PetPI[i],range(0,n)):
				if(j=='0'):
					P[i].append(variables[k]+'`')
				elif(j=='1'):
					P[i].append(variables[k])
		PQ.append(P)
		if(len(PQ)>1):
			pass
		final_result = [min(PQ[0],key=len)]
		# print(final_result)
		for i in range(0,len(final_result)):
			for k in range(len(final_result[i])):
				for y in final_result:
					minexp += y[k]
			minexp+= ' + ' 

	for y in EssPI:
		for x in range(n):
			if y[x] == 'X':
				pass
			elif y[x] == '0':
				minexp += variables[x]+'`'
			elif y[x] == '1':
				minexp += variables[x]
		if y != EssPI[-1]:
			minexp += ' + '


	#STEP : Sorting 

	#Sorting string on the basis of the lexicographical order as per the requirement of the question


	# print("Result = ")
	minexp2=''
	#print("Result = ")
	# print(minexp)
	terms=minexp.split(' + ')
	terms.sort()
	# print(terms)
	for j,k in zip(terms,range(len(terms))):
		minexp2+=j
		if k != len(terms)-1:
			minexp2+=" + "
	return minexp2



def inputfuc(mystring,n):

	#STEP : Make the Input Suitable for the program

	#Slicing string and storing the minterms accordingly for the program

	#mystring=input()
	# mystring = '(1,3,7,11,15) d (0,2,5)'
	# mystring = '(1,2) d (8,12)'

	oneslist=[]
	dlist=[]

	if(mystring[mystring.find('d')+2] == '('):
		df=mystring.rfind('(')
		de=mystring.rfind(')')
		dstring = mystring[df+1:de]

		for i in dstring.split(','):
			dlist.append(i)

	# if (mystring[0]=='-') and len(dlist)==0:
	# 	return '0'

	#For ones list
	if (mystring[0]!='-'):
		onef=mystring.find('(')
		onee=mystring.find(')')
		onestring=mystring[onef+1:onee] #0,1,2,4,5,6,8,9,12,13,14

		for i in onestring.split(','):
			oneslist.append(i)

	#print("Coloumn 0")
	# print(oneslist)
	#print(oneslist+dlist)
	#print("\n")


	if len(oneslist+dlist) == 2**n:
		return '1'
	elif len(oneslist) == 0 and len(dlist) == 0:
		return '0'
	return binary(oneslist+dlist,oneslist,dlist,n)
	
# n=4


print("Enter the number of Vatriables:")
n=input() #Enter the value of n i.e the number of variables
n=int(n)

print("Enter the String containg the Min-terms:")
mystring=input()


# mystring = ''
# n= 4
# mystring = '(1,3,7,11,15) d (0,2,5)'


inputfuc(mystring,n)

	
	
	

	
