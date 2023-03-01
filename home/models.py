from django.db import models
import datetime


class ServiceInfo(models.Model):
    happy_clients = models.IntegerField()
    hard_worker = models.IntegerField()
    tie_ups = models.IntegerField()
    support = models.IntegerField()


class Testimonials(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    message = models.CharField(max_length=200)
    image = models.CharField(max_length=5000, null=True, blank=True)
    occupation = models.CharField(max_length=30, null=True, blank=True)


class Pg(models.Model):
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=5000, null=True, blank=True)


class Contacts(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    email = models.EmailField()
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Register(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    gender = models.CharField(max_length=10)
    room = models.CharField(max_length=10)
    college = models.CharField(max_length=100)
    taxi_service = models.CharField(max_length=10, blank=True, default="No")
    hotel_service = models.CharField(max_length=10, blank=True, default="No")
    checked = models.CharField(max_length=5, blank=True, choices=(("Y", "Yes"), ("N", "No")))
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class Test(models.Model):
    name = models.CharField(max_length=40)
    college = models.CharField(max_length=50)

