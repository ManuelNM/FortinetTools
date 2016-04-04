#!/usr/bin/python
"""
Script para crear rutas en el firewall
1.- Crea un archivo CLIrutas.txt con los comandos a escribir.
Lee del archivo rutas.txt
La esctructura del archivo es:
Destino;Interfaz;Prioridad;Gateway
"""

archivo="rutas.txt"
file_objetos=open(archivo,"r")
final=open("CLIrutas.txt","w")
print "[*] Inicia"

i=1
final.write("config router static\n") #Inicia
for line in file_objetos:
	usar=line.split(";")
	destino=usar[0]
	interfaz=usar[1]
	prioridad=usar[2]
	gateway=usar[3][:-1]
	final.write("edit "+str(i)+"\n")
	final.write("set device "+interfaz+"\n")
	final.write("set priority "+prioridad+"\n")
	final.write("set dst "+destino+"\n")
	final.write("set distance 2\n")
	if (gateway!='-'):
		final.write("set gateway "+gateway+"\n")
	final.write("next\n")
	i+=1
final.write("end\n")
final.close()

print "[*] Saliendo";
