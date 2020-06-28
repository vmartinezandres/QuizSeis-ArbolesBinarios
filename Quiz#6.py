class Nodo:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.prev = None

class ArbolBinario:
    def __init__(self):
        self.root = None
        self.tail = None

    def agregarNodo(self, value):
        if self.root == None:
            self.root = Nodo(value)
        else:
            father = self.root

            while value != father.value:
                if value < father.value:
                    if father.left == None:
                        father.left = Nodo(value)
                        break
                    
                    else:
                        father = father.left
                
                else:
                    if father.right == None:
                        father.right = Nodo(value)
                        break
            
                    else:
                        father = father.right
                        
    def encontrarNodo(self, first, value):
        if first != None:
            nodo = first
            while value != nodo.value:
                if value < nodo.value:
                    if nodo.left != None:
                        nodo = nodo.left

                    else:
                        return None;
                    
                else:
                    if nodo.right != None:
                        nodo = nodo.right
                    
                    else:
                        return None
                    
            return nodo
        
        else:
            return None

    def encontrarPenultimoNodo(self, first, value):
            if first.value != value and first != None:
                nodo = first
                penultimoNodo = nodo
                while value != nodo.value:
                    if value < nodo.value:
                        if nodo.left != None:
                            penultimoNodo = nodo
                            nodo = nodo.left
                        
                        else:
                            return None
                        
                    else:
                        if nodo.right != None:
                            penultimoNodo = nodo
                            nodo = nodo.right

                        else:
                            return None

                return penultimoNodo
            
            else:
                return None
        
    def buscarMin(self, first):
        if first != None:
            while first.left != None:
                first = first.left
            
            return first
        
        else:
            return None


    def buscarMax(self, first):
        if first != None:
            while first.right != None:
                first = first.right
            
            return first
        
        else:
            return None


    def eliminar(self, first, value):
        if first != None:
            nodo = self.encontrarNodo(first, value)
            if nodo != None:
                if nodo.left == None and nodo.right == None:
                    penultimoNodo = self.encontrarPenultimoNodo(first, nodo.value)              

                    if penultimoNodo.left != None and penultimoNodo.left.value == nodo.value:
                        penultimoNodo.left = None
                    else:
                        penultimoNodo.right = None
                
                else:
                    if nodo.left != None:
                        nodoRemplazo = self.buscarMax(nodo.left)

                        nodo.value = nodoRemplazo.value

                        if nodo.left.value == nodoRemplazo.value:
                            if nodoRemplazo.left != None:
                                nodo.left = nodoRemplazo.left
                            else:
                                nodo.left = None 
                        
                        else:
                            eliminar(nodo.left, nodoRemplazo.value)

                    else:
                        nodoRemplazo = self.buscarMin(nodo.right)
                        nodo.value = nodoRemplazo.value
                        if nodo.right.value == nodoRemplazo.value:
                            if nodoRemplazo.right != None:
                                nodo.right = nodoRemplazo.right      
                            else:
                                nodo.right = None

                        else:
                            eliminar(nodo.right, nodoRemplazo.value)                       

    def imprimirInOrden(self, first):
        if first != None:
            self.imprimirInOrden(first.left)
            print(first.value)
            self.imprimirInOrden(first.right)
            

    def imprimirPreOrden(self, first):
        if first != None:
            nodo = first
            while nodo.left != None: # Mientras tenga hijo izquierdo
                if nodo.right != None: # Si tiene dos hijos
                    if self.tail == None:
                        self.tail = nodo.right
                    else:
                        if nodo.value != self.tail.value: # si el padre no es el tail
                            nodo.right.prev = self.tail 
                        self.tail = nodo.right                           
                    
                print(nodo.value)
                nodo = nodo.left
    
            print(nodo.value)

            if nodo.right != None: # Si llega al final y tiene hijo derecho
                if self.tail != None and nodo.value == self.tail.value:
                    self.tail = None  
                nodo = nodo.right
                self.imprimirPreOrden(nodo)
                
            else: # si llega al final a una hoja
                if self.tail != None: # si tail existe
                    if nodo.value != self.tail.value: 
                        nodoTail = self.tail
                        if self.tail.prev != None:
                            self.tail = self.tail.prev
                            nodoTail.prev = None
                        
                        self.imprimirPreOrden(nodoTail); 
                       
                    else:
                        self.tail = None
                        

    def imprimirPostOrden(self, first):
        if (first != None):
            self.imprimirPostOrden(first.left)
            self.imprimirPostOrden(first.right)
            print(first.value)
    
