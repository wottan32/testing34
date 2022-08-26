from main import Persona

# if __name__ == '__main__':
print('Creacion objetos'.center(50, '-'))
persona1 = Persona('Carla', 'Gomez', 30)
persona1.mostrar_detalle()

print('Eliminacion objetos'.center(30, '-'))
del persona1