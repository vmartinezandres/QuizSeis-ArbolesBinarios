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

    def AgregarNodo(self, value):
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
                        
    def EncontrarNodo(self, first, value):
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

    def EncontrarPenultimoNodo(self, first, value):
            if first.value != value and first != None:
                nodo = first
                PenultimoNodo = nodo
                while value != nodo.value:
                    if value < nodo.value:
                        if nodo.left != None:
                            PenultimoNodo = nodo
                            nodo = nodo.left
                        
                        else:
                            return None
                        
                    else:
                        if nodo.right != None:
                            PenultimoNodo = nodo
                            nodo = nodo.right

                        else:
                            return None

                return PenultimoNodo
            
            else:
                return None
        
    def BuscarMin(self, first):
        if first != None:
            while first.left != None:
                first = first.left
            
            return first
        
        else:
            return None


    def BuscarMax(self, first):
        if first != None:
            while first.right != None:
                first = first.right
            
            return first
        
        else:
            return None


    def Eliminar(self, first, value):
        if first != None:
            nodo = self.EncontrarNodo(first, value)
            if nodo != None:
                if nodo.left == None and nodo.right == None:
                    PenultimoNodo = self.EncontrarPenultimoNodo(first, nodo.value)              

                    if PenultimoNodo.left != None and PenultimoNodo.left.value == nodo.value:
                        PenultimoNodo.left = None
                    else:
                        PenultimoNodo.right = None
                
                else:
                    if nodo.left != None:
                        NodoRemplazo = self.BuscarMax(nodo.left)

                        nodo.value = NodoRemplazo.value

                        if nodo.left.value == NodoRemplazo.value:
                            if NodoRemplazo.left != None:
                                nodo.left = NodoRemplazo.left
                            else:
                                nodo.left = None 
                        
                        else:
                            self.Eliminar(nodo.left, NodoRemplazo.value)

                    else:
                        NodoRemplazo = self.BuscarMin(nodo.right)
                        nodo.value = NodoRemplazo.value
                        if nodo.right.value == NodoRemplazo.value:
                            if NodoRemplazo.right != None:
                                nodo.right = NodoRemplazo.right      
                            else:
                                nodo.right = None

                        else:
                            self.Eliminar(nodo.right, NodoRemplazo.value)                       

    def ImprimirInOrden(self, first):
        if first != None:
            self.ImprimirInOrden(first.left)
            print(first.value)
            self.ImprimirInOrden(first.right)
            

    def ImprimirPreOrden(self, first):
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
                self.ImprimirPreOrden(nodo)
                
            else: # si llega al final a una hoja
                if self.tail != None: # si tail existe
                    if nodo.value != self.tail.value: 
                        NodoTail = self.tail
                        if self.tail.prev != None:
                            self.tail = self.tail.prev
                            NodoTail.prev = None
                        
                        self.ImprimirPreOrden(NodoTail); 
                       
                    else:
                        self.tail = None
                        

    def ImprimirPostOrden(self, first):
        if first != None:
            self.ImprimirPostOrden(first.left)
            self.ImprimirPostOrden(first.right)
            print(first.value)
    
