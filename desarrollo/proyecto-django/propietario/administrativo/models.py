from django.db import models


class Propietario(models.Model):
    opcionesTipo = (
		('ecuador', 'ecuatoriana'),
		('peru', 'peruana'),
		('colombia', 'colombiana'),
	)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField("Edad")
    nacionalidad = models.CharField(max_length=30, choices=opcionesTipo)

    def __str__(self):
        return "%s %s %d %s" % (self.nombre,
                self.apellido,
                self.edad,
                self.nacionalidad)

class Departamento(models.Model):
    costo_departamento = models.DecimalField(max_digits=100, decimal_places=2)
    numero_cuartos = models.IntegerField("numero de cuartos")
    numero_banios = models.IntegerField("numero de banos")
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE,
            related_name="departamentos")
    valor_alicuota = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return "%f %f" % (self.costo_departamento, self.valor_alicuota)