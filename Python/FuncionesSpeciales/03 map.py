class Empleado:

	def __init__(self,nombre,cargo,salario):

		self.nombre = nombre
		self.cargo = cargo
		self.salario = salario 

	def __str__(self):

		return "{} que trabaja como {} tiene un salario de {}".format(self.nombre, self.cargo,self.salario)

empleados = [
	Empleado("Juan","Director",6700),
	Empleado("Ana","Presidenta",7000),
	Empleado("Antonio","Admin",2000),
	Empleado("Sara","Secreataria",2100),
	Empleado("Mario","Botones",1800),
	
]

def comision(empleado):
	if(empleado.salario <= 3000):
		empleado.salario = empleado.salario * 1.03
	return empleado

#Lo que hace es aplicar una funcion a toda a una lista
comisiones = map(comision, empleados)

for men in comisiones:
	print(men)