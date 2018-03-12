from numpy import * 

def createMatrix():
	x = array([[1, 2, 3, 4],
		[5, 6, 7, 8],
		[9, 10, 11, 12],
		[13, 14, 15, 16]])
	print(x)
	return x

def addZerosCol(matrix):
	matrix = insert(matrix,[0],[[0],[0],[0],[0]],axis=1)
	print(matrix)

def addZerosRow(matrix):
	matrix = insert(matrix,[0],[[0, 0, 0, 0]],axis=0)
	print(matrix)

def deleteData(matrix):
	matrix = delete(matrix,[1],0)
	print(matrix)

def whatYouNeed(matrix):
	matrix = insert(matrix,[0],[[0],[0],[0],[0]],axis=1)
	matrix = insert(matrix,[0],[[0, 0, 0, 0, 0]],axis=0)
	matrix = delete(matrix,[4],0)
	matrix = delete(matrix,[4],1)
	print(matrix)

if __name__ == "__main__":
	matrix = createMatrix()
	addZerosCol(matrix)
	addZerosRow(matrix)
	deleteData(matrix)
	whatYouNeed(matrix)
