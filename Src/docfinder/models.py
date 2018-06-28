from django.db import models


class Specialty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Insurance(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=50, null=True)
    zip_code = models.CharField(max_length=10, null=True)
    gender = models.CharField(max_length=5, null=True)
    phone_number = models.CharField(max_length=11, null=True)
    specialties = models.ManyToManyField(Specialty)
    insurances = models.ManyToManyField(Insurance)

    def __str__(self):
        return self.first_name + " " + self.last_name


class User(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=100, null=True)
    age = models.CharField(max_length=3, null=True)
    gender = models.CharField(max_length=5, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Preference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=200, null=True)
    value = models.CharField(max_length=200, null=True)




