from django.db import models
from django.contrib.auth.models import User

# Create your models here.
 
class Sexo(models.Model):
    id_sexo = models.IntegerField(primary_key=True)
    descripccion = models.CharField(max_length=20)

class Lectores(models.Model):
 id_lector = models.AutoField(primary_key=True)
 nombre = models.CharField(max_length=50)
 apellido = models.CharField(max_length=50)
 correo = models.EmailField()
 sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
 usuario = models.ForeignKey(User,on_delete=models.CASCADE)
 


class Metodo_Pago(models.Model):
    id_pago= models.IntegerField(primary_key=True)
    tipo_pago = models.CharField(max_length=20)
    moneda = models.CharField(max_length=20)


class Pedido(models.Model):
    id_pedido= models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Lectores, on_delete=models.CASCADE)
    direccion = models.TextField()
    total = models.DecimalField(max_digits=19, decimal_places=2)
    fecha = models.DateField(auto_now = True)
    metodo =models.ForeignKey(Metodo_Pago, on_delete=models.CASCADE)



class Autor(models.Model):
    id_autor = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()

class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    precio = models.DecimalField(max_digits=19, decimal_places=2)
    nombre = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    sinopsis = models.CharField(max_length=300)
    anio = models.DateField(auto_now=False, auto_now_add=False)
    autor =models.ForeignKey(Autor, on_delete=models.CASCADE)

class Genero (models.Model):
    id_genero = models.IntegerField(primary_key=True)
    tipo_genero = models.CharField(max_length=50)
    genero =models.ForeignKey(Libro, on_delete=models.CASCADE)

class Formato(models.Model):
    id_formato = models.IntegerField(primary_key=True)
    tipo_formato = models.CharField(max_length=50)
    libro =models.ForeignKey(Libro, on_delete=models.CASCADE)

class Detalle_Pedido ( models.Model):
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    id_detalle_pedido = models.IntegerField(primary_key=True)
    id_libro =  models.ForeignKey(Libro, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=19, decimal_places=2)





    










