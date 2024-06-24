from django.db import models # type: ignore

# Create your models here.

#creating Company Model
class Company(models.Model):
    Company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100, choices= 
                          (('IT','IT'),
                           ('Non IT','Non IT'),
                           ('Fianace','Fianace')
                           ))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name + ' ' + self.location

#employee model
class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=50,choices=(
        ('Manager','Manager'),
        ('Develpoer','Developer'),
        ('Project Leader','Project Leader')
    ))
    Company=models.ForeignKey(Company, on_delete=models.CASCADE)