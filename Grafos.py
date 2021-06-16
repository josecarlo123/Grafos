import networkx as nx
import graphviz
from networkx.algorithms.operators.product import _init_product_graph
from networkx.classes.function import edges, info
from networkx.drawing import nx_agraph
from networkx.generators.trees import prefix_tree

G = nx.DiGraph()

Presentacion=[]



def IngresarNodo():
    print("Ingrese el nombre del nodo: ")
    nombre=str(input())
    print("Ingrese la informacion que llevara "+ nombre)
    info=str(input())
    G.add_node(nombre)
    G.nodes[nombre]["Informacion"] = info

def leerNodos():
    print("Estos son los nodos que han sido ingresados:")
    for nodo in G.nodes:
        print(nodo)

def Unir2Nodos():
    print("Ingrese el nombre del primer nodo a unir: ")
    nodo1=str(input())
    print("Ingrese el nombre del segundo nodo a unir: ")
    nodo2=str(input())
    G.add_edge(nodo1, nodo2)

    
def verSusesor():
    print("Ingrese un nodo")
    nod =input()
    try:
        print("Susessor de " +nod+" "+ list(G.successors(nod))[0])
    except:
        print("No hay susesor"+ nod)
    try:
        print("Predesesor de " +nod+ " "+list(G.predecessors(nod))[0])
    except:
        print("No hay predesesor de")

def verinfonodo():
    print("Ingrese un nodo")
    nod =input()
    print("La informacion del nodo: "+nod+" es: "+G.nodes[nod]["Informacion"])

if __name__=="__main__":

    while True:
        print("1) Ingresar nodo")
        print("2) Conectar 2 nodos")
        print("3) Ver susesor y predesesor")
        print("4) Ver info del nodo")
        print("Escoja una opcion: ")
        valor=int(input())
        if valor==1:
            IngresarNodo()
        elif valor==2:
            leerNodos()
            Unir2Nodos()
        elif valor==3:
            verSusesor()
            list(G.nodes)
        elif valor==4:
            verinfonodo()
            #prueba()
           # prueba2()
        else:
            print("Opcion incorrecta.")