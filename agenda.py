class Contacto: # Nueva clase Contacto
    def __init__(self, nombre, telefono, correo, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion


class Agenda:
    def __init__(self,):
        self.contactos = []
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
                print("número 1")
            case 3:
                print("número 1")
            case 4:
                print("número 1")
            case 5:
                print("número 1")
            case 6:
                print("número 1")
            case 7:
                print("Adios")
                break

if __name__ == "__main__":
    main()
