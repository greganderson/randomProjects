#! /usr/bin/env python

def main():
	row1 = [0, 1, 2]
	row2 = [3, 4, 5]
	row3 = [6, 7, 8]
	row4 = [9, 10, 11]
	row5 = [12, 13, 14]
	test = []
	test.append(row1)
	test.append(row2)
	test.append(row3)
	test.append(row4)
	test.append(row5)
	print test
	getPos(2,test)
	getPos(4,test)
	getPos(8,test)
	getPos(5,test)
	getPos(12,test)
	getPos(11,test)
	getPos(14,test)

def getPos(pos, arr):
	print
	print "Position: " + str(pos)
	print "Down " + str(pos/len(arr))
	print "Over " + str(pos%len(arr[0])),

if __name__=="__main__":
	main()
