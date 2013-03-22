#! /usr/bin/env python

arr = []	# 2D Array with numbers 0-(rows*cols - 1) filling the indices

rows = input("Rows: ")
cols = input("Columns: ")

def main():
	# Fill the 2D Array
	for i in range(0, rows*cols, cols):
		temp = []
		for j in range(cols):
			temp.append(j+i)
		arr.append(temp)

	for i in range(rows):
		for j in range(cols):
			print arr[i][j],
		print

def getPos(pos):
	print
	print "Position: " + str(pos)
	print "Down " + str(pos/cols)
	print "Over " + str(pos%cols),

if __name__=="__main__":
	main()
