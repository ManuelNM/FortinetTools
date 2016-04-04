#!/usr/bin/python
"Search in file todo.txt (all objects) the elements that are in the file buscar.txt and print the edit line and the following 3 lines."
f1=open("todo.txt","r")
l1=f1.readlines()

f2=open("buscar.txt","r")
l2=f2.readlines()

for buscar in l2 :
	for i in range(0,len(l1)):
		if buscar[:-1] in l1[i]:
			print l1[i],
			print l1[i+1],
			print l1[i+2],
			print l1[i+3],
