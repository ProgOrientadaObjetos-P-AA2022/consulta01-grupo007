
class Auto:
	def __init__(self, marca, anio, precio, color, placa):
		self.marca = marca
		self.anio = anio
		self.precio = precio
		self.color = color
		self.placa = placa 

	def obtenerMarca(self):
		return self.marca 
	def obtenerAnio(self):
		return self.anio 
	def obtenerPrecio(self):
		return self.precio 
	def obtenerColor(self):
		return self.color 
	def obtenerPlaca(self):
		return self.placa 

	def presentar(self):
		print("\nAutos: \nMarca: " + self.obtenerMarca() + "\nAño: " +
			self.obtenerAnio() + "\nPrecio: " + self.obtenerPrecio() +
			"\nColor: " + self.obtenerColor() + "\nPlaca: " + 
			self.obtenerPlaca())


auto1 = Auto("Nissan", "2012", "25000", "Marfil", "LBA-778")
auto1.presentar()
auto2 = Auto("BMW", "2021", "47600", "Negro", "MCB-250")
auto2.presentar()
auto3 = Auto("Hyundai", "2019", "35800", "Plateado", "TDH-354")
auto3.presentar()


