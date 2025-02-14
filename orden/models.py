from django.db import models

class Orden(models.Model):
    MODALIDAD_CHOICES = [
        ('particular', 'Particular'),
        ('terceros', 'Contra terceros'),
        ('riesgo', 'Contra todo riesgo'),
        ('recupero', 'Recupero de siniestro')
    ]
    ESTADOS_CHOICES = [
        ('particular_uno', 'Enviar presupuesto a cliente'),
        ('particular_dos', 'Cobrar seña y asignar cita'),
        ('particular_tres', 'Cobrar primera mitad (descontando seña)'),
        ('particular_cuatro', 'Ingresar el auto al taller y realizar los trabajos correspondientes'),
        ('particular_cinco', 'Coordinar fecha de retiro con el dueño'),
        ('particular_seis', 'Cobrar segunda mitad'),
        ('terceros_uno', 'Primer paso de terceros'),
        ('riesgo_uno', 'Primer paso de riesgo'),
        ('recupero_uno', 'Primer paso de recupero'),
    ]

    nombre_cliente = models.CharField(max_length=200, verbose_name='Nombre del cliente', blank=False)
    telefono_cliente = models.CharField(max_length=200, verbose_name='Telefono del cliente', blank=False)
    marca_vehiculo = models.CharField(max_length=200, verbose_name='Marca del vehiculo', blank=False)
    modelo_vehiculo = models.CharField(max_length=200, verbose_name='Modelo del vehiculo', blank=False)
    patente_vehiculo = models.CharField(max_length=200, verbose_name='Patente del vehiculo', blank=False)
    imagenes = models.ImageField(upload_to='Imagenes/', verbose_name='Imagenes del vehiculo', blank=True, null=True)
    modalidad = models.CharField(max_length=50, choices=MODALIDAD_CHOICES, verbose_name='Modalidad de cobertura', blank=False)
    estado = models.CharField(max_length=50, choices=ESTADOS_CHOICES, verbose_name='Estado', blank=True)
    trabajos_a_realizar = models.TextField(verbose_name="Trabajos a realizar")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'orden'
        verbose_name_plural = 'ordenes'

    def __str__(self):
        return (self.marca_vehiculo + ' ' + self.modelo_vehiculo + ' de ' + self.nombre_cliente)
