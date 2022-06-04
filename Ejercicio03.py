
class Persona:
	def __init__(self, nombre, estatura, peso, ojos, cabello):
		self.nombre = nombre
		self.estatura = estatura
		self.peso = peso 
		self.ojos = ojos 
		self.cabello = cabello
		self.icm = 0

	
	def obtenerNombre(self):
		return self.nombre
	def obtenerEstatura(self):
		return self.estatura
	def obtenerPeso(self):
		return self.peso 
	def obtenerOjos(self):
		return self.ojos
	def obtenerCabello(self):
		return self.cabello

	def calcularICM(self):
		self.icm = self.peso / (self.estatura * self.estatura)
		return self.icm

	def presentar(self):
		print("\nDatos Medicos del Paciente \nNombre: ", self.obtenerNombre(),
			"\nEstatura en m: ", self.obtenerEstatura(),"\nPeso en Kg: ", 
			self.obtenerPeso(),"\nColor de Ojos : ", self.obtenerOjos(),
			"\nColor de Cabello: ", self.obtenerCabello())
		print("Indice de Masa Corporal: ", self.calcularICM())


p1 = Persona("Pablo", 1.80, 67.50, "Café", "Negro")
p1.presentar()
p2 = Persona("Juan", 1.67, 62.80, "Verdes", "Castaño")
p2.presentar()
