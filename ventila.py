from pyswip import Prolog


archivo = Prolog
archivo.consult("ventilador.pl")

motor = input("Introduce el estado del motor: ") 
aspa = input("Introduce el estado del aspa: ") 
interruptor = input("Introduce el estado del interruptor: ") 

result = bool(list(archivo.query(f"tiene_arreglo({motor},{aspa},{interruptor})")))

print("El ventilador tiene arreglo." if result else "El ventilador no tiene arreglo.")