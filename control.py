from modelo import Mediciones
from vista import Vista


class Control:
    
    def __init__(self):
        
        self.vista=Vista()
        self.modelo=Mediciones()
        
   
    def inicio(self):
        
        opcion="0"
                         
        while opcion!="s":
    
            if opcion == "0":
                opcion=self.vista.menu()
            elif opcion == "1":
                t=self.modelo.get_temperatura()
                self.vista.mostrar_temperatura(t)
                opcion="0"
            elif opcion == "2":
                p = self.modelo.get_presion()
                self.vista.mostrar_presion(p)
                opcion = "0"
            elif opcion == "4":

               self.vista.mostrar_grafico_temperatura(self.modelo.get_temperaturas())
               opcion="0" 
           
            elif opcion == "6":
               self.vista.mostrar_grafico_humedad(self.modelo.get_humedades())
               opcion="0"
              
            elif opcion == "7":
                medio = self.modelo.get_valor_medio(self.modelo.get_temperaturas())
                self.vista.mostrar_valor_medio(medio, "temperatura")
                opcion = "0"
           
            
           

            
                     
            elif opcion == "s":
               print("¡Hasta luego!")
               break
            else:
               opcion=self.vista.menu

        
