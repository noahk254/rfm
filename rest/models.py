from django.db import models

class Livestock(models.Model):
    type = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    health_status = models.CharField(max_length=100)
    weight = models.FloatField()
    last_checkup_date = models.DateField()

    def __str__(self):
        return f"{self.type} - {self.breed}"
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    salary = models.FloatField()
    start_date = models.DateField()

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    products = models.TextField(help_text="Comma-separated list of products") 

    def __str__(self):
        return self.name 
