from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator

# Create your models here.
class Gym(models.Model):
    gym = models.CharField(max_length=200)
    address = models.TextField()
    number = models.CharField(max_length=11, validators=[MinLengthValidator(8)])

    def __str__(self):
        return f"{self.gym}"

class Coach(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(blank=True, max_length=11, validators=[MinLengthValidator(11)])

    def __str__(self):
        return f"{self.name}"

class Field(models.Model):
    field = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.field}"

class Sorena_User(models.Model):
    
    
    name = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    number = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    national = models.CharField(max_length=10, validators=[MinLengthValidator(10)], unique=True)
    birthyear = models.IntegerField(validators=[MinValueValidator(1300), MaxValueValidator(1402)])
    birthmonth = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    birthday = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)])
    start_insurance_year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1300), MaxValueValidator(1402)])
    start_insurance_month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    start_insurance_day = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    coach = models.ForeignKey(Coach, on_delete = models.CASCADE, default=0)
    field = models.ForeignKey(Field, on_delete= models.CASCADE, default=0)
    

    def __str__(self):
        return f"{self.name} {self.last} number: {self.number} start_insurance_year: {self.start_insurance_year}"

class Time(models.Model):
    field = models.ForeignKey(Field, on_delete= models.CASCADE)
    coach = models.ForeignKey(Coach, on_delete = models.CASCADE)
    day = models.CharField(max_length=200)
    time = models.TimeField()
    gym = models.ForeignKey(Gym, on_delete= models.CASCADE, related_name="gyms")

    def __str__(self):
        return f"{self.field} {self.coach} {self.gym}"


class Admin(models.Model):
    username = models.CharField(max_length=200, unique=True)


    

   