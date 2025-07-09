class Contacto: # Se define la clase Contacto. Esta clase servirá como un 'molde' para crear objetos que representen contactos individuales en la agenda.
    def __init__(self, nombre, telefono, correo, direccion): # Se define el método constructor (__init__) para la clase Contacto. Recibe 'self' (la instancia del objeto que se está creando) y los datos iniciales de un contacto: nombre, telefono, correo y direccion.
        self.nombre = nombre # Se asigna el valor del parámetro 'nombre' al atributo 'nombre' de la instancia del Contacto.
        self.telefono = telefono # Se asigna el valor del parámetro 'telefono' al atributo 'telefono' de la instancia del Contacto.
        self.correo = correo # Se asigna el valor del parámetro 'correo' al atributo 'correo' de la instancia del Contacto.
        self.direccion = direccion # Se asigna el valor del parámetro 'direccion' al atributo 'direccion' de la instancia del Contacto.


class Agenda: # Se define la clase Agenda. Esta clase actuará como un molde para crear objetos de tipo Agenda.
    def __init__(self): # Se define el método constructor (__init__). Este método se ejecuta automáticamente cada vez que se crea una nueva instancia (objeto) de la clase Agenda.
        self.contactos = [] # Se inicializa una lista vacía llamada 'contactos' como un atributo de la instancia de Agenda. Aquí se guardarán todos los contactos que se añadan a la agenda.
    
    def añadir_contacto(self, contacto): # Se define un método llamado 'añadir_contacto' dentro de la clase Agenda. Recibe 'self' (la instancia de la Agenda) y un objeto 'contacto' (que se espera sea una instancia de la clase Contacto) como parámetros.
        self.contactos.append(contacto) # Se añade la instancia del objeto 'contacto' (que contiene el nombre, teléfono, correo y dirección) a la lista 'self.contactos' de la agenda.
    
def eliminar_contacto(self, nombre): # Se define un método llamado 'eliminar_contacto' dentro de la clase Agenda. Recibe 'self' (la instancia de la Agenda) y el 'nombre' del contacto a eliminar como parámetros.
    for contacto in self.contactos: # Se inicia un bucle que itera sobre cada 'contacto' (instancia de Contacto) que ya está guardado en la lista 'self.contactos'.
        if nombre == contacto.nombre: # Se compara el 'nombre' proporcionado con el atributo 'nombre' de cada 'contacto' en la lista. Si coinciden, significa que se encontró el contacto a eliminar.
            self.contactos.remove(contacto) # Si se encuentra la coincidencia, se elimina esa instancia específica de 'contacto' de la lista 'self.contactos'.
            return True # Se retorna 'True' para indicar que el contacto fue encontrado y eliminado exitosamente.
    return False # Si el bucle termina (es decir, se recorrieron todos los contactos) y no se encontró ninguna coincidencia, se retorna 'False' para indicar que el contacto no fue encontrado.
    
    def buscar_contacto(self, criterio):
        pass



def mostrar_menu():
    print("""
    MENU AGENDA
          1. agregar contacto
          2. eliminar un contacto
          3. buscar un contacto
          4. listar contactos
          5. guardar en fichero
          6. cargar desde fichero
          7. salir
    """)
        
def main():
    while True:
        mostrar_menu()
        num = int(input("Ingrese una opción: "))
        match num:
            case 1:
                print("número 1")
            case 2:
                print("número 2")
            case 3:
                print("número 3")
            case 4:
                print("número 4")
            case 5:
                print("número 5")
            case 6:
                print("número 6")
            case 7:
                print("Adios")
                break

if __name__ == "__main__":
    main()