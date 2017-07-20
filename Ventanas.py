#!/usr/bin/env python3
"""
@author: ISC juan luis Ordoñez perez
"""
import tkinter as tk #importamos la lo libreria que nos permitira hacer una grafica
ventana=tk.Tk()
ventana.title("primer ventana")
#anchoxalto en pixeles
ventana.geometry('380x300')
#color de fondo de la ventana
ventana.configure(background='dark turquoise')

#imprimimos texto
etiqueta1=tk.Label(ventana,text="Hola mundo",bg="red",fg="white")
etiqueta1.pack(padx=20,pady=20,side=tk.LEFT)
#etiqueta1.pack(fill=tk.X) #esto sirve para cerrar la etiqueta anteriormente abierta y evitar que nos afecte el codigo
#el atributo de fill=tk.X sirve para que nuestra etiqueta se adapte al tamaño de nuestra ventana en el eje de las x

etiqueta2=tk.Label(ventana,text="Hola ",bg="gray",fg="white")
etiqueta2.pack(padx=20,pady=20,side=tk.LEFT)
#etiqueta2.pack(padx=20,pady=20)#esto sirve para cerrar la etiqueta anteriormente abierta y evitar que nos afecte el codigo
#la parte de padx=20, pady= 20 sirve para dejar espacios entre etiquetas.

etiqueta3=tk.Label(ventana,text="como estas ",bg="blue",fg="white")
etiqueta3.pack(padx=20,pady=20,side=tk.LEFT)
#etiqueta3.pack(side=tk.LEFT)#esto sirve para cerrar la etiqueta anteriormente abierta y evitar que nos afecte el codigo
#el tributo side=tk.LEFT sirve para decirle a la aplicacion hacia qie lado queremos que este alineado nuestra etiqueta

etiqueta4=tk.Label(ventana,text="lol ",bg="blue",fg="white")
etiqueta4.pack(padx=20,pady=20,side=tk.LEFT)
#etiqueta4.pack(padx=20,pady=50,ipadx=20,ipady=20)#esto sirve para cerrar la etiqueta anteriormente abierta y evitar que nos afecte el codigo
#ipadx e ipady sirve para dejar espacios dentro de la etiqueta.


#ponemos un ciclo para que no se cierre la ventana
ventana.mainloop()
