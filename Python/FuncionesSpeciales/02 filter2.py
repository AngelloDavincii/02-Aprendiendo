class Empleado:

	def __init__(self,nombre,cargo,salario):

		self.nombre = nombre
		self.cargo = cargo
		self.salario = salario 

	def __str__(self):

		return "{} que trabaja como {} tiene un salario de {}".format(self.nombre, self.cargo,self.salario)

empleados = [
	Empleado("Juan","Director",75000),
	Empleado("Ana","Presidenta",85000),
	Empleado("Antonio","Admin",55000),
	Empleado("Sara","Secreataria",35000),
	Empleado("Mario","Botones",25000),
	
]

salarios =filter(lambda empleado: empleado.salario > 50000, empleados)

for sal in salarios:
	print(sal)