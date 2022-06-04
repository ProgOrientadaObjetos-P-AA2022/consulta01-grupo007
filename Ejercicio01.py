
class Empresa:

	def __init__(self, nombre, numEmpleados, ciudad):
		self.nombre = nombre
		self.numEmpleados = numEmpleados
		self.ciudad = ciudad

	def obtenerNombre(self):
		return self.nombre 
	def obtenerNumEmpleados(self):
		return self.numEmpleados
	def obtenerCiudad(self):
		return self.ciudad

	def presentar(self):
		print("\nDatos de la empresa: \nNombre:",self.obtenerNombre(),"\nNumero de empleados:",
			self.obtenerNumEmpleados(),"\nCiudad: ",self.obtenerCiudad())


e1 = Empresa("SuperMaxi", 250, "Loja")
e1.presentar()
e2 = Empresa("Adidad", 785, "New York")
e2.presentar()