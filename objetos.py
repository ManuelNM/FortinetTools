#!/usr/bin/python

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