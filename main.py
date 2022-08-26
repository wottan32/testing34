class Persona:
  def __init__(self, nombre, apellido, edad):
    self._nombre = nombre
    self._apellido = apellido
    self._edad = edad

  @property
  def nombre(self):
    print('Llamando método get nombre')
    return self._nombre

  @property
  def apellido(self):
    print('Llamando método get apellido')
    return self._apellido

  @property
  def edad(self):
    print('Llamando método get edad')
    return self._edad

  @nombre.setter
  def nombre(self, nombre):
    self._nombre = nombre

  @apellido.setter
  def apellido(self, apellido):
    self._apellido = apellido

  @edad.setter
  def edad(self, edad):
    self._edad = edad
    

  def mostrar_detalle(self):
    print(f'Persona: {self._nombre} {self.apellido} {self.edad}')

  def __del__(self):
    print(f'Persona: {self._nombre} {self._apellido}')

    
if __name__ == '__main__':
  persona1 = Persona('Juan', 'Perez', 28)
  # print(persona1.nombre)
  persona1.nombre = 'Juan Carlos'
  persona1.apellido = 'Torres'
  persona1.edad = 32
  print(persona1.nombre)
  print(persona1.apellido)
  print(persona1.edad)
# persona1.mostrar_detalle()
  print(__name__)
