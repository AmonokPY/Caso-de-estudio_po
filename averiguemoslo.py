#encapsulamiento: atributos/ocultos-> no tienen que ser accecibles desde fuera de la class
class libro:
    def __init__(self, nombre, autor,año, ISBN):
        self._nombre= nombre #<- protegido
        self.__autor= autor #<- Privado
        self.año=año #<-Publico
        self.__ISBN=ISBN
    #slef-> representacion mismas de un ojetop dentro de la clase que esta representando
       
    
    def obtener_información(self):
        print (f"El libro titulado:{self._nombre}, del autor {self.__autor}, publicado en {self.año}")
    
    @property#->
    def nombre(self):
        return self._nombre
        
    def set_nombre(self,nuevo_nombre):
        self._nombre
        

libro1= libro(" Sobreviviendo","Joseph Jimenez", "2024", "hgcdgc1")
libro1.obtener_información()
print(libro1.nombre)