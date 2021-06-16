import networkx as nx
#import graphviz
from networkx.algorithms.operators.product import _init_product_graph
from networkx.classes.function import edges, info
from networkx.drawing import nx_agraph
from networkx.generators.trees import prefix_tree
import os
from os import remove


Columnas=[]
Filas=[]
lista=[]
lista2=[]

G=  nx.DiGraph()

G.add_node("Daniel")
G.add_node("Javier")
G.add_node("Kimberly")
G.add_node("Fernando")

G.add_edge("Daniel", "Javier")
G.add_edge("Javier", "Kimberly")

for i in G.nodes:
  Columnas.append(i)
  Filas.append(i)

r = len(Columnas)+1
for i in range (r):
    lista.append(0)
    lista2.append(0)

print(lista)
listaFinal=[]
print(lista[0])

x=1
for i in Filas:
    lista=lista2.copy()
    
    #x=1
    lista[0]=i
    for edge in G.edges:
        
        x=1
        for j in Columnas:
            
            if ((i==edge[0] and j == edge[1]) or (i==edge[1] and j == edge[0])):

                
                lista[x]=1
            #print(x)
            x+=1
        #x=1
    print("Lista a guardar: " + str(lista))
    listaFinal.append(lista)
    print(lista)
    print(lista2)
    print("Se vuelven 0 otra vez")
   
    #for i in range(len(lista)):
    #    lista2[i]=0


for columna in Columnas:
    print(columna)

print(listaFinal)
for i in listaFinal:
    print(i)
    


 
#A = nx.nx_agraph.to_agraph(G)
#A.layout('dot')
#A.draw('salida.png') # guardar como png
 
#graphviz.Source(A.to_string()) # mostrar en jupyter