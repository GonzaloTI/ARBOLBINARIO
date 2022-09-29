'''

Titulo:  (IMPLEMENTACION DE AVL Y ELIMINAR NODO)
Autor : Gonzalo Tarqui Ignacio
Fecha : 28/09/2022
Version: 2.7

'''
from Nodo import Node
#.llama a la calse Nodo
from Arbol import Arbol
#.llama a la clase Arbol

def main():
  tree = Arbol()
  print(tree.esVacio())
  tree.InsertarNodo(100)
  tree.InsertarNodo(200)
  tree.InsertarNodo(300)
  #tree.InsertarNodo(140)
  #tree.InsertarNodo(155)


  """ 100
          200
      150
  140     155  """
    
  
  print( tree.altura(tree.getRoot()) , 'de altura')

  print (tree.cantidad(tree.getRoot()) , 'cantidad')

  print (tree.amplitud( tree.getRoot()) , 'del amplitud')


  #tree.setRoot(tree.rotacionIzquierda(tree.getRoot()))

  print('----------------------preorden antes del AVL')

  #.tree.preOrden(tree.getRoot())
  tree.preOrdenDirect()

  #tree.setRoot(tree.ARBOLAVL(tree.getRoot()))
  tree.avl()

  print('----------------------preorden DESPUES DEL AVL')
  tree.preOrdenDirect()


  #tree.setRoot( tree.deleteNode(tree.getRoot(),200) ) 
  tree.deleteNodevalue(200)
  print('----------------------preorden DESPUES DEL AVL y el eliminar(200)')
  #tree.preOrden(tree.getRoot())

  tree.preOrdenDirect()


if __name__ == '__main__':
    main()






