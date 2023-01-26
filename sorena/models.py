from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator

# Create your models here.
class Coach(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(blank=True, max_length=11, validators=[MinLengthValidator(11)])

    def __str__(self):
        return f"{self.name}"

class Field(models.Model):
    field = models.CharField(max_length=200)
    def __str__(self):
        return f"Field: {self.field}"

class Sorena_User(models.Model):
    
    
    name = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    number = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    national_id = models.CharField(max_length=10, validators=[MinLengthValidator(10)], unique=True)
    birthyear = models.IntegerField(validators=[MinValueValidator(1300), MaxValueValidator(1402)])
    birthmonth = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    birthday = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)])
    start_insurance_year = models.IntegerField(validators=[MinValueValidator(1300), MaxValueValidator(1402)])
    start_insurance_month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    start_insurance_day = models.IntegerField(blank=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    end_insurance_year = models.IntegerField(blank=True, validators=[MinValueValidator(1300), MaxValueValidator(1402)])
    coach = models.ForeignKey(Coach, on_delete = models.CASCADE, related_name="coaches")
    field = models.ForeignKey(Field, on_delete= models.CASCADE, related_name="fields")
    

    def __str__(self):
        return f"{self.name} {self.last} number: {self.number} start_insurance_year: {self.start_insurance_year}"




class Admin(models.Model):
    username = models.CharField(max_length=200, unique=True)


    

   